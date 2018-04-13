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

from isi_sdk_8_0.models.cluster_node_state_servicelight import ClusterNodeStateServicelight  # noqa: F401,E501
from isi_sdk_8_0.models.cluster_node_state_smartfail import ClusterNodeStateSmartfail  # noqa: F401,E501
from isi_sdk_8_0.models.empty import Empty  # noqa: F401,E501


class ClusterNodeState(object):
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
        'readonly': 'Empty',
        'servicelight': 'ClusterNodeStateServicelight',
        'smartfail': 'ClusterNodeStateSmartfail'
    }

    attribute_map = {
        'readonly': 'readonly',
        'servicelight': 'servicelight',
        'smartfail': 'smartfail'
    }

    def __init__(self, readonly=None, servicelight=None, smartfail=None):  # noqa: E501
        """ClusterNodeState - a model defined in Swagger"""  # noqa: E501

        self._readonly = None
        self._servicelight = None
        self._smartfail = None
        self.discriminator = None

        if readonly is not None:
            self.readonly = readonly
        if servicelight is not None:
            self.servicelight = servicelight
        if smartfail is not None:
            self.smartfail = smartfail

    @property
    def readonly(self):
        """Gets the readonly of this ClusterNodeState.  # noqa: E501

        Node readonly state.  # noqa: E501

        :return: The readonly of this ClusterNodeState.  # noqa: E501
        :rtype: Empty
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly):
        """Sets the readonly of this ClusterNodeState.

        Node readonly state.  # noqa: E501

        :param readonly: The readonly of this ClusterNodeState.  # noqa: E501
        :type: Empty
        """

        self._readonly = readonly

    @property
    def servicelight(self):
        """Gets the servicelight of this ClusterNodeState.  # noqa: E501

        Node service light state.  # noqa: E501

        :return: The servicelight of this ClusterNodeState.  # noqa: E501
        :rtype: ClusterNodeStateServicelight
        """
        return self._servicelight

    @servicelight.setter
    def servicelight(self, servicelight):
        """Sets the servicelight of this ClusterNodeState.

        Node service light state.  # noqa: E501

        :param servicelight: The servicelight of this ClusterNodeState.  # noqa: E501
        :type: ClusterNodeStateServicelight
        """

        self._servicelight = servicelight

    @property
    def smartfail(self):
        """Gets the smartfail of this ClusterNodeState.  # noqa: E501

        Node smartfail state.  # noqa: E501

        :return: The smartfail of this ClusterNodeState.  # noqa: E501
        :rtype: ClusterNodeStateSmartfail
        """
        return self._smartfail

    @smartfail.setter
    def smartfail(self, smartfail):
        """Sets the smartfail of this ClusterNodeState.

        Node smartfail state.  # noqa: E501

        :param smartfail: The smartfail of this ClusterNodeState.  # noqa: E501
        :type: ClusterNodeStateSmartfail
        """

        self._smartfail = smartfail

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
        if not isinstance(other, ClusterNodeState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
