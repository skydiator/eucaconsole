from pages.detailpage import DetailPage


class ASGDetailPage(DetailPage):

    def __init__(self, tester):
        self.tester = tester

    _asg_detail_page_title = "Details for scaling group: {0}" #asg name required
    _next_step_modal_id = "nextstep-scalinggroup-modal"
    _do_notshow_again_checkbox_id = "check-do-not-show-me-again"
    _close_modal_x_css = "#nextstep-scalinggroup-modal>a.close-reveal-modal"
    _scaling_policies_tab_css = "[href='/scalinggroups/{0}/policies']" #asg name required
    _instances_tab_css = "[href='/scalinggroups/{0}/instances']" #asg name required


    _delete_volume_action_menuitem_id = "delete-volume-action"
    _attach_volume_action_menuitem_id = "attach-volume-action"
    _volume_status_css = "[class='label radius status {0}']"  # volume status is required
    _create_snapshot_tile_css = "#create-snapshot>a"
    _snapshots_tab_css = "[href='/volumes/{0}/snapshots']"  # volume_id is required
    _general_tab_css = '[href="/volumes/{0}/snapshots"]'  # volume_id is required
    _active_tab_css ="dd.active"
    _id_link_in_tile_of_newly_created_snapshot_css='[class="ng-binding"]'

    def verify_asg_detail_page_loaded(self, asg_name):
        """
        Waits for the asg detail page title to appear; waits for actions menu to become visible. Closes the next step modal.
        """
        if self.tester.check_visibility_by_id(self._next_step_modal_id):
            self.tester.click_element_by_css(self._close_modal_x_css)
        self.tester.wait_for_text_present_by_id(DetailPage(self)._detail_page_title_id, self._asg_detail_page_title.format(asg_name))
        self.tester.wait_for_element_present_by_css(DetailPage(self)._actions_menu_css)




    def click_action_delete_volume_on_detail_page(self):
        self.tester.click_element_by_css(DetailPage._actions_menu_css)
        self.tester.click_element_by_id(self._delete_volume_action_menuitem_id)

    def click_action_attach_volume_on_detail_page(self):
        self.tester.click_element_by_css(DetailPage._actions_menu_css)
        self.tester.click_element_by_id(self._attach_volume_action_menuitem_id)

    def verify_volume_status_is_available(self, timeout_in_seconds):
        self.tester.wait_for_visible_by_css(self._volume_status_css.format("available"), timeout_in_seconds)

    def verify_volume_status_is_attached(self, timeout_in_seconds):
        self.tester.wait_for_visible_by_css(self._volume_status_css.format("attached"), timeout_in_seconds)

    def get_volume_name_and_id(self):
        name_and_id = str(self.tester.store_text_by_css(DetailPage(self)._resource_name_and_id_css))
        if len(name_and_id) > 12:
            volume_id = name_and_id[-13:-1]
            volume_name = name_and_id[1:-15]
        else:
            volume_name = None
            volume_id = name_and_id
        return {'volume_name': volume_name, 'volume_id': volume_id}

    def goto_snapshots_tab(self, volume_id):
        """
        Checks if Snapshot tab is already open. Opens snapshot tab if not.
        """
        tab = self.tester.store_text_by_css(self._active_tab_css)
        print "Found active tab {0}".format(tab)
        if tab == "General":
            self.tester.click_element_by_css(self._snapshots_tab_css.format(volume_id))
        elif tab == "Snapshots":
            pass
        else:
            print "ERROR: tab {0} not among recognized tab names.".format(tab)

    def click_create_snapshot_from_volume_tile(self, volume_id):
        self.goto_snapshots_tab(volume_id)
        self.tester.click_element_by_css(self._create_snapshot_tile_css)

    def goto_detail_page_of_newly_created_snapshot(self, volume_id):
        self.goto_snapshots_tab(volume_id)
        self.tester.click_element_by_css(self._id_link_in_tile_of_newly_created_snapshot_css)

    def verify_snapshot_tile_not_present(self):
        NotImplementedError




