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


class ClusterNodesError(object):
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
        'failed_upgrade_action': 'str',
        'log': 'str'
    }

    attribute_map = {
        'failed_upgrade_action': 'failed_upgrade_action',
        'log': 'log'
    }

    def __init__(self, failed_upgrade_action=None, log=None):  # noqa: E501
        """ClusterNodesError - a model defined in Swagger"""  # noqa: E501

        self._failed_upgrade_action = None
        self._log = None
        self.discriminator = None

        if failed_upgrade_action is not None:
            self.failed_upgrade_action = failed_upgrade_action
        if log is not None:
            self.log = log

    @property
    def failed_upgrade_action(self):
        """Gets the failed_upgrade_action of this ClusterNodesError.  # noqa: E501

        Last upgrade step which failed on node.  # noqa: E501

        :return: The failed_upgrade_action of this ClusterNodesError.  # noqa: E501
        :rtype: str
        """
        return self._failed_upgrade_action

    @failed_upgrade_action.setter
    def failed_upgrade_action(self, failed_upgrade_action):
        """Sets the failed_upgrade_action of this ClusterNodesError.

        Last upgrade step which failed on node.  # noqa: E501

        :param failed_upgrade_action: The failed_upgrade_action of this ClusterNodesError.  # noqa: E501
        :type: str
        """

        self._failed_upgrade_action = failed_upgrade_action

    @property
    def log(self):
        """Gets the log of this ClusterNodesError.  # noqa: E501

        Upgrade error log.  # noqa: E501

        :return: The log of this ClusterNodesError.  # noqa: E501
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this ClusterNodesError.

        Upgrade error log.  # noqa: E501

        :param log: The log of this ClusterNodesError.  # noqa: E501
        :type: str
        """

        self._log = log

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
        if not isinstance(other, ClusterNodesError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
