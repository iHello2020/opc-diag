# -*- coding: utf-8 -*-
#
# phys_pkg.py
#
# Copyright (C) 2013 Steve Canny scanny@cisco.com
#
# This module is part of opc-diag and is released under the MIT License:
# http://www.opensource.org/licenses/mit-license.php

"""Interface to a physical OPC package, either a zip archive or directory"""


class PhysPkg(object):
    """
    Provides read and write services for packages on the filesystem. Suitable
    for use with OPC packages in either Zip or expanded directory form.
    |PhysPkg| objects are iterable, generating a (uri, blob) 2-tuple for each
    item in the package.
    """
    def __init__(self, blobs, root_uri):
        super(PhysPkg, self).__init__()
        self._blobs = blobs
        self._root_uri = root_uri

    def __iter__(self):
        """
        Generate a (uri, blob) 2-tuple for each of the items in the package.
        """

    @staticmethod
    def read(path):
        """
        Return a |PhysPkg| instance loaded with contents of OPC package at
        *path*, where *path* can be either a regular zip package or a
        directory containing an expanded package.
        """

    @property
    def root_uri(self):
        return self._root_uri  # pragma: no cover