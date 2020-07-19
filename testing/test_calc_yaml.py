#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
import yaml

from pythoncode.calc import Calculator

cal = Calculator()
def get_testDatas():
    with open(file="./datas/testDatas.yaml", mode="r") as f:
        testDatas = yaml.safe_load(f)
        print(type(testDatas))
        print(testDatas)
        return testDatas

def get_steps():
    with open(file="./datas/steps.yaml", mode="r") as f:
        add_datas = []
        div_datas = []
        stepDatas = yaml.safe_load(f)
        testDatas = get_testDatas()
        for step in stepDatas:
            if step == "add":
                for key in testDatas.keys():
                    if key[:3] == step:
                        add_datas.append(testDatas[key])
            elif step == "div":
                for key in testDatas.keys():
                    if key[:3] == step:
                        div_datas.append(testDatas[key])
        return add_datas, div_datas


class TestCal_1:
    add_datas, div_datas = get_steps()
    print("====add_datas====")
    print(add_datas)
    print("====div_datas====")
    print(div_datas)

    @pytest.mark.parametrize('a, b, result', add_datas)
    def test_add(self,a, b, result):
        print("==test_add==")
        print(a)
        print(b)
        print(result)
        assert result == cal.add(a, b)

    @pytest.mark.parametrize('a, b, result', div_datas)
    def test_div(self, a, b, result):
        print("==test_div==")
        print(a)
        print(b)
        print(result)
        assert result == cal.div(a, b)
