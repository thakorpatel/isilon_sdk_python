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


class NdmpContextsBreContext(object):
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
        'bre_context_id': 'str',
        'id': 'str'
    }

    attribute_map = {
        'bre_context_id': 'bre_context_id',
        'id': 'id'
    }

    def __init__(self, bre_context_id=None, id=None):  # noqa: E501
        """NdmpContextsBreContext - a model defined in Swagger"""  # noqa: E501

        self._bre_context_id = None
        self._id = None
        self.discriminator = None

        if bre_context_id is not None:
            self.bre_context_id = bre_context_id
        if id is not None:
            self.id = id

    @property
    def bre_context_id(self):
        """Gets the bre_context_id of this NdmpContextsBreContext.  # noqa: E501

        Unique ID of NDMP BRE context  # noqa: E501

        :return: The bre_context_id of this NdmpContextsBreContext.  # noqa: E501
        :rtype: str
        """
        return self._bre_context_id

    @bre_context_id.setter
    def bre_context_id(self, bre_context_id):
        """Sets the bre_context_id of this NdmpContextsBreContext.

        Unique ID of NDMP BRE context  # noqa: E501

        :param bre_context_id: The bre_context_id of this NdmpContextsBreContext.  # noqa: E501
        :type: str
        """

        self._bre_context_id = bre_context_id

    @property
    def id(self):
        """Gets the id of this NdmpContextsBreContext.  # noqa: E501

        Unique display id.  # noqa: E501

        :return: The id of this NdmpContextsBreContext.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NdmpContextsBreContext.

        Unique display id.  # noqa: E501

        :param id: The id of this NdmpContextsBreContext.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, NdmpContextsBreContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
