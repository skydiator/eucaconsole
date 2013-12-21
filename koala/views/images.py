# -*- coding: utf-8 -*-
"""
Pyramid views for Eucalyptus and AWS images

"""
from urllib import urlencode

from beaker.cache import cache_region
from boto.exception import EC2ResponseError
from pyramid.httpexceptions import HTTPFound
from pyramid.i18n import TranslationString as _
from pyramid.view import view_config


from ..constants.images import EUCA_IMAGE_OWNER_ALIAS_CHOICES, AWS_IMAGE_OWNER_ALIAS_CHOICES
from ..forms.images import ImageForm
from ..models import Notification
from ..models import LandingPageFilter
from ..views import BaseView, LandingPageView,  TaggedItemView


class ImagesView(LandingPageView):
    TEMPLATE = '../templates/images/images.pt'

    def __init__(self, request):
        super(ImagesView, self).__init__(request)
        self.initial_sort_key = 'name'
        self.prefix = '/images'

    @view_config(route_name='images', renderer=TEMPLATE)
    def images_landing(self):
        json_items_endpoint = self.request.route_url('images_json')
        if self.request.GET:
            json_items_endpoint += '?{params}'.format(params=urlencode(self.request.GET))
        # Filter fields are passed to 'properties_filter_form' template macro to display filters at left
        owner_choices = EUCA_IMAGE_OWNER_ALIAS_CHOICES
        if self.cloud_type == 'aws':
            owner_choices = AWS_IMAGE_OWNER_ALIAS_CHOICES
        self.filter_fields = [
            LandingPageFilter(key='owner_alias', name='Images owned by', choices=owner_choices),
        ]
        # filter_keys are passed to client-side filtering in search box
        self.filter_keys = ['architecture', 'description', 'id', 'name', 'owner_alias']
        # sort_keys are passed to sorting drop-down
        self.sort_keys = [
            dict(key='id', name='ID'),
            dict(key='name', name=_(u'Image name')),
            dict(key='architecture', name=_(u'Architecture')),
            dict(key='platform', name=_(u'Platform')),
            dict(key='description', name=_(u'Description')),
        ]

        return dict(
            display_type=self.display_type,
            filter_fields=self.filter_fields,
            filter_keys=self.filter_keys,
            sort_keys=self.sort_keys,
            prefix=self.prefix,
            initial_sort_key=self.initial_sort_key,
            json_items_endpoint=json_items_endpoint,
        )


class ImagesJsonView(BaseView):
    """Images returned as JSON"""
    @view_config(route_name='images_json', renderer='json', request_method='GET')
    def images_json(self):
        images = []
        for image in self.get_items():
            images.append(dict(
                architecture=image.architecture,
                description=image.description,
                id=image.id,
                kernel_id=image.kernel_id,
                name=image.name,
                owner_alias=image.owner_alias,
                platform=image.platform,  # TODO: get platform via util method
                root_device_type=image.root_device_type,
                type=image.type,
            ))
        return dict(results=images)

    def get_items(self):
        owner_alias = self.request.params.get('owner_alias')
        if not owner_alias and self.cloud_type == 'aws':
            # Set default alias to 'amazon' for AWS
            owner_alias = 'amazon'
        owners = [owner_alias] if owner_alias else []
        conn = self.get_connection()
        region = self.request.session.get('region')
        return self.get_images(conn, owners, region)

    def get_images(self, conn, owners, region):
        """Get images, leveraging Beaker cache for long_term duration (3600 seconds)"""
        cache_key = 'images_cache_{owners}_{region}'.format(owners=owners, region=region)

        @cache_region('long_term', cache_key)
        def _get_images_cache(_owners, _region):
            try:
                return conn.get_all_images(owners=_owners) if conn else []
            except EC2ResponseError as exc:
                return BaseView.handle_403_error(exc, request=self.request)
        return _get_images_cache(owners, region)


class ImageView(TaggedItemView):
    """Views for single Image"""
    TEMPLATE = '../templates/images/image_view.pt'

    def __init__(self, request):
        super(ImageView, self).__init__(request)
        self.conn = self.get_connection()
        self.image = self.get_image()
        self.image_form = ImageForm(self.request, formdata=self.request.params or None)
        self.tagged_obj = self.image
        self.render_dict = dict(
            image=self.image,
            image_form=self.image_form,
        )

    def get_image(self):
        image_param = self.request.matchdict.get('id')
        images_param = [image_param]
        images = self.conn.get_all_images(image_ids=images_param)
        image = images[0] if images else None
        return image 

    @view_config(route_name='image_view', renderer=TEMPLATE)
    def image_view(self):
        return self.render_dict
 
    @view_config(route_name='image_update', request_method='POST', renderer=TEMPLATE)
    def image_update(self):
        if self.image_form.validate():
            self.update_tags()

            location = self.request.route_url('image_view', id=self.image.id)
            msg = _(u'Successfully modified image')
            self.request.session.flash(msg, queue=Notification.SUCCESS)
            return HTTPFound(location=location)

        return self.render_dict

