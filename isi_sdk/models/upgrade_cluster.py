# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 3
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isi_sdk_8_0.models.cluster_nodes_onefs_version import ClusterNodesOnefsVersion  # noqa: F401,E501
from isi_sdk_8_0.models.upgrade_cluster_cluster_overview import UpgradeClusterClusterOverview  # noqa: F401,E501
from isi_sdk_8_0.models.upgrade_cluster_upgrade_settings import UpgradeClusterUpgradeSettings  # noqa: F401,E501


class UpgradeCluster(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'cluster_overview': 'UpgradeClusterClusterOverview',
        'cluster_state': 'str',
        'finish_time': 'str',
        'install_image_path': 'str',
        'onefs_version_current': 'ClusterNodesOnefsVersion',
        'onefs_version_upgrade': 'ClusterNodesOnefsVersion',
        'patch_action': 'str',
        'patch_name': 'str',
        'start_time': 'str',
        'upgrade_settings': 'UpgradeClusterUpgradeSettings'
    }

    attribute_map = {
        'cluster_overview': 'cluster_overview',
        'cluster_state': 'cluster_state',
        'finish_time': 'finish_time',
        'install_image_path': 'install_image_path',
        'onefs_version_current': 'onefs_version_current',
        'onefs_version_upgrade': 'onefs_version_upgrade',
        'patch_action': 'patch_action',
        'patch_name': 'patch_name',
        'start_time': 'start_time',
        'upgrade_settings': 'upgrade_settings'
    }

    def __init__(self, cluster_overview=None, cluster_state=None, finish_time=None, install_image_path=None, onefs_version_current=None, onefs_version_upgrade=None, patch_action=None, patch_name=None, start_time=None, upgrade_settings=None):  # noqa: E501
        """UpgradeCluster - a model defined in Swagger"""  # noqa: E501

        self._cluster_overview = None
        self._cluster_state = None
        self._finish_time = None
        self._install_image_path = None
        self._onefs_version_current = None
        self._onefs_version_upgrade = None
        self._patch_action = None
        self._patch_name = None
        self._start_time = None
        self._upgrade_settings = None
        self.discriminator = None

        if cluster_overview is not None:
            self.cluster_overview = cluster_overview
        if cluster_state is not None:
            self.cluster_state = cluster_state
        if finish_time is not None:
            self.finish_time = finish_time
        if install_image_path is not None:
            self.install_image_path = install_image_path
        if onefs_version_current is not None:
            self.onefs_version_current = onefs_version_current
        if onefs_version_upgrade is not None:
            self.onefs_version_upgrade = onefs_version_upgrade
        if patch_action is not None:
            self.patch_action = patch_action
        if patch_name is not None:
            self.patch_name = patch_name
        if start_time is not None:
            self.start_time = start_time
        if upgrade_settings is not None:
            self.upgrade_settings = upgrade_settings

    @property
    def cluster_overview(self):
        """Gets the cluster_overview of this UpgradeCluster.  # noqa: E501

        The cluster overview of an upgrade process.  # noqa: E501

        :return: The cluster_overview of this UpgradeCluster.  # noqa: E501
        :rtype: UpgradeClusterClusterOverview
        """
        return self._cluster_overview

    @cluster_overview.setter
    def cluster_overview(self, cluster_overview):
        """Sets the cluster_overview of this UpgradeCluster.

        The cluster overview of an upgrade process.  # noqa: E501

        :param cluster_overview: The cluster_overview of this UpgradeCluster.  # noqa: E501
        :type: UpgradeClusterClusterOverview
        """

        self._cluster_overview = cluster_overview

    @property
    def cluster_state(self):
        """Gets the cluster_state of this UpgradeCluster.  # noqa: E501

        The different states of an upgrade, rollback, or assessment. One of the following values: 'committed', 'upgraded', 'partially upgraded', 'upgrading', 'rolling back', 'assessing', 'error'  # noqa: E501

        :return: The cluster_state of this UpgradeCluster.  # noqa: E501
        :rtype: str
        """
        return self._cluster_state

    @cluster_state.setter
    def cluster_state(self, cluster_state):
        """Sets the cluster_state of this UpgradeCluster.

        The different states of an upgrade, rollback, or assessment. One of the following values: 'committed', 'upgraded', 'partially upgraded', 'upgrading', 'rolling back', 'assessing', 'error'  # noqa: E501

        :param cluster_state: The cluster_state of this UpgradeCluster.  # noqa: E501
        :type: str
        """

        self._cluster_state = cluster_state

    @property
    def finish_time(self):
        """Gets the finish_time of this UpgradeCluster.  # noqa: E501

        The time when a rollback, assessment or upgrade has finished completely. Use ISO 8601 standard. Null if the cluster_state is not 'upgraded'.  # noqa: E501

        :return: The finish_time of this UpgradeCluster.  # noqa: E501
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        """Sets the finish_time of this UpgradeCluster.

        The time when a rollback, assessment or upgrade has finished completely. Use ISO 8601 standard. Null if the cluster_state is not 'upgraded'.  # noqa: E501

        :param finish_time: The finish_time of this UpgradeCluster.  # noqa: E501
        :type: str
        """

        self._finish_time = finish_time

    @property
    def install_image_path(self):
        """Gets the install_image_path of this UpgradeCluster.  # noqa: E501

        The location (path) of the upgrade image which must be within /ifs. Null if the cluster_state is 'committed' or 'upgraded.'  # noqa: E501

        :return: The install_image_path of this UpgradeCluster.  # noqa: E501
        :rtype: str
        """
        return self._install_image_path

    @install_image_path.setter
    def install_image_path(self, install_image_path):
        """Sets the install_image_path of this UpgradeCluster.

        The location (path) of the upgrade image which must be within /ifs. Null if the cluster_state is 'committed' or 'upgraded.'  # noqa: E501

        :param install_image_path: The install_image_path of this UpgradeCluster.  # noqa: E501
        :type: str
        """

        self._install_image_path = install_image_path

    @property
    def onefs_version_current(self):
        """Gets the onefs_version_current of this UpgradeCluster.  # noqa: E501

        The current OneFS version before upgrade.  # noqa: E501

        :return: The onefs_version_current of this UpgradeCluster.  # noqa: E501
        :rtype: ClusterNodesOnefsVersion
        """
        return self._onefs_version_current

    @onefs_version_current.setter
    def onefs_version_current(self, onefs_version_current):
        """Sets the onefs_version_current of this UpgradeCluster.

        The current OneFS version before upgrade.  # noqa: E501

        :param onefs_version_current: The onefs_version_current of this UpgradeCluster.  # noqa: E501
        :type: ClusterNodesOnefsVersion
        """

        self._onefs_version_current = onefs_version_current

    @property
    def onefs_version_upgrade(self):
        """Gets the onefs_version_upgrade of this UpgradeCluster.  # noqa: E501

        The OneFS version the user is attempting to upgrade to. Null if the cluster_state is 'committed' or 'assessing.'  # noqa: E501

        :return: The onefs_version_upgrade of this UpgradeCluster.  # noqa: E501
        :rtype: ClusterNodesOnefsVersion
        """
        return self._onefs_version_upgrade

    @onefs_version_upgrade.setter
    def onefs_version_upgrade(self, onefs_version_upgrade):
        """Sets the onefs_version_upgrade of this UpgradeCluster.

        The OneFS version the user is attempting to upgrade to. Null if the cluster_state is 'committed' or 'assessing.'  # noqa: E501

        :param onefs_version_upgrade: The onefs_version_upgrade of this UpgradeCluster.  # noqa: E501
        :type: ClusterNodesOnefsVersion
        """

        self._onefs_version_upgrade = onefs_version_upgrade

    @property
    def patch_action(self):
        """Gets the patch_action of this UpgradeCluster.  # noqa: E501

        The most recent patch action performed.  # noqa: E501

        :return: The patch_action of this UpgradeCluster.  # noqa: E501
        :rtype: str
        """
        return self._patch_action

    @patch_action.setter
    def patch_action(self, patch_action):
        """Sets the patch_action of this UpgradeCluster.

        The most recent patch action performed.  # noqa: E501

        :param patch_action: The patch_action of this UpgradeCluster.  # noqa: E501
        :type: str
        """

        self._patch_action = patch_action

    @property
    def patch_name(self):
        """Gets the patch_name of this UpgradeCluster.  # noqa: E501

        The patch with the most recent patch action.  # noqa: E501

        :return: The patch_name of this UpgradeCluster.  # noqa: E501
        :rtype: str
        """
        return self._patch_name

    @patch_name.setter
    def patch_name(self, patch_name):
        """Sets the patch_name of this UpgradeCluster.

        The patch with the most recent patch action.  # noqa: E501

        :param patch_name: The patch_name of this UpgradeCluster.  # noqa: E501
        :type: str
        """

        self._patch_name = patch_name

    @property
    def start_time(self):
        """Gets the start_time of this UpgradeCluster.  # noqa: E501

        The time when an upgrade, rollback, or assessment was started. Use ISO 8601 standard. Null if the cluster_state is 'committed' or 'partially upgraded.'  # noqa: E501

        :return: The start_time of this UpgradeCluster.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this UpgradeCluster.

        The time when an upgrade, rollback, or assessment was started. Use ISO 8601 standard. Null if the cluster_state is 'committed' or 'partially upgraded.'  # noqa: E501

        :param start_time: The start_time of this UpgradeCluster.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def upgrade_settings(self):
        """Gets the upgrade_settings of this UpgradeCluster.  # noqa: E501

        The settings neccessary when starting an upgrade. Null if the cluster_state is not 'upgrading' or 'partially upgraded.' or 'error'.  # noqa: E501

        :return: The upgrade_settings of this UpgradeCluster.  # noqa: E501
        :rtype: UpgradeClusterUpgradeSettings
        """
        return self._upgrade_settings

    @upgrade_settings.setter
    def upgrade_settings(self, upgrade_settings):
        """Sets the upgrade_settings of this UpgradeCluster.

        The settings neccessary when starting an upgrade. Null if the cluster_state is not 'upgrading' or 'partially upgraded.' or 'error'.  # noqa: E501

        :param upgrade_settings: The upgrade_settings of this UpgradeCluster.  # noqa: E501
        :type: UpgradeClusterUpgradeSettings
        """

        self._upgrade_settings = upgrade_settings

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpgradeCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
