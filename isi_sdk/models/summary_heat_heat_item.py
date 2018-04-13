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


class SummaryHeatHeatItem(object):
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
        'class_name': 'str',
        'event_name': 'str',
        'event_type': 'int',
        'lin': 'str',
        'node': 'int',
        'operation_rate': 'float',
        'path': 'str',
        'time': 'int'
    }

    attribute_map = {
        'class_name': 'class_name',
        'event_name': 'event_name',
        'event_type': 'event_type',
        'lin': 'lin',
        'node': 'node',
        'operation_rate': 'operation_rate',
        'path': 'path',
        'time': 'time'
    }

    def __init__(self, class_name=None, event_name=None, event_type=None, lin=None, node=None, operation_rate=None, path=None, time=None):  # noqa: E501
        """SummaryHeatHeatItem - a model defined in Swagger"""  # noqa: E501

        self._class_name = None
        self._event_name = None
        self._event_type = None
        self._lin = None
        self._node = None
        self._operation_rate = None
        self._path = None
        self._time = None
        self.discriminator = None

        self.class_name = class_name
        self.event_name = event_name
        if event_type is not None:
            self.event_type = event_type
        if lin is not None:
            self.lin = lin
        if node is not None:
            self.node = node
        self.operation_rate = operation_rate
        self.path = path
        self.time = time

    @property
    def class_name(self):
        """Gets the class_name of this SummaryHeatHeatItem.  # noqa: E501

        The class of operation  # noqa: E501

        :return: The class_name of this SummaryHeatHeatItem.  # noqa: E501
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this SummaryHeatHeatItem.

        The class of operation  # noqa: E501

        :param class_name: The class_name of this SummaryHeatHeatItem.  # noqa: E501
        :type: str
        """
        if class_name is None:
            raise ValueError("Invalid value for `class_name`, must not be `None`")  # noqa: E501

        self._class_name = class_name

    @property
    def event_name(self):
        """Gets the event_name of this SummaryHeatHeatItem.  # noqa: E501

        The type of event  # noqa: E501

        :return: The event_name of this SummaryHeatHeatItem.  # noqa: E501
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this SummaryHeatHeatItem.

        The type of event  # noqa: E501

        :param event_name: The event_name of this SummaryHeatHeatItem.  # noqa: E501
        :type: str
        """
        if event_name is None:
            raise ValueError("Invalid value for `event_name`, must not be `None`")  # noqa: E501

        self._event_name = event_name

    @property
    def event_type(self):
        """Gets the event_type of this SummaryHeatHeatItem.  # noqa: E501

        The event type id  # noqa: E501

        :return: The event_type of this SummaryHeatHeatItem.  # noqa: E501
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this SummaryHeatHeatItem.

        The event type id  # noqa: E501

        :param event_type: The event_type of this SummaryHeatHeatItem.  # noqa: E501
        :type: int
        """

        self._event_type = event_type

    @property
    def lin(self):
        """Gets the lin of this SummaryHeatHeatItem.  # noqa: E501

        Logical inode (LIN)  # noqa: E501

        :return: The lin of this SummaryHeatHeatItem.  # noqa: E501
        :rtype: str
        """
        return self._lin

    @lin.setter
    def lin(self, lin):
        """Sets the lin of this SummaryHeatHeatItem.

        Logical inode (LIN)  # noqa: E501

        :param lin: The lin of this SummaryHeatHeatItem.  # noqa: E501
        :type: str
        """

        self._lin = lin

    @property
    def node(self):
        """Gets the node of this SummaryHeatHeatItem.  # noqa: E501

        The node where this event occurred.  # noqa: E501

        :return: The node of this SummaryHeatHeatItem.  # noqa: E501
        :rtype: int
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this SummaryHeatHeatItem.

        The node where this event occurred.  # noqa: E501

        :param node: The node of this SummaryHeatHeatItem.  # noqa: E501
        :type: int
        """

        self._node = node

    @property
    def operation_rate(self):
        """Gets the operation_rate of this SummaryHeatHeatItem.  # noqa: E501

        Approximate operations per second for this lin.  # noqa: E501

        :return: The operation_rate of this SummaryHeatHeatItem.  # noqa: E501
        :rtype: float
        """
        return self._operation_rate

    @operation_rate.setter
    def operation_rate(self, operation_rate):
        """Sets the operation_rate of this SummaryHeatHeatItem.

        Approximate operations per second for this lin.  # noqa: E501

        :param operation_rate: The operation_rate of this SummaryHeatHeatItem.  # noqa: E501
        :type: float
        """
        if operation_rate is None:
            raise ValueError("Invalid value for `operation_rate`, must not be `None`")  # noqa: E501

        self._operation_rate = operation_rate

    @property
    def path(self):
        """Gets the path of this SummaryHeatHeatItem.  # noqa: E501

        Canonical LIN path if known  # noqa: E501

        :return: The path of this SummaryHeatHeatItem.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this SummaryHeatHeatItem.

        Canonical LIN path if known  # noqa: E501

        :param path: The path of this SummaryHeatHeatItem.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def time(self):
        """Gets the time of this SummaryHeatHeatItem.  # noqa: E501

        Unix Epoch time in seconds of the request.  # noqa: E501

        :return: The time of this SummaryHeatHeatItem.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this SummaryHeatHeatItem.

        Unix Epoch time in seconds of the request.  # noqa: E501

        :param time: The time of this SummaryHeatHeatItem.  # noqa: E501
        :type: int
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

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
        if not isinstance(other, SummaryHeatHeatItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
