# -*- coding: utf-8 -*-
#
# test_presenter.py
#
# Copyright (C) 2013 Steve Canny scanny@cisco.com
#
# This module is part of opc-diag and is released under the MIT License:
# http://www.opensource.org/licenses/mit-license.php

"""Unit tests for presenter module"""

from __future__ import unicode_literals

from opcdiag.model import PkgItem
from opcdiag.presenter import ItemPresenter

import pytest

from .unitutil import instance_mock


@pytest.fixture
def binary_part_(request):
    binary_part_ = instance_mock(PkgItem, request)
    binary_part_.is_content_types = False
    binary_part_.is_rels_item = False
    binary_part_.is_xml_part = False
    return binary_part_


@pytest.fixture
def content_types_item_(request):
    content_types_item_ = instance_mock(PkgItem, request)
    content_types_item_.is_content_types = True
    content_types_item_.is_rels_item = False
    content_types_item_.is_xml_part = False
    return content_types_item_


@pytest.fixture
def rels_item_(request):
    rels_item_ = instance_mock(PkgItem, request)
    rels_item_.is_content_types = False
    rels_item_.is_rels_item = True
    rels_item_.is_xml_part = False
    return rels_item_


@pytest.fixture
def xml_part_(request):
    xml_part_ = instance_mock(PkgItem, request)
    xml_part_.is_content_types = False
    xml_part_.is_rels_item = False
    xml_part_.is_xml_part = True
    return xml_part_


class DescribeItemPresenter(object):

    def it_constructs_subclass_based_on_item_type(
            self, content_types_item_, rels_item_, xml_part_, binary_part_):
        cases = (
            (content_types_item_, 'ContentTypesPresenter'),
            (rels_item_,          'RelsItemPresenter'),
            (xml_part_,           'XmlPartPresenter'),
            (binary_part_,        'ItemPresenter'),
        )
        for pkg_item, expected_type_name in cases:
            item_presenter = ItemPresenter(pkg_item)
            assert type(item_presenter).__name__ == expected_type_name