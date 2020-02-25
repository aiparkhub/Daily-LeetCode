# -*- coding:utf-8 -*-
#
# Geek International Park | 极客国际公园 & GeekParkHub | 极客实验室
# Website | https://www.geekparkhub.com
# Description | Open · Creation |
# Open Source Open Achievement Dream, GeekParkHub Co-construction has never been seen before.
#
# HackerParkHub | 黑客公园
# Website | https://www.hackerparkhub.org
# Description | In the spirit of fearless exploration, create unknown technology and worship of technology.
#
# AIParkHub | 人工智能公园
# Website | https://github.com/aiparkhub
# Description | Embark on the wave of AI and push the limits of machine intelligence.
#
# @GeekDeveloper : JEEP-711
# @Author : system
# @Version : 0.2.5
# @Program : 定义 数组示例 | Definition array example
# @File : array_example.py
# @Description : 实现支持动态扩容, 动态增删改的数组操作
# Implementation of array operations that support dynamic expansion, dynamic addition, deletion, and modification
# @Copyright © 2019 - 2020 AIParkHub-Organization. All rights reserved.


class ArrayExample:
    """
    A simple wrapper around List, You cannot have -1 in the array
    Assumes int for element type, Insertion & deletion & random access of array
    """

    def __init__(self, capacity: int):
        """
        定义 初始化 方法 | Definition initialization method
        :param capacity:
        """
        self._data = []
        self._capacity = capacity

    def __getitem__(self, position: int) -> object:
        return self._data[position]

    def __setitem__(self, index: int, value: object):
        self._data[index] = value

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item

    def find(self, index: int) -> object:
        """
        定义 查询数组 方法 | Definition query array method
        :param index:
        :return:
        """

        try:
            return self._data[index]
        except IndexError:
            return None

    def delete(self, index: int) -> bool:
        """
        定义 删除数组 方法 | Definition delete array method
        :param index:
        :return:
        """

        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False

    def insert(self, index: int, value: int) -> bool:
        """
        定义 插入数组 方法 | Define insert array method
        :param index:
        :param value:
        :return:
        """

        if len(self) >= self._capacity:
            return False
        else:
            return self._data.insert(index, value)

    def print_all(self):
        """
        定义 打印数组 方法 | Define print array method
        :return:
        """

        for item in self:
            print(item)


def test_array():
    """
    定义 测试函数 | Definition test function
    :return:
    """

    array = ArrayExample(5)  # 创建对象实例 | Create object instance
    # 对象实例 调用方法 | Object instance call method
    array.insert(0, 3)
    array.insert(0, 4)
    array.insert(1, 5)
    array.insert(3, 9)
    array.insert(3, 10)
    assert array.insert(0, 100) is False
    assert len(array) == 5
    assert array.find(1) == 5
    assert array.delete(4) is True
    array.print_all()


# 定义 主模块 | Definition Main module
if __name__ == "__main__":
    # 调用函数 | Call Function
    test_array()
