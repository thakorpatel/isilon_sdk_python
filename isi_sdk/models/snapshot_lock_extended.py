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


class SnapshotLockExtended(object):
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
        'comment': 'str',
        'count': 'int',
        'expires': 'int',
        'id': 'int'
    }

    attribute_map = {
        'comment': 'comment',
        'count': 'count',
        'expires': 'expires',
        'id': 'id'
    }

    def __init__(self, comment=None, count=None, expires=None, id=None):  # noqa: E501
        """SnapshotLockExtended - a model defined in Swagger"""  # noqa: E501

        self._comment = None
        self._count = None
        self._expires = None
        self._id = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if count is not None:
            self.count = count
        if expires is not None:
            self.expires = expires
        if id is not None:
            self.id = id

    @property
    def comment(self):
        """Gets the comment of this SnapshotLockExtended.  # noqa: E501

        User supplied lock comment.  # noqa: E501

        :return: The comment of this SnapshotLockExtended.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this SnapshotLockExtended.

        User supplied lock comment.  # noqa: E501

        :param comment: The comment of this SnapshotLockExtended.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def count(self):
        """Gets the count of this SnapshotLockExtended.  # noqa: E501

        Recursive lock count.  # noqa: E501

        :return: The count of this SnapshotLockExtended.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this SnapshotLockExtended.

        Recursive lock count.  # noqa: E501

        :param count: The count of this SnapshotLockExtended.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def expires(self):
        """Gets the expires of this SnapshotLockExtended.  # noqa: E501

        The Unix Epoch time the snapshot lock will expire and be eligible for automatic deletion.  # noqa: E501

        :return: The expires of this SnapshotLockExtended.  # noqa: E501
        :rtype: int
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this SnapshotLockExtended.

        The Unix Epoch time the snapshot lock will expire and be eligible for automatic deletion.  # noqa: E501

        :param expires: The expires of this SnapshotLockExtended.  # noqa: E501
        :type: int
        """

        self._expires = expires

    @property
    def id(self):
        """Gets the id of this SnapshotLockExtended.  # noqa: E501

        System generated lock ID.  # noqa: E501

        :return: The id of this SnapshotLockExtended.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SnapshotLockExtended.

        System generated lock ID.  # noqa: E501

        :param id: The id of this SnapshotLockExtended.  # noqa: E501
        :type: int
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
        if not isinstance(other, SnapshotLockExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
