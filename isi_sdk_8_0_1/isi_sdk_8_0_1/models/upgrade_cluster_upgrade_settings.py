# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 4
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UpgradeClusterUpgradeSettings(object):
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
        'nodes_to_rolling_upgrade': 'list[int]',
        'upgrade_type': 'str'
    }

    attribute_map = {
        'nodes_to_rolling_upgrade': 'nodes_to_rolling_upgrade',
        'upgrade_type': 'upgrade_type'
    }

    def __init__(self, nodes_to_rolling_upgrade=None, upgrade_type=None):  # noqa: E501
        """UpgradeClusterUpgradeSettings - a model defined in Swagger"""  # noqa: E501

        self._nodes_to_rolling_upgrade = None
        self._upgrade_type = None
        self.discriminator = None

        if nodes_to_rolling_upgrade is not None:
            self.nodes_to_rolling_upgrade = nodes_to_rolling_upgrade
        if upgrade_type is not None:
            self.upgrade_type = upgrade_type

    @property
    def nodes_to_rolling_upgrade(self):
        """Gets the nodes_to_rolling_upgrade of this UpgradeClusterUpgradeSettings.  # noqa: E501

        The nodes (to be) scheduled for upgrade ordered by queue position number. Null if the cluster_state is 'partially upgraded' or upgrade_type is 'simultaneous'. One of the following values: [<lnn-1>, <lnn-2>, ... ], 'All', null  # noqa: E501

        :return: The nodes_to_rolling_upgrade of this UpgradeClusterUpgradeSettings.  # noqa: E501
        :rtype: list[int]
        """
        return self._nodes_to_rolling_upgrade

    @nodes_to_rolling_upgrade.setter
    def nodes_to_rolling_upgrade(self, nodes_to_rolling_upgrade):
        """Sets the nodes_to_rolling_upgrade of this UpgradeClusterUpgradeSettings.

        The nodes (to be) scheduled for upgrade ordered by queue position number. Null if the cluster_state is 'partially upgraded' or upgrade_type is 'simultaneous'. One of the following values: [<lnn-1>, <lnn-2>, ... ], 'All', null  # noqa: E501

        :param nodes_to_rolling_upgrade: The nodes_to_rolling_upgrade of this UpgradeClusterUpgradeSettings.  # noqa: E501
        :type: list[int]
        """

        self._nodes_to_rolling_upgrade = nodes_to_rolling_upgrade

    @property
    def upgrade_type(self):
        """Gets the upgrade_type of this UpgradeClusterUpgradeSettings.  # noqa: E501

        The type of upgrade to perform. One of the following values: 'rolling', 'simultaneous'  # noqa: E501

        :return: The upgrade_type of this UpgradeClusterUpgradeSettings.  # noqa: E501
        :rtype: str
        """
        return self._upgrade_type

    @upgrade_type.setter
    def upgrade_type(self, upgrade_type):
        """Sets the upgrade_type of this UpgradeClusterUpgradeSettings.

        The type of upgrade to perform. One of the following values: 'rolling', 'simultaneous'  # noqa: E501

        :param upgrade_type: The upgrade_type of this UpgradeClusterUpgradeSettings.  # noqa: E501
        :type: str
        """

        self._upgrade_type = upgrade_type

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
        if not isinstance(other, UpgradeClusterUpgradeSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other