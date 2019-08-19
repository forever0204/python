#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging

def do_try():
    try:
        num = input('Please input:')
        num = float(num)
        result = div(num)
    except ZeroDivisionError as e:
        print('被除数不可为0！')
        print(e)
    except ValueError as e:
        print('输入的值必须为数字！')
        print(e)
    except BaseException as e:
        print('发生错误！')
        print(e)
    else:
        print('100 /', num, '=', result)
    finally:
        print('Try End')

    #raise OverflowError('发生溢出错误！')

def div(num):
    return 100 / num

def main():
    try:
        do_try()
    except OverflowError as e:
        print(e)
        logging.exception(e)
    finally:
        print('Main End')

main()