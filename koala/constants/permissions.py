# -*- coding: utf-8 -*-
"""
Constants for IAM Policy permissions (actions)

"""
from pyramid.i18n import TranslationString as _


# Policy Generator Actions for EC2
EC2_ACTIONS = [
    # 'ActivateLicense',
    'AllocateAddress',
    'AssignPrivateIpAddresses',
    'AssociateAddress',
    # 'AssociateDhcpOptions',
    # 'AssociateRouteTable',
    # 'AttachInternetGateway',
    # 'AttachNetworkInterface',
    'AttachVolume',
    # 'AttachVpnGateway',
    'AuthorizeSecurityGroupEgress',
    'AuthorizeSecurityGroupIngress',
    # 'BundleInstance',
    # 'CancelBundleTask',
    # 'CancelConversionTask',
    # 'CancelExportTask',
    'CancelReservedInstancesListing',
    # 'CancelSpotInstanceRequests',
    # 'ConfirmProductInstance',
    'CopyImage',
    'CopySnapshot',
    # 'CreateCustomerGateway',
    # 'CreateDhcpOptions',
    'CreateImage',
    # 'CreateInstanceExportTask',
    # 'CreateInternetGateway',
    'CreateKeyPair',
    # 'CreateNetworkAcl',
    # 'CreateNetworkAclEntry',
    # 'CreateNetworkInterface',
    'CreatePlacementGroup',
    'CreateReservedInstancesListing',
    # 'CreateRoute',
    # 'CreateRouteTable',
    'CreateSecurityGroup',
    'CreateSnapshot',
    # 'CreateSpotDatafeedSubscription',
    # 'CreateSubnet',
    'CreateTags',
    'CreateVolume',
    # 'CreateVpc',
    # 'CreateVpnConnection',
    # 'CreateVpnConnectionRoute',
    # 'CreateVpnGateway',
    # 'DeactivateLicense',
    # 'DeleteCustomerGateway',
    # 'DeleteDhcpOptions',
    # 'DeleteInternetGateway',
    'DeleteKeyPair',
    # 'DeleteNetworkAcl',
    # 'DeleteNetworkAclEntry',
    # 'DeleteNetworkInterface',
    'DeletePlacementGroup',
    # 'DeleteRoute',
    # 'DeleteRouteTable',
    'DeleteSecurityGroup',
    'DeleteSnapshot',
    # 'DeleteSpotDatafeedSubscription',
    # 'DeleteSubnet',
    'DeleteTags',
    'DeleteVolume',
    # 'DeleteVpc',
    # 'DeleteVpnConnection',
    # 'DeleteVpnConnectionRoute',
    # 'DeleteVpnGateway',
    'DeregisterImage',
    'DescribeAccountAttributes',
    'DescribeAddresses',
    'DescribeAvailabilityZones',
    # 'DescribeBundleTasks',
    # 'DescribeConversionTasks',
    # 'DescribeCustomerGateways',
    # 'DescribeDhcpOptions',
    # 'DescribeExportTasks',
    'DescribeImageAttribute',
    'DescribeImages',
    'DescribeInstanceAttribute',
    'DescribeInstanceStatus',
    'DescribeInstances',
    # 'DescribeInternetGateways',
    'DescribeKeyPairs',
    # 'DescribeLicenses',
    # 'DescribeNetworkAcls',
    # 'DescribeNetworkInterfaceAttribute',
    # 'DescribeNetworkInterfaces',
    'DescribePlacementGroups',
    'DescribeRegions',
    'DescribeReservedInstances',
    'DescribeReservedInstancesListings',
    'DescribeReservedInstancesModifications',
    'DescribeReservedInstancesOfferings',
    # 'DescribeRouteTables',
    'DescribeSecurityGroups',
    'DescribeSnapshotAttribute',
    'DescribeSnapshots',
    # 'DescribeSpotDatafeedSubscription',
    # 'DescribeSpotInstanceRequests',
    # 'DescribeSpotPriceHistory',
    # 'DescribeSubnets',
    'DescribeTags',
    'DescribeVolumeAttribute',
    'DescribeVolumeStatus',
    'DescribeVolumes',
    # 'DescribeVpcAttribute',
    # 'DescribeVpcs',
    # 'DescribeVpnConnections',
    # 'DescribeVpnGateways',
    # 'DetachInternetGateway',
    # 'DetachNetworkInterface',
    'DetachVolume',
    # 'DetachVpnGateway',
    # 'DisableVgwRoutePropagation',
    'DisassociateAddress',
    # 'DisassociateRouteTable',
    # 'EnableVgwRoutePropagation',
    'EnableVolumeIO',
    'GetConsoleOutput',
    'GetPasswordData',
    'ImportInstance',
    'ImportKeyPair',
    'ImportVolume',
    'ModifyImageAttribute',
    'ModifyInstanceAttribute',
    'ModifyNetworkInterfaceAttribute',
    'ModifyReservedInstances',
    'ModifySnapshotAttribute',
    'ModifyVolumeAttribute',
    # 'ModifyVpcAttribute',
    'MonitorInstances',
    # 'PurchaseReservedInstancesOffering',
    'RebootInstances',
    'RegisterImage',
    'ReleaseAddress',
    # 'ReplaceNetworkAclAssociation',
    # 'ReplaceNetworkAclEntry',
    # 'ReplaceRoute',
    # 'ReplaceRouteTableAssociation',
    'ReportInstanceStatus',
    # 'RequestSpotInstances',
    'ResetImageAttribute',
    'ResetInstanceAttribute',
    # 'ResetNetworkInterfaceAttribute',
    'ResetSnapshotAttribute',
    'RevokeSecurityGroupEgress',
    'RevokeSecurityGroupIngress',
    'RunInstances',
    'StartInstances',
    'StopInstances',
    'TerminateInstances',
    'UnassignPrivateIpAddresses',
    'UnmonitorInstances',
]


# Policy Generator Actions for AutoScaling
AUTOSCALING_ACTIONS = [
    'CreateAutoScalingGroup',
    'CreateLaunchConfiguration',
    'CreateOrUpdateScalingTrigger',
    'CreateOrUpdateTags',
    'DeleteAutoScalingGroup',
    'DeleteLaunchConfiguration',
    'DeleteNotificationConfiguration',
    'DeletePolicy',
    'DeleteScheduledAction',
    'DeleteTags',
    'DeleteTrigger',
    'DescribeAdjustmentTypes',
    'DescribeAutoScalingGroups',
    'DescribeAutoScalingInstances',
    'DescribeAutoScalingNotificationTypes',
    'DescribeLaunchConfigurations',
    'DescribeMetricCollectionTypes',
    'DescribeNotificationConfigurations',
    'DescribePolicies',
    'DescribeScalingActivities',
    'DescribeScalingProcessTypes',
    'DescribeScheduledActions',
    'DescribeTags',
    'DescribeTriggers',
    'DisableMetricsCollection',
    'EnableMetricsCollection',
    'ExecutePolicy',
    'PutNotificationConfiguration',
    'PutScalingPolicy',
    'PutScheduledUpdateGroupAction',
    'ResumeProcesses',
    'SetDesiredCapacity',
    'SetInstanceHealth',
    'SuspendProcesses',
    'TerminateInstanceInAutoScalingGroup',
    'UpdateAutoScalingGroup',
]

# Policy Generator Actions for Elastic Load Balancing
ELB_ACTIONS = [
    'ConfigureHealthCheck',
    'CreateAppCookieStickinessPolicy',
    'CreateLBCookieStickinessPolicy',
    'CreateLoadBalancer',
    'CreateLoadBalancerListeners',
    'DeleteLoadBalancer',
    'DeleteLoadBalancerListeners',
    'DeleteLoadBalancerPolicy',
    'DeregisterInstancesFromLoadBalancer',
    'DescribeInstanceHealth',
    'DescribeLoadBalancers',
    'DisableAvailabilityZonesForLoadBalancer',
    'EnableAvailabilityZonesForLoadBalancer',
    'RegisterInstancesWithLoadBalancer',
    'SetLoadBalancerListenerSSLCertificate',
    'SetLoadBalancerPoliciesOfListener',
]


# Policy Generator Actions for CloudWatch
CLOUDWATCH_ACTIONS = [
    'DeleteAlarms',
    'DescribeAlarmHistory',
    'DescribeAlarms',
    'DescribeAlarmsForMetric',
    'DisableAlarmActions',
    'EnableAlarmActions',
    'GetMetricStatistics',
    'ListMetrics',
    'PutMetricAlarm',
    'PutMetricData',
    'SetAlarmState',
]


POLICY_ACTIONS = [
    {
        'name': 'ec2',
        'label': _(u'All EC2 actions'),
        'actions': EC2_ACTIONS,
    },
    {
        'name': 'elasticloadbalancing',
        'label': _(u'All Load Balancing actions'),
        'actions': ELB_ACTIONS,
    },
    {
        'name': 'autoscaling',
        'label': _(u'All Autoscaling actions'),
        'actions': AUTOSCALING_ACTIONS,
    },
    {
        'name': 'cloudwatch',
        'label': _(u'All CloudWatch actions'),
        'actions': CLOUDWATCH_ACTIONS,
    },
]


