#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import random
import sys

def print_result():
    print u"请输入到场观众总数，按Enter结束输入："
    num = input()
    while num == 0 or num < 0:
        print u"输入不合法，请重新输入："
        num = input()
    result = random.randint(1, int(num))
    print u"获奖观众编号为：" + str(result)

if __name__ == '__main__':
    print u"西安交通大学兵马俑BBS二十周年站庆晚会抽奖程序"
    print u"*****************一镜未剪0.01版******************"
    print "**************************************************"
    print_result()
    print u"是否继续抽奖？继续请按Y，结束请按N："
    key = raw_input()
    while key == "Y" or key == "y":
        print_result()
        print u"是否继续抽奖？继续请按Y，结束请按N："
        key = raw_input()
    if key == "N" or key == "n":
        sys.exit(0)