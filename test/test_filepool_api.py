# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 3
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import isi_sdk_8_0
from isi_sdk_8_0.api.filepool_api import FilepoolApi  # noqa: E501
from isi_sdk_8_0.rest import ApiException


class TestFilepoolApi(unittest.TestCase):
    """FilepoolApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_0.api.filepool_api.FilepoolApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_filepool_policy(self):
        """Test case for create_filepool_policy

        """
        pass

    def test_delete_filepool_policy(self):
        """Test case for delete_filepool_policy

        """
        pass

    def test_get_filepool_default_policy(self):
        """Test case for get_filepool_default_policy

        """
        pass

    def test_get_filepool_policy(self):
        """Test case for get_filepool_policy

        """
        pass

    def test_get_filepool_template(self):
        """Test case for get_filepool_template

        """
        pass

    def test_get_filepool_templates(self):
        """Test case for get_filepool_templates

        """
        pass

    def test_list_filepool_policies(self):
        """Test case for list_filepool_policies

        """
        pass

    def test_update_filepool_default_policy(self):
        """Test case for update_filepool_default_policy

        """
        pass

    def test_update_filepool_policy(self):
        """Test case for update_filepool_policy

        """
        pass


if __name__ == '__main__':
    unittest.main()
