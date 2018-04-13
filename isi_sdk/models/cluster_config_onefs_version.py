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


class ClusterConfigOnefsVersion(object):
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
        'build': 'str',
        'copyright': 'str',
        'reldate': 'int',
        'release': 'str',
        'revision': 'str',
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'build': 'build',
        'copyright': 'copyright',
        'reldate': 'reldate',
        'release': 'release',
        'revision': 'revision',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, build=None, copyright=None, reldate=None, release=None, revision=None, type=None, version=None):  # noqa: E501
        """ClusterConfigOnefsVersion - a model defined in Swagger"""  # noqa: E501

        self._build = None
        self._copyright = None
        self._reldate = None
        self._release = None
        self._revision = None
        self._type = None
        self._version = None
        self.discriminator = None

        self.build = build
        self.copyright = copyright
        self.reldate = reldate
        self.release = release
        self.revision = revision
        self.type = type
        self.version = version

    @property
    def build(self):
        """Gets the build of this ClusterConfigOnefsVersion.  # noqa: E501

        OneFS build string.  # noqa: E501

        :return: The build of this ClusterConfigOnefsVersion.  # noqa: E501
        :rtype: str
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this ClusterConfigOnefsVersion.

        OneFS build string.  # noqa: E501

        :param build: The build of this ClusterConfigOnefsVersion.  # noqa: E501
        :type: str
        """
        if build is None:
            raise ValueError("Invalid value for `build`, must not be `None`")  # noqa: E501

        self._build = build

    @property
    def copyright(self):
        """Gets the copyright of this ClusterConfigOnefsVersion.  # noqa: E501

        Cluster copyright information.  # noqa: E501

        :return: The copyright of this ClusterConfigOnefsVersion.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this ClusterConfigOnefsVersion.

        Cluster copyright information.  # noqa: E501

        :param copyright: The copyright of this ClusterConfigOnefsVersion.  # noqa: E501
        :type: str
        """
        if copyright is None:
            raise ValueError("Invalid value for `copyright`, must not be `None`")  # noqa: E501

        self._copyright = copyright

    @property
    def reldate(self):
        """Gets the reldate of this ClusterConfigOnefsVersion.  # noqa: E501

        Timestamp of release date.  # noqa: E501

        :return: The reldate of this ClusterConfigOnefsVersion.  # noqa: E501
        :rtype: int
        """
        return self._reldate

    @reldate.setter
    def reldate(self, reldate):
        """Sets the reldate of this ClusterConfigOnefsVersion.

        Timestamp of release date.  # noqa: E501

        :param reldate: The reldate of this ClusterConfigOnefsVersion.  # noqa: E501
        :type: int
        """
        if reldate is None:
            raise ValueError("Invalid value for `reldate`, must not be `None`")  # noqa: E501

        self._reldate = reldate

    @property
    def release(self):
        """Gets the release of this ClusterConfigOnefsVersion.  # noqa: E501

        Kernel release number.  # noqa: E501

        :return: The release of this ClusterConfigOnefsVersion.  # noqa: E501
        :rtype: str
        """
        return self._release

    @release.setter
    def release(self, release):
        """Sets the release of this ClusterConfigOnefsVersion.

        Kernel release number.  # noqa: E501

        :param release: The release of this ClusterConfigOnefsVersion.  # noqa: E501
        :type: str
        """
        if release is None:
            raise ValueError("Invalid value for `release`, must not be `None`")  # noqa: E501

        self._release = release

    @property
    def revision(self):
        """Gets the revision of this ClusterConfigOnefsVersion.  # noqa: E501

        OneFS build number.  # noqa: E501

        :return: The revision of this ClusterConfigOnefsVersion.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this ClusterConfigOnefsVersion.

        OneFS build number.  # noqa: E501

        :param revision: The revision of this ClusterConfigOnefsVersion.  # noqa: E501
        :type: str
        """
        if revision is None:
            raise ValueError("Invalid value for `revision`, must not be `None`")  # noqa: E501

        self._revision = revision

    @property
    def type(self):
        """Gets the type of this ClusterConfigOnefsVersion.  # noqa: E501

        Kernel release type.  # noqa: E501

        :return: The type of this ClusterConfigOnefsVersion.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ClusterConfigOnefsVersion.

        Kernel release type.  # noqa: E501

        :param type: The type of this ClusterConfigOnefsVersion.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def version(self):
        """Gets the version of this ClusterConfigOnefsVersion.  # noqa: E501

        Kernel full version information.  # noqa: E501

        :return: The version of this ClusterConfigOnefsVersion.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ClusterConfigOnefsVersion.

        Kernel full version information.  # noqa: E501

        :param version: The version of this ClusterConfigOnefsVersion.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

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
        if not isinstance(other, ClusterConfigOnefsVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
