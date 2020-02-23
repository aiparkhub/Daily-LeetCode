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
# @Program : 定义 链表 lru缓存 示例 | Definition LinkList lru cache example
# @File : linked_list_lru_cache_example.py
# @Description : 定义 链表示例 | Definition LinkList example
# @Copyright © 2019 - 2020 AIParkHub-Group. All rights reserved.


"""
<Description>
👨🏼‍💻Daily Leet Code : 146👨🏼‍💻
    运用你所掌握的数据结构并设计实现一个LRU(最近最少使用)的缓存机制;
    该缓存机制应该支持以下操作: 获取数据`get`和写入数据`put`;
    获取数据get(key): 如果密钥 (key)存在于缓存中, 则获取密钥的值(总是正数), 否则返回 -1
    写入数据put(key, value): 如果密钥不存在则写入其数据值;
    当缓存容量达到上限时, 它应该在写入新数据之前删除最近最少使用的数据值, 从而为新的数据值留出空间;
</Description>

<Coding ideas> 哈希表 + 双向链表 | 哈希表: 查询 0(1), 双向链表: 有序, 增删操作 0(1) </Coding ideas>
"""


class SingleListNode(object):
    """
    定义 单向链表 | Definition One-way linked list
    """

    def __init__(self, x, y):
        """
        定义 初始化 方法 | Definition initialization method
        :param x:
        :param y:
        """
        self.key = x
        self.val = y
        self.next = None
        self.prev = None


class LRUCache:
    """
    定义 LRU缓存类 | Define LRU cache class
    """

    def __init__(self, capacity: int):
        """
        定义 初始化 方法 | Definition initialization method
        :param capacity: 容量
        """
        self.cap = capacity
        self.hkeys = {}
        # 定义 `top` & `tail` 用于限定节点边界 | Define `top` & `tail` Used to define
        # node boundaries
        self.top = SingleListNode(None, -1)
        self.tail = SingleListNode(None, -1)
        self.top.next = self.tail
        self.tail.prev = self.top

    def get_value(self, key: int) -> int:
        """
        定义 获取数值 方法 | Definition get value method
        :param key:
        :return:
        """

        if key in self.hkeys.keys():
            cur = self.hkeys[key]  # 更新节点顺序
            cur.next.prev = cur.prev  # 跳出原位置
            cur.prev.next = cur.next
            top_node = self.top.next  # 最近使用过的数据值将置于链表首部
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur
            return self.hkeys[key].val
        return -1

    def put_value(self, key: int, value: int) -> None:
        """
        定义 添加 数值方法 | Definition Add Numerical Method
        :param key:
        :param value:
        :return:
        """

        if key in self.hkeys.keys():
            cur = self.hkeys[key]
            cur.val = value
            cur.prev.next = cur.next  # 跳出原位置
            cur.next.prev = cur.prev
            top_node = self.top.next  # 最近使用过的数据值将置于链表首部
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur
        else:
            cur = SingleListNode(key, value)  # 增加新节点至首部
            self.hkeys[key] = cur
            top_node = self.top.next  # 最近使用过的数据值将置于链表首部
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur
            if len(self.hkeys.keys()) > self.cap:
                self.hkeys.pop(self.tail.prev.key)
                self.tail.prev.prev.next = self.tail  # 去除原尾节点
                self.tail.prev = self.tail.prev.prev

    def __repr__(self):
        """
        覆写 输出格式 特殊方法 | Overwrite output format Special method
        :return:
        """
        overwrite_values = []
        p = self.top.next
        while p.next:
            overwrite_values.append(str(p.val))
            p = p.next
        return ' -> '.join(overwrite_values)


# 定义 主模块 | Definition Main module
if __name__ == "__main__":
    # 创建对象实例 | Create object instance
    data_cache = LRUCache(2)

    # 对象实例 调用方法 | Object instance call method
    data_cache.put_value(1, 1)
    data_cache.put_value(2, 2)
    print('data_cache.put_value =>', data_cache)

    data_cache.get_value(1)  # Return result = 1
    data_cache.put_value(3, 3)  # This operation will invalidate key 2
    print('data_cache.put_value(3, 3) =>', data_cache)

    data_cache.get_value(2)  # Return result = -1 (Not found)
    data_cache.put_value(4, 4)  # This will invalidate key 1
    print('data_cache.put_value(4, 4) => ', data_cache)

    data_cache.get_value(1)  # Return result = -1 (Not found)
    data_cache.get_value(3)  # Return result = 3
    print('data_cache.get_value(3) => ', data_cache)

    data_cache.get_value(4)  # Return result = 4
    print('data_cache.get_value(4) =>', data_cache)
