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
from isi_sdk_8_0.models.smb_share_permission import SmbSharePermission  # noqa: F401,E501


class SmbShare(object):
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
        'access_based_enumeration': 'bool',
        'access_based_enumeration_root_only': 'bool',
        'allow_delete_readonly': 'bool',
        'allow_execute_always': 'bool',
        'allow_variable_expansion': 'bool',
        'auto_create_directory': 'bool',
        'browsable': 'bool',
        'ca_timeout': 'int',
        'ca_write_integrity': 'str',
        'change_notify': 'str',
        'create_permissions': 'str',
        'csc_policy': 'str',
        'description': 'str',
        'directory_create_mask': 'int',
        'directory_create_mode': 'int',
        'file_create_mask': 'int',
        'file_create_mode': 'int',
        'file_filter_extensions': 'list[str]',
        'file_filter_type': 'str',
        'file_filtering_enabled': 'bool',
        'hide_dot_files': 'bool',
        'host_acl': 'list[str]',
        'impersonate_guest': 'str',
        'impersonate_user': 'str',
        'inheritable_path_acl': 'bool',
        'mangle_byte_start': 'int',
        'mangle_map': 'list[str]',
        'name': 'str',
        'ntfs_acl_support': 'bool',
        'oplocks': 'bool',
        'path': 'str',
        'permissions': 'list[SmbSharePermission]',
        'run_as_root': 'list[GroupMember]',
        'strict_ca_lockout': 'bool',
        'strict_flush': 'bool',
        'strict_locking': 'bool',
        'zone': 'str'
    }

    attribute_map = {
        'access_based_enumeration': 'access_based_enumeration',
        'access_based_enumeration_root_only': 'access_based_enumeration_root_only',
        'allow_delete_readonly': 'allow_delete_readonly',
        'allow_execute_always': 'allow_execute_always',
        'allow_variable_expansion': 'allow_variable_expansion',
        'auto_create_directory': 'auto_create_directory',
        'browsable': 'browsable',
        'ca_timeout': 'ca_timeout',
        'ca_write_integrity': 'ca_write_integrity',
        'change_notify': 'change_notify',
        'create_permissions': 'create_permissions',
        'csc_policy': 'csc_policy',
        'description': 'description',
        'directory_create_mask': 'directory_create_mask',
        'directory_create_mode': 'directory_create_mode',
        'file_create_mask': 'file_create_mask',
        'file_create_mode': 'file_create_mode',
        'file_filter_extensions': 'file_filter_extensions',
        'file_filter_type': 'file_filter_type',
        'file_filtering_enabled': 'file_filtering_enabled',
        'hide_dot_files': 'hide_dot_files',
        'host_acl': 'host_acl',
        'impersonate_guest': 'impersonate_guest',
        'impersonate_user': 'impersonate_user',
        'inheritable_path_acl': 'inheritable_path_acl',
        'mangle_byte_start': 'mangle_byte_start',
        'mangle_map': 'mangle_map',
        'name': 'name',
        'ntfs_acl_support': 'ntfs_acl_support',
        'oplocks': 'oplocks',
        'path': 'path',
        'permissions': 'permissions',
        'run_as_root': 'run_as_root',
        'strict_ca_lockout': 'strict_ca_lockout',
        'strict_flush': 'strict_flush',
        'strict_locking': 'strict_locking',
        'zone': 'zone'
    }

    def __init__(self, access_based_enumeration=None, access_based_enumeration_root_only=None, allow_delete_readonly=None, allow_execute_always=None, allow_variable_expansion=None, auto_create_directory=None, browsable=None, ca_timeout=None, ca_write_integrity=None, change_notify=None, create_permissions=None, csc_policy=None, description=None, directory_create_mask=None, directory_create_mode=None, file_create_mask=None, file_create_mode=None, file_filter_extensions=None, file_filter_type=None, file_filtering_enabled=None, hide_dot_files=None, host_acl=None, impersonate_guest=None, impersonate_user=None, inheritable_path_acl=None, mangle_byte_start=None, mangle_map=None, name=None, ntfs_acl_support=None, oplocks=None, path=None, permissions=None, run_as_root=None, strict_ca_lockout=None, strict_flush=None, strict_locking=None, zone=None):  # noqa: E501
        """SmbShare - a model defined in Swagger"""  # noqa: E501

        self._access_based_enumeration = None
        self._access_based_enumeration_root_only = None
        self._allow_delete_readonly = None
        self._allow_execute_always = None
        self._allow_variable_expansion = None
        self._auto_create_directory = None
        self._browsable = None
        self._ca_timeout = None
        self._ca_write_integrity = None
        self._change_notify = None
        self._create_permissions = None
        self._csc_policy = None
        self._description = None
        self._directory_create_mask = None
        self._directory_create_mode = None
        self._file_create_mask = None
        self._file_create_mode = None
        self._file_filter_extensions = None
        self._file_filter_type = None
        self._file_filtering_enabled = None
        self._hide_dot_files = None
        self._host_acl = None
        self._impersonate_guest = None
        self._impersonate_user = None
        self._inheritable_path_acl = None
        self._mangle_byte_start = None
        self._mangle_map = None
        self._name = None
        self._ntfs_acl_support = None
        self._oplocks = None
        self._path = None
        self._permissions = None
        self._run_as_root = None
        self._strict_ca_lockout = None
        self._strict_flush = None
        self._strict_locking = None
        self._zone = None
        self.discriminator = None

        if access_based_enumeration is not None:
            self.access_based_enumeration = access_based_enumeration
        if access_based_enumeration_root_only is not None:
            self.access_based_enumeration_root_only = access_based_enumeration_root_only
        if allow_delete_readonly is not None:
            self.allow_delete_readonly = allow_delete_readonly
        if allow_execute_always is not None:
            self.allow_execute_always = allow_execute_always
        if allow_variable_expansion is not None:
            self.allow_variable_expansion = allow_variable_expansion
        if auto_create_directory is not None:
            self.auto_create_directory = auto_create_directory
        if browsable is not None:
            self.browsable = browsable
        if ca_timeout is not None:
            self.ca_timeout = ca_timeout
        if ca_write_integrity is not None:
            self.ca_write_integrity = ca_write_integrity
        if change_notify is not None:
            self.change_notify = change_notify
        if create_permissions is not None:
            self.create_permissions = create_permissions
        if csc_policy is not None:
            self.csc_policy = csc_policy
        if description is not None:
            self.description = description
        if directory_create_mask is not None:
            self.directory_create_mask = directory_create_mask
        if directory_create_mode is not None:
            self.directory_create_mode = directory_create_mode
        if file_create_mask is not None:
            self.file_create_mask = file_create_mask
        if file_create_mode is not None:
            self.file_create_mode = file_create_mode
        if file_filter_extensions is not None:
            self.file_filter_extensions = file_filter_extensions
        if file_filter_type is not None:
            self.file_filter_type = file_filter_type
        if file_filtering_enabled is not None:
            self.file_filtering_enabled = file_filtering_enabled
        if hide_dot_files is not None:
            self.hide_dot_files = hide_dot_files
        if host_acl is not None:
            self.host_acl = host_acl
        if impersonate_guest is not None:
            self.impersonate_guest = impersonate_guest
        if impersonate_user is not None:
            self.impersonate_user = impersonate_user
        if inheritable_path_acl is not None:
            self.inheritable_path_acl = inheritable_path_acl
        if mangle_byte_start is not None:
            self.mangle_byte_start = mangle_byte_start
        if mangle_map is not None:
            self.mangle_map = mangle_map
        if name is not None:
            self.name = name
        if ntfs_acl_support is not None:
            self.ntfs_acl_support = ntfs_acl_support
        if oplocks is not None:
            self.oplocks = oplocks
        if path is not None:
            self.path = path
        if permissions is not None:
            self.permissions = permissions
        if run_as_root is not None:
            self.run_as_root = run_as_root
        if strict_ca_lockout is not None:
            self.strict_ca_lockout = strict_ca_lockout
        if strict_flush is not None:
            self.strict_flush = strict_flush
        if strict_locking is not None:
            self.strict_locking = strict_locking
        if zone is not None:
            self.zone = zone

    @property
    def access_based_enumeration(self):
        """Gets the access_based_enumeration of this SmbShare.  # noqa: E501

        Only enumerate files and folders the requesting user has access to.  # noqa: E501

        :return: The access_based_enumeration of this SmbShare.  # noqa: E501
        :rtype: bool
        """
        return self._access_based_enumeration

    @access_based_enumeration.setter
    def access_based_enumeration(self, access_based_enumeration):
        """Sets the access_based_enumeration of this SmbShare.

        Only enumerate files and folders the requesting user has access to.  # noqa: E501

        :param access_based_enumeration: The access_based_enumeration of this SmbShare.  # noqa: E501
        :type: bool
        """

        self._access_based_enumeration = access_based_enumeration

    @property
    def access_based_enumeration_root_only(self):
        """Gets the access_based_enumeration_root_only of this SmbShare.  # noqa: E501

        Access-based enumeration on only the root directory of the share.  # noqa: E501

        :return: The access_based_enumeration_root_only of this SmbShare.  # noqa: E501
        :rtype: bool
        """
        return self._access_based_enumeration_root_only

    @access_based_enumeration_root_only.setter
    def access_based_enumeration_root_only(self, access_based_enumeration_root_only):
        """Sets the access_based_enumeration_root_only of this SmbShare.

        Access-based enumeration on only the root directory of the share.  # noqa: E501

        :param access_based_enumeration_root_only: The access_based_enumeration_root_only of this SmbShare.  # noqa: E501
        :type: bool
        """

        self._access_based_enumeration_root_only = access_based_enumeration_root_only

    @property
    def allow_delete_readonly(self):
        """Gets the allow_delete_readonly of this SmbShare.  # noqa: E501

        Allow deletion of read-only files in the share.  # noqa: E501

        :return: The allow_delete_readonly of this SmbShare.  # noqa: E501
        :rtype: bool
        """
        return self._allow_delete_readonly

    @allow_delete_readonly.setter
    def allow_delete_readonly(self, allow_delete_readonly):
        """Sets the allow_delete_readonly of this SmbShare.

        Allow deletion of read-only files in the share.  # noqa: E501

        :param allow_delete_readonly: The allow_delete_readonly of this SmbShare.  # noqa: E501
        :type: bool
        """

        self._allow_delete_readonly = allow_delete_readonly

    @property
    def allow_execute_always(self):
        """Gets the allow_execute_always of this SmbShare.  # noqa: E501

        Allows users to execute files they have read rights for.  # noqa: E501

        :return: The allow_execute_always of this SmbShare.  # noqa: E501
        :rtype: bool
        """
        return self._allow_execute_always

    @allow_execute_always.setter
    def allow_execute_always(self, allow_execute_always):
        """Sets the allow_execute_always of this SmbShare.

        Allows users to execute files they have read rights for.  # noqa: E501

        :param allow_execute_always: The allow_execute_always of this SmbShare.  # noqa: E501
        :type: bool
        """

        self._allow_execute_always = allow_execute_always

    @property
    def allow_variable_expansion(self):
        """Gets the allow_variable_expansion of this SmbShare.  # noqa: E501

        Allow automatic expansion of variables for home directories.  # noqa: E501

        :return: The allow_variable_expansion of this SmbShare.  # noqa: E501
        :rtype: bool
        """
        return self._allow_variable_expansion

    @allow_variable_expansion.setter
    def allow_variable_expansion(self, allow_variable_expansion):
        """Sets the allow_variable_expansion of this SmbShare.

        Allow automatic expansion of variables for home directories.  # noqa: E501

        :param allow_variable_expansion: The allow_variable_expansion of this SmbShare.  # noqa: E501
        :type: bool
        """

        self._allow_variable_expansion = allow_variable_expansion

    @property
    def auto_create_directory(self):
        """Gets the auto_create_directory of this SmbShare.  # noqa: E501

        Automatically create home directories.  # noqa: E501

        :return: The auto_create_directory of this SmbShare.  # noqa: E501
        :rtype: bool
        """
        return self._auto_create_directory

    @auto_create_directory.setter
    def auto_create_directory(self, auto_create_directory):
        """Sets the auto_create_directory of this SmbShare.

        Automatically create home directories.  # noqa: E501

        :param auto_create_directory: The auto_create_directory of this SmbShare.  # noqa: E501
        :type: bool
        """

        self._auto_create_directory = auto_create_directory

    @property
    def browsable(self):
        """Gets the browsable of this SmbShare.  # noqa: E501

        Share is visible in net view and the browse list.  # noqa: E501

        :return: The browsable of this SmbShare.  # noqa: E501
        :rtype: bool
        """
        return self._browsable

    @browsable.setter
    def browsable(self, browsable):
        """Sets the browsable of this SmbShare.

        Share is visible in net view and the browse list.  # noqa: E501

        :param browsable: The browsable of this SmbShare.  # noqa: E501
        :type: bool
        """

        self._browsable = browsable

    @property
    def ca_timeout(self):
        """Gets the ca_timeout of this SmbShare.  # noqa: E501

        Persistent open timeout for the share.  # noqa: E501

        :return: The ca_timeout of this SmbShare.  # noqa: E501
        :rtype: int
        """
        return self._ca_timeout

    @ca_timeout.setter
    def ca_timeout(self, ca_timeout):
        """Sets the ca_timeout of this SmbShare.

        Persistent open timeout for the share.  # noqa: E501

        :param ca_timeout: The ca_timeout of this SmbShare.  # noqa: E501
        :type: int
        """
        if ca_timeout is not None and ca_timeout < 2:  # noqa: E501
            raise ValueError("Invalid value for `ca_timeout`, must be a value greater than or equal to `2`")  # noqa: E501

        self._ca_timeout = ca_timeout

    @property
    def ca_write_integrity(self):
        """Gets the ca_write_integrity of this SmbShare.  # noqa: E501

        Specify the level of write-integrity on continuously available shares.  # noqa: E501

        :return: The ca_write_integrity of this SmbShare.  # noqa: E501
        :rtype: str
        """
        return self._ca_write_integrity

    @ca_write_integrity.setter
    def ca_write_integrity(self, ca_write_integrity):
        """Sets the ca_write_integrity of this SmbShare.

        Specify the level of write-integrity on continuously available shares.  # noqa: E501

        :param ca_write_integrity: The ca_write_integrity of this SmbShare.  # noqa: E501
        :type: str
        """

        self._ca_write_integrity = ca_write_integrity

    @property
    def change_notify(self):
        """Gets the change_notify of this SmbShare.  # noqa: E501

        Level of change notification alerts on the share.  # noqa: E501

        :return: The change_notify of this SmbShare.  # noqa: E501
        :rtype: str
        """
        return self._change_notify

    @change_notify.setter
    def change_notify(self, change_notify):
        """Sets the change_notify of this SmbShare.

        Level of change notification alerts on the share.  # noqa: E501

        :param change_notify: The change_notify of this SmbShare.  # noqa: E501
        :type: str
        """

        self._change_notify = change_notify

    @property
    def create_permissions(self):
        """Gets the create_permissions of this SmbShare.  # noqa: E501

        Create permissions for new files and directories in share.  # noqa: E501

        :return: The create_permissions of this SmbShare.  # noqa: E501
        :rtype: str
        """
        return self._create_permissions

    @create_permissions.setter
    def create_permissions(self, create_permissions):
        """Sets the create_permissions of this SmbShare.

        Create permissions for new files and directories in share.  # noqa: E501

        :param create_permissions: The create_permissions of this SmbShare.  # noqa: E501
        :type: str
        """

        self._create_permissions = create_permissions

    @property
    def csc_policy(self):
        """Gets the csc_policy of this SmbShare.  # noqa: E501

        Client-side caching policy for the shares.  # noqa: E501

        :return: The csc_policy of this SmbShare.  # noqa: E501
        :rtype: str
        """
        return self._csc_policy

    @csc_policy.setter
    def csc_policy(self, csc_policy):
        """Sets the csc_policy of this SmbShare.

        Client-side caching policy for the shares.  # noqa: E501

        :param csc_policy: The csc_policy of this SmbShare.  # noqa: E501
        :type: str
        """

        self._csc_policy = csc_policy

    @property
    def description(self):
        """Gets the description of this SmbShare.  # noqa: E501

        Description for this SMB share.  # noqa: E501

        :return: The description of this SmbShare.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SmbShare.

        Description for this SMB share.  # noqa: E501

        :param description: The description of this SmbShare.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def directory_create_mask(self):
        """Gets the directory_create_mask of this SmbShare.  # noqa: E501

        Directory create mask bits.  # noqa: E501

        :return: The directory_create_mask of this SmbShare.  # noqa: E501
        :rtype: int
        """
        return self._directory_create_mask

    @directory_create_mask.setter
    def directory_create_mask(self, directory_create_mask):
        """Sets the directory_create_mask of this SmbShare.

        Directory create mask bits.  # noqa: E501

        :param directory_create_mask: The directory_create_mask of this SmbShare.  # noqa: E501
        :type: int
        """

        self._directory_create_mask = directory_create_mask

    @property
    def directory_create_mode(self):
        """Gets the directory_create_mode of this SmbShare.  # noqa: E501

        Directory create mode bits.  # noqa: E501

        :return: The directory_create_mode of this SmbShare.  # noqa: E501
        :rtype: int
        """
        return self._directory_create_mode

    @directory_create_mode.setter
    def directory_create_mode(self, directory_create_mode):
        """Sets the directory_create_mode of this SmbShare.

        Directory create mode bits.  # noqa: E501

        :param directory_create_mode: The directory_create_mode of this SmbShare.  # noqa: E501
        :type: int
        """

        self._directory_create_mode = directory_create_mode

    @property
    def file_create_mask(self):
        """Gets the file_create_mask of this SmbShare.  # noqa: E501

        File create mask bits.  # noqa: E501

        :return: The file_create_mask of this SmbShare.  # noqa: E501
        :rtype: int
        """
        return self._file_create_mask

    @file_create_mask.setter
    def file_create_mask(self, file_create_mask):
        """Sets the file_create_mask of this SmbShare.

        File create mask bits.  # noqa: E501

        :param file_create_mask: The file_create_mask of this SmbShare.  # noqa: E501
        :type: int
        """

        self._file_create_mask = file_create_mask

    @property
    def file_create_mode(self):
        """Gets the file_create_mode of this SmbShare.  # noqa: E501

        File create mode bits.  # noqa: E501

        :return: The file_create_mode of this SmbShare.  # noqa: E501
        :rtype: int
        """
        return self._file_create_mode

    @file_create_mode.setter
    def file_create_mode(self, file_create_mode):
        """Sets the file_create_mode of this SmbShare.

        File create mode bits.  # noqa: E501

        :param file_create_mode: The file_create_mode of this SmbShare.  # noqa: E501
        :type: int
        """

        self._file_create_mode = file_create_mode

    @property
    def file_filter_extensions(self):
        """Gets the file_filter_extensions of this SmbShare.  # noqa: E501

        Specifies the list of file extensions.  # noqa: E501

        :return: The file_filter_extensions of this SmbShare.  # noqa: E501
        :rtype: list[str]
        """
        return self._file_filter_extensions

    @file_filter_extensions.setter
    def file_filter_extensions(self, file_filter_extensions):
        """Sets the file_filter_extensions of this SmbShare.

        Specifies the list of file extensions.  # noqa: E501

        :param file_filter_extensions: The file_filter_extensions of this SmbShare.  # noqa: E501
        :type: list[str]
        """

        self._file_filter_extensions = file_filter_extensions

    @property
    def file_filter_type(self):
        """Gets the file_filter_type of this SmbShare.  # noqa: E501

        Specifies if filter list is for deny or allow. Default is deny.  # noqa: E501

        :return: The file_filter_type of this SmbShare.  # noqa: E501
        :rtype: str
        """
        return self._file_filter_type

    @file_filter_type.setter
    def file_filter_type(self, file_filter_type):
        """Sets the file_filter_type of this SmbShare.

        Specifies if filter list is for deny or allow. Default is deny.  # noqa: E501

        :param file_filter_type: The file_filter_type of this SmbShare.  # noqa: E501
        :type: str
        """

        self._file_filter_type = file_filter_type

    @property
    def file_filtering_enabled(self):
        """Gets the file_filtering_enabled of this SmbShare.  # noqa: E501

        Enables file filtering on this zone.  # noqa: E501

        :return: The file_filtering_enabled of this SmbShare.  # noqa: E501
        :rtype: bool
        """
        return self._file_filtering_enabled

    @file_filtering_enabled.setter
    def file_filtering_enabled(self, file_filtering_enabled):
        """Sets the file_filtering_enabled of this SmbShare.

        Enables file filtering on this zone.  # noqa: E501

        :param file_filtering_enabled: The file_filtering_enabled of this SmbShare.  # noqa: E501
        :type: bool
        """

        self._file_filtering_enabled = file_filtering_enabled

    @property
    def hide_dot_files(self):
        """Gets the hide_dot_files of this SmbShare.  # noqa: E501

        Hide files and directories that begin with a period '.'.  # noqa: E501

        :return: The hide_dot_files of this SmbShare.  # noqa: E501
        :rtype: bool
        """
        return self._hide_dot_files

    @hide_dot_files.setter
    def hide_dot_files(self, hide_dot_files):
        """Sets the hide_dot_files of this SmbShare.

        Hide files and directories that begin with a period '.'.  # noqa: E501

        :param hide_dot_files: The hide_dot_files of this SmbShare.  # noqa: E501
        :type: bool
        """

        self._hide_dot_files = hide_dot_files

    @property
    def host_acl(self):
        """Gets the host_acl of this SmbShare.  # noqa: E501

        An ACL expressing which hosts are allowed access. A deny clause must be the final entry.  # noqa: E501

        :return: The host_acl of this SmbShare.  # noqa: E501
        :rtype: list[str]
        """
        return self._host_acl

    @host_acl.setter
    def host_acl(self, host_acl):
        """Sets the host_acl of this SmbShare.

        An ACL expressing which hosts are allowed access. A deny clause must be the final entry.  # noqa: E501

        :param host_acl: The host_acl of this SmbShare.  # noqa: E501
        :type: list[str]
        """

        self._host_acl = host_acl

    @property
    def impersonate_guest(self):
        """Gets the impersonate_guest of this SmbShare.  # noqa: E501

        Specify the condition in which user access is done as the guest account.  # noqa: E501

        :return: The impersonate_guest of this SmbShare.  # noqa: E501
        :rtype: str
        """
        return self._impersonate_guest

    @impersonate_guest.setter
    def impersonate_guest(self, impersonate_guest):
        """Sets the impersonate_guest of this SmbShare.

        Specify the condition in which user access is done as the guest account.  # noqa: E501

        :param impersonate_guest: The impersonate_guest of this SmbShare.  # noqa: E501
        :type: str
        """

        self._impersonate_guest = impersonate_guest

    @property
    def impersonate_user(self):
        """Gets the impersonate_user of this SmbShare.  # noqa: E501

        User account to be used as guest account.  # noqa: E501

        :return: The impersonate_user of this SmbShare.  # noqa: E501
        :rtype: str
        """
        return self._impersonate_user

    @impersonate_user.setter
    def impersonate_user(self, impersonate_user):
        """Sets the impersonate_user of this SmbShare.

        User account to be used as guest account.  # noqa: E501

        :param impersonate_user: The impersonate_user of this SmbShare.  # noqa: E501
        :type: str
        """

        self._impersonate_user = impersonate_user

    @property
    def inheritable_path_acl(self):
        """Gets the inheritable_path_acl of this SmbShare.  # noqa: E501

        Set the inheritable ACL on the share path.  # noqa: E501

        :return: The inheritable_path_acl of this SmbShare.  # noqa: E501
        :rtype: bool
        """
        return self._inheritable_path_acl

    @inheritable_path_acl.setter
    def inheritable_path_acl(self, inheritable_path_acl):
        """Sets the inheritable_path_acl of this SmbShare.

        Set the inheritable ACL on the share path.  # noqa: E501

        :param inheritable_path_acl: The inheritable_path_acl of this SmbShare.  # noqa: E501
        :type: bool
        """

        self._inheritable_path_acl = inheritable_path_acl

    @property
    def mangle_byte_start(self):
        """Gets the mangle_byte_start of this SmbShare.  # noqa: E501

        Specifies the wchar_t starting point for automatic byte mangling.  # noqa: E501

        :return: The mangle_byte_start of this SmbShare.  # noqa: E501
        :rtype: int
        """
        return self._mangle_byte_start

    @mangle_byte_start.setter
    def mangle_byte_start(self, mangle_byte_start):
        """Sets the mangle_byte_start of this SmbShare.

        Specifies the wchar_t starting point for automatic byte mangling.  # noqa: E501

        :param mangle_byte_start: The mangle_byte_start of this SmbShare.  # noqa: E501
        :type: int
        """

        self._mangle_byte_start = mangle_byte_start

    @property
    def mangle_map(self):
        """Gets the mangle_map of this SmbShare.  # noqa: E501

        Character mangle map.  # noqa: E501

        :return: The mangle_map of this SmbShare.  # noqa: E501
        :rtype: list[str]
        """
        return self._mangle_map

    @mangle_map.setter
    def mangle_map(self, mangle_map):
        """Sets the mangle_map of this SmbShare.

        Character mangle map.  # noqa: E501

        :param mangle_map: The mangle_map of this SmbShare.  # noqa: E501
        :type: list[str]
        """

        self._mangle_map = mangle_map

    @property
    def name(self):
        """Gets the name of this SmbShare.  # noqa: E501

        Share name.  # noqa: E501

        :return: The name of this SmbShare.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SmbShare.

        Share name.  # noqa: E501

        :param name: The name of this SmbShare.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ntfs_acl_support(self):
        """Gets the ntfs_acl_support of this SmbShare.  # noqa: E501

        Support NTFS ACLs on files and directories.  # noqa: E501

        :return: The ntfs_acl_support of this SmbShare.  # noqa: E501
        :rtype: bool
        """
        return self._ntfs_acl_support

    @ntfs_acl_support.setter
    def ntfs_acl_support(self, ntfs_acl_support):
        """Sets the ntfs_acl_support of this SmbShare.

        Support NTFS ACLs on files and directories.  # noqa: E501

        :param ntfs_acl_support: The ntfs_acl_support of this SmbShare.  # noqa: E501
        :type: bool
        """

        self._ntfs_acl_support = ntfs_acl_support

    @property
    def oplocks(self):
        """Gets the oplocks of this SmbShare.  # noqa: E501

        Support oplocks.  # noqa: E501

        :return: The oplocks of this SmbShare.  # noqa: E501
        :rtype: bool
        """
        return self._oplocks

    @oplocks.setter
    def oplocks(self, oplocks):
        """Sets the oplocks of this SmbShare.

        Support oplocks.  # noqa: E501

        :param oplocks: The oplocks of this SmbShare.  # noqa: E501
        :type: bool
        """

        self._oplocks = oplocks

    @property
    def path(self):
        """Gets the path of this SmbShare.  # noqa: E501

        Path of share within /ifs.  # noqa: E501

        :return: The path of this SmbShare.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this SmbShare.

        Path of share within /ifs.  # noqa: E501

        :param path: The path of this SmbShare.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def permissions(self):
        """Gets the permissions of this SmbShare.  # noqa: E501

        Specifies an ordered list of permission modifications.  # noqa: E501

        :return: The permissions of this SmbShare.  # noqa: E501
        :rtype: list[SmbSharePermission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this SmbShare.

        Specifies an ordered list of permission modifications.  # noqa: E501

        :param permissions: The permissions of this SmbShare.  # noqa: E501
        :type: list[SmbSharePermission]
        """

        self._permissions = permissions

    @property
    def run_as_root(self):
        """Gets the run_as_root of this SmbShare.  # noqa: E501

        Allow account to run as root.  # noqa: E501

        :return: The run_as_root of this SmbShare.  # noqa: E501
        :rtype: list[GroupMember]
        """
        return self._run_as_root

    @run_as_root.setter
    def run_as_root(self, run_as_root):
        """Sets the run_as_root of this SmbShare.

        Allow account to run as root.  # noqa: E501

        :param run_as_root: The run_as_root of this SmbShare.  # noqa: E501
        :type: list[GroupMember]
        """

        self._run_as_root = run_as_root

    @property
    def strict_ca_lockout(self):
        """Gets the strict_ca_lockout of this SmbShare.  # noqa: E501

        Specifies if persistent opens would do strict lockout on the share.  # noqa: E501

        :return: The strict_ca_lockout of this SmbShare.  # noqa: E501
        :rtype: bool
        """
        return self._strict_ca_lockout

    @strict_ca_lockout.setter
    def strict_ca_lockout(self, strict_ca_lockout):
        """Sets the strict_ca_lockout of this SmbShare.

        Specifies if persistent opens would do strict lockout on the share.  # noqa: E501

        :param strict_ca_lockout: The strict_ca_lockout of this SmbShare.  # noqa: E501
        :type: bool
        """

        self._strict_ca_lockout = strict_ca_lockout

    @property
    def strict_flush(self):
        """Gets the strict_flush of this SmbShare.  # noqa: E501

        Handle SMB flush operations.  # noqa: E501

        :return: The strict_flush of this SmbShare.  # noqa: E501
        :rtype: bool
        """
        return self._strict_flush

    @strict_flush.setter
    def strict_flush(self, strict_flush):
        """Sets the strict_flush of this SmbShare.

        Handle SMB flush operations.  # noqa: E501

        :param strict_flush: The strict_flush of this SmbShare.  # noqa: E501
        :type: bool
        """

        self._strict_flush = strict_flush

    @property
    def strict_locking(self):
        """Gets the strict_locking of this SmbShare.  # noqa: E501

        Specifies whether byte range locks contend against SMB I/O.  # noqa: E501

        :return: The strict_locking of this SmbShare.  # noqa: E501
        :rtype: bool
        """
        return self._strict_locking

    @strict_locking.setter
    def strict_locking(self, strict_locking):
        """Sets the strict_locking of this SmbShare.

        Specifies whether byte range locks contend against SMB I/O.  # noqa: E501

        :param strict_locking: The strict_locking of this SmbShare.  # noqa: E501
        :type: bool
        """

        self._strict_locking = strict_locking

    @property
    def zone(self):
        """Gets the zone of this SmbShare.  # noqa: E501

        Name of the access zone to which to move this SMB share  # noqa: E501

        :return: The zone of this SmbShare.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this SmbShare.

        Name of the access zone to which to move this SMB share  # noqa: E501

        :param zone: The zone of this SmbShare.  # noqa: E501
        :type: str
        """

        self._zone = zone

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
        if not isinstance(other, SmbShare):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
