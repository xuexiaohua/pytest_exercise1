#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
# 函数级的setup\teardown

def setup_function():
    print("开始计算")

def teardown_function():
    print("计算结束")

@pytest.fixture()
def forward():
    yield setup_function()
    teardown_function()