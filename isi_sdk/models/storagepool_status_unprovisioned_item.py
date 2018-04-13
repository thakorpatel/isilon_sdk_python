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


class StoragepoolStatusUnprovisionedItem(object):
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
        'bay': 'int',
        'lnn': 'int'
    }

    attribute_map = {
        'bay': 'bay',
        'lnn': 'lnn'
    }

    def __init__(self, bay=None, lnn=None):  # noqa: E501
        """StoragepoolStatusUnprovisionedItem - a model defined in Swagger"""  # noqa: E501

        self._bay = None
        self._lnn = None
        self.discriminator = None

        self.bay = bay
        self.lnn = lnn

    @property
    def bay(self):
        """Gets the bay of this StoragepoolStatusUnprovisionedItem.  # noqa: E501

        The drive bay number.  # noqa: E501

        :return: The bay of this StoragepoolStatusUnprovisionedItem.  # noqa: E501
        :rtype: int
        """
        return self._bay

    @bay.setter
    def bay(self, bay):
        """Sets the bay of this StoragepoolStatusUnprovisionedItem.

        The drive bay number.  # noqa: E501

        :param bay: The bay of this StoragepoolStatusUnprovisionedItem.  # noqa: E501
        :type: int
        """
        if bay is None:
            raise ValueError("Invalid value for `bay`, must not be `None`")  # noqa: E501

        self._bay = bay

    @property
    def lnn(self):
        """Gets the lnn of this StoragepoolStatusUnprovisionedItem.  # noqa: E501

        The node the drive is on.  # noqa: E501

        :return: The lnn of this StoragepoolStatusUnprovisionedItem.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this StoragepoolStatusUnprovisionedItem.

        The node the drive is on.  # noqa: E501

        :param lnn: The lnn of this StoragepoolStatusUnprovisionedItem.  # noqa: E501
        :type: int
        """
        if lnn is None:
            raise ValueError("Invalid value for `lnn`, must not be `None`")  # noqa: E501

        self._lnn = lnn

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
        if not isinstance(other, StoragepoolStatusUnprovisionedItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
