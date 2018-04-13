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

from isi_sdk_8_0.models.event_eventlist import EventEventlist  # noqa: F401,E501


class EventEventlists(object):
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
        'eventlists': 'list[EventEventlist]'
    }

    attribute_map = {
        'eventlists': 'eventlists'
    }

    def __init__(self, eventlists=None):  # noqa: E501
        """EventEventlists - a model defined in Swagger"""  # noqa: E501

        self._eventlists = None
        self.discriminator = None

        if eventlists is not None:
            self.eventlists = eventlists

    @property
    def eventlists(self):
        """Gets the eventlists of this EventEventlists.  # noqa: E501


        :return: The eventlists of this EventEventlists.  # noqa: E501
        :rtype: list[EventEventlist]
        """
        return self._eventlists

    @eventlists.setter
    def eventlists(self, eventlists):
        """Sets the eventlists of this EventEventlists.


        :param eventlists: The eventlists of this EventEventlists.  # noqa: E501
        :type: list[EventEventlist]
        """

        self._eventlists = eventlists

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
        if not isinstance(other, EventEventlists):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
