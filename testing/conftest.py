#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
# 函数级的setup\teardown
@pytest.fixture()
def setup_function():
    print("开始计算")
@pytest.fixture()
def teardown_function():
    print("计算结束")