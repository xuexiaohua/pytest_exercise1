#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 测试文件

import sys
import pytest



sys.path.append('..')
from pythoncode.calc import Calculator

class TestCalc:
    @pytest.mark.parametrize('a', [2, 0.2, 0, -0.2, -2])
    @pytest.mark.parametrize('b', [2, 0.2, 0, -0.2, -2])
    def test_add(self, a, b, forward):
        cal = Calculator()
        assert a + b == cal.add(a, b)

    @pytest.mark.parametrize('a', [2, 0.2, 0, -0.2, -2])
    @pytest.mark.parametrize('b', [2, 0.2, 0, -0.2, -2])
    def test_sub(self, a, b, forward):
        cal = Calculator()
        assert a - b == cal.sub(a, b)

    @pytest.mark.parametrize('a', [2, 0.2, 0, -0.2, -2])
    @pytest.mark.parametrize('b', [2, 0.2, 0, -0.2, -2])
    def test_multi(self, a, b, forward):
        cal = Calculator()
        assert a * b == cal.multi(a, b)

    @pytest.mark.parametrize('a', [2, 0.2, 0, -0.2, -2])
    @pytest.mark.parametrize('b', [2, 0.2, 0, -0.2, -2])
    def test_div(self, a, b, forward):
        cal = Calculator()
        assert a / b == cal.div(a, b)


if __name__ == '__main__':
    pytest.main()
