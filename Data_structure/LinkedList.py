#!/usr/bin/python
# -*- coding: utf-8 -*-
#@Date    :
#@Author  :
#@Link    :
#@describe:使用python代码对数据结构中链表的实现

class Node(object):
    #定义一个节点类 
    def __init__(self,elem,next_=None):
        self.elem = elem
        self.next = next_

class LinkedList(object):
    # 定义一个单节点
    def __init__(self):
        self.head = None

    
