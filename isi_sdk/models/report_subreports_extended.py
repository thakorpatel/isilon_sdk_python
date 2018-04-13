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

from isi_sdk_8_0.models.report_subreport import ReportSubreport  # noqa: F401,E501
from isi_sdk_8_0.models.report_subreports import ReportSubreports  # noqa: F401,E501


class ReportSubreportsExtended(object):
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
        'subreports': 'list[ReportSubreport]',
        'resume': 'str',
        'total': 'int'
    }

    attribute_map = {
        'subreports': 'subreports',
        'resume': 'resume',
        'total': 'total'
    }

    def __init__(self, subreports=None, resume=None, total=None):  # noqa: E501
        """ReportSubreportsExtended - a model defined in Swagger"""  # noqa: E501

        self._subreports = None
        self._resume = None
        self._total = None
        self.discriminator = None

        if subreports is not None:
            self.subreports = subreports
        if resume is not None:
            self.resume = resume
        if total is not None:
            self.total = total

    @property
    def subreports(self):
        """Gets the subreports of this ReportSubreportsExtended.  # noqa: E501


        :return: The subreports of this ReportSubreportsExtended.  # noqa: E501
        :rtype: list[ReportSubreport]
        """
        return self._subreports

    @subreports.setter
    def subreports(self, subreports):
        """Sets the subreports of this ReportSubreportsExtended.


        :param subreports: The subreports of this ReportSubreportsExtended.  # noqa: E501
        :type: list[ReportSubreport]
        """

        self._subreports = subreports

    @property
    def resume(self):
        """Gets the resume of this ReportSubreportsExtended.  # noqa: E501

        Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).  # noqa: E501

        :return: The resume of this ReportSubreportsExtended.  # noqa: E501
        :rtype: str
        """
        return self._resume

    @resume.setter
    def resume(self, resume):
        """Sets the resume of this ReportSubreportsExtended.

        Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).  # noqa: E501

        :param resume: The resume of this ReportSubreportsExtended.  # noqa: E501
        :type: str
        """

        self._resume = resume

    @property
    def total(self):
        """Gets the total of this ReportSubreportsExtended.  # noqa: E501

        Total number of items available.  # noqa: E501

        :return: The total of this ReportSubreportsExtended.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ReportSubreportsExtended.

        Total number of items available.  # noqa: E501

        :param total: The total of this ReportSubreportsExtended.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if not isinstance(other, ReportSubreportsExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
