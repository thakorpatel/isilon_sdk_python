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

from isi_sdk_8_0.models.group_member import GroupMember  # noqa: F401,E501
from isi_sdk_8_0.models.quota_quota_thresholds import QuotaQuotaThresholds  # noqa: F401,E501


class QuotaQuotaCreateParams(object):
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
        'container': 'bool',
        'enforced': 'bool',
        'force': 'bool',
        'include_snapshots': 'bool',
        'path': 'str',
        'persona': 'GroupMember',
        'thresholds': 'QuotaQuotaThresholds',
        'thresholds_include_overhead': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'container': 'container',
        'enforced': 'enforced',
        'force': 'force',
        'include_snapshots': 'include_snapshots',
        'path': 'path',
        'persona': 'persona',
        'thresholds': 'thresholds',
        'thresholds_include_overhead': 'thresholds_include_overhead',
        'type': 'type'
    }

    def __init__(self, container=None, enforced=None, force=None, include_snapshots=None, path=None, persona=None, thresholds=None, thresholds_include_overhead=None, type=None):  # noqa: E501
        """QuotaQuotaCreateParams - a model defined in Swagger"""  # noqa: E501

        self._container = None
        self._enforced = None
        self._force = None
        self._include_snapshots = None
        self._path = None
        self._persona = None
        self._thresholds = None
        self._thresholds_include_overhead = None
        self._type = None
        self.discriminator = None

        if container is not None:
            self.container = container
        self.enforced = enforced
        if force is not None:
            self.force = force
        self.include_snapshots = include_snapshots
        self.path = path
        if persona is not None:
            self.persona = persona
        if thresholds is not None:
            self.thresholds = thresholds
        self.thresholds_include_overhead = thresholds_include_overhead
        self.type = type

    @property
    def container(self):
        """Gets the container of this QuotaQuotaCreateParams.  # noqa: E501

        If true, SMB shares using the quota directory see the quota thresholds as share size.  # noqa: E501

        :return: The container of this QuotaQuotaCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this QuotaQuotaCreateParams.

        If true, SMB shares using the quota directory see the quota thresholds as share size.  # noqa: E501

        :param container: The container of this QuotaQuotaCreateParams.  # noqa: E501
        :type: bool
        """

        self._container = container

    @property
    def enforced(self):
        """Gets the enforced of this QuotaQuotaCreateParams.  # noqa: E501

        True if the quota provides enforcement, otherwise a accounting quota.  # noqa: E501

        :return: The enforced of this QuotaQuotaCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._enforced

    @enforced.setter
    def enforced(self, enforced):
        """Sets the enforced of this QuotaQuotaCreateParams.

        True if the quota provides enforcement, otherwise a accounting quota.  # noqa: E501

        :param enforced: The enforced of this QuotaQuotaCreateParams.  # noqa: E501
        :type: bool
        """
        if enforced is None:
            raise ValueError("Invalid value for `enforced`, must not be `None`")  # noqa: E501

        self._enforced = enforced

    @property
    def force(self):
        """Gets the force of this QuotaQuotaCreateParams.  # noqa: E501

        Force creation of quotas on the root of /ifs.  # noqa: E501

        :return: The force of this QuotaQuotaCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this QuotaQuotaCreateParams.

        Force creation of quotas on the root of /ifs.  # noqa: E501

        :param force: The force of this QuotaQuotaCreateParams.  # noqa: E501
        :type: bool
        """

        self._force = force

    @property
    def include_snapshots(self):
        """Gets the include_snapshots of this QuotaQuotaCreateParams.  # noqa: E501

        If true, quota governs snapshot data as well as head data.  # noqa: E501

        :return: The include_snapshots of this QuotaQuotaCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._include_snapshots

    @include_snapshots.setter
    def include_snapshots(self, include_snapshots):
        """Sets the include_snapshots of this QuotaQuotaCreateParams.

        If true, quota governs snapshot data as well as head data.  # noqa: E501

        :param include_snapshots: The include_snapshots of this QuotaQuotaCreateParams.  # noqa: E501
        :type: bool
        """
        if include_snapshots is None:
            raise ValueError("Invalid value for `include_snapshots`, must not be `None`")  # noqa: E501

        self._include_snapshots = include_snapshots

    @property
    def path(self):
        """Gets the path of this QuotaQuotaCreateParams.  # noqa: E501

        The /ifs path governed.  # noqa: E501

        :return: The path of this QuotaQuotaCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this QuotaQuotaCreateParams.

        The /ifs path governed.  # noqa: E501

        :param path: The path of this QuotaQuotaCreateParams.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def persona(self):
        """Gets the persona of this QuotaQuotaCreateParams.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The persona of this QuotaQuotaCreateParams.  # noqa: E501
        :rtype: GroupMember
        """
        return self._persona

    @persona.setter
    def persona(self, persona):
        """Sets the persona of this QuotaQuotaCreateParams.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param persona: The persona of this QuotaQuotaCreateParams.  # noqa: E501
        :type: GroupMember
        """

        self._persona = persona

    @property
    def thresholds(self):
        """Gets the thresholds of this QuotaQuotaCreateParams.  # noqa: E501

          # noqa: E501

        :return: The thresholds of this QuotaQuotaCreateParams.  # noqa: E501
        :rtype: QuotaQuotaThresholds
        """
        return self._thresholds

    @thresholds.setter
    def thresholds(self, thresholds):
        """Sets the thresholds of this QuotaQuotaCreateParams.

          # noqa: E501

        :param thresholds: The thresholds of this QuotaQuotaCreateParams.  # noqa: E501
        :type: QuotaQuotaThresholds
        """

        self._thresholds = thresholds

    @property
    def thresholds_include_overhead(self):
        """Gets the thresholds_include_overhead of this QuotaQuotaCreateParams.  # noqa: E501

        If true, thresholds apply to data plus filesystem overhead required to store the data (i.e. 'physical' usage).  # noqa: E501

        :return: The thresholds_include_overhead of this QuotaQuotaCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._thresholds_include_overhead

    @thresholds_include_overhead.setter
    def thresholds_include_overhead(self, thresholds_include_overhead):
        """Sets the thresholds_include_overhead of this QuotaQuotaCreateParams.

        If true, thresholds apply to data plus filesystem overhead required to store the data (i.e. 'physical' usage).  # noqa: E501

        :param thresholds_include_overhead: The thresholds_include_overhead of this QuotaQuotaCreateParams.  # noqa: E501
        :type: bool
        """
        if thresholds_include_overhead is None:
            raise ValueError("Invalid value for `thresholds_include_overhead`, must not be `None`")  # noqa: E501

        self._thresholds_include_overhead = thresholds_include_overhead

    @property
    def type(self):
        """Gets the type of this QuotaQuotaCreateParams.  # noqa: E501

        The type of quota.  # noqa: E501

        :return: The type of this QuotaQuotaCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QuotaQuotaCreateParams.

        The type of quota.  # noqa: E501

        :param type: The type of this QuotaQuotaCreateParams.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["directory", "user", "group", "default-user", "default-group"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, QuotaQuotaCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
