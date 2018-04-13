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

from isi_sdk_8_0.models.storagepool_status_unhealthy_item import StoragepoolStatusUnhealthyItem  # noqa: F401,E501
from isi_sdk_8_0.models.storagepool_status_unprovisioned_item import StoragepoolStatusUnprovisionedItem  # noqa: F401,E501


class StoragepoolStatus(object):
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
        'unhealthy': 'list[StoragepoolStatusUnhealthyItem]',
        'unprovisioned': 'list[StoragepoolStatusUnprovisionedItem]'
    }

    attribute_map = {
        'unhealthy': 'unhealthy',
        'unprovisioned': 'unprovisioned'
    }

    def __init__(self, unhealthy=None, unprovisioned=None):  # noqa: E501
        """StoragepoolStatus - a model defined in Swagger"""  # noqa: E501

        self._unhealthy = None
        self._unprovisioned = None
        self.discriminator = None

        self.unhealthy = unhealthy
        self.unprovisioned = unprovisioned

    @property
    def unhealthy(self):
        """Gets the unhealthy of this StoragepoolStatus.  # noqa: E501

        Disk pools which are currently unhealthy.  # noqa: E501

        :return: The unhealthy of this StoragepoolStatus.  # noqa: E501
        :rtype: list[StoragepoolStatusUnhealthyItem]
        """
        return self._unhealthy

    @unhealthy.setter
    def unhealthy(self, unhealthy):
        """Sets the unhealthy of this StoragepoolStatus.

        Disk pools which are currently unhealthy.  # noqa: E501

        :param unhealthy: The unhealthy of this StoragepoolStatus.  # noqa: E501
        :type: list[StoragepoolStatusUnhealthyItem]
        """
        if unhealthy is None:
            raise ValueError("Invalid value for `unhealthy`, must not be `None`")  # noqa: E501

        self._unhealthy = unhealthy

    @property
    def unprovisioned(self):
        """Gets the unprovisioned of this StoragepoolStatus.  # noqa: E501

        Drives which are not currently provisioned into a disk pool.  # noqa: E501

        :return: The unprovisioned of this StoragepoolStatus.  # noqa: E501
        :rtype: list[StoragepoolStatusUnprovisionedItem]
        """
        return self._unprovisioned

    @unprovisioned.setter
    def unprovisioned(self, unprovisioned):
        """Sets the unprovisioned of this StoragepoolStatus.

        Drives which are not currently provisioned into a disk pool.  # noqa: E501

        :param unprovisioned: The unprovisioned of this StoragepoolStatus.  # noqa: E501
        :type: list[StoragepoolStatusUnprovisionedItem]
        """
        if unprovisioned is None:
            raise ValueError("Invalid value for `unprovisioned`, must not be `None`")  # noqa: E501

        self._unprovisioned = unprovisioned

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
        if not isinstance(other, StoragepoolStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
