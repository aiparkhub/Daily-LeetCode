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
# @Program : 安装脚本 | Installation script
# @File : setup.py
# @Description : 定义 安装脚本 | Define the installation script
# @Copyright © 2019 - 2020 AIParkHub-Group. All rights reserved.


# 导入 第三方模块 | Import third-party modules
from setuptools import find_packages, setup

setup(
    name='daily_leetcode',
    version='0.2.5',
    description="LeetCode of the Day | Enhanced Algorithmic Ideas",
    long_description=readme + '\n\n' + history,
    platforms=["Linux", "MacOS"],
    author="jeep711",
    author_email='jeep-711@outlook.com',
    url='https://github.com/aiparkhub/Daily-LeetCode',
    packages=[
        'daily_leetcode',
    ],
    # packages=find_packages()
    package_dir={'daily_leetcode': 'daily_leetcode'},
    license="MIT license",
    zip_safe=False,
    keywords='daily_leetcode',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
