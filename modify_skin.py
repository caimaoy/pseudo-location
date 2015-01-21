# -*- coding: UTF-8 -*-

'''
Last modified time: 2015-01-21 09:59:38
Edit time: 2015-01-21 10:00:44
File name: modify_skin.py
Edit by caimaoy
'''

__author__ = 'caimaoy'

import codecs
import re
import os


def _rpl(s='@'):
    """返回re.sub的回调函数，前面添加字符串s

    :s: 添加的字符串s
    :returns: re.sub的回调函数

    """
    def _foo(match):
        m = match.group(1)
        if m == "":
            ret = match.group()
        else:
            ret = match.group().replace(m, s + m)
        return ret
    return _foo


def __modify_skin(file_path, s='@'):
    """修改替换file_path中的文件值

    :file_path: 需要替换的文件
    :s: 添加的字符串
    :returns: None

    """
    o = []
    reg = re.compile(r'value="(.*)"')
    with codecs.open(file_path, 'r', 'utf-8') as f:
        for i in f:
            i_rpl = reg.sub(_rpl(s), i)
            o.append(i_rpl)
    with codecs.open(file_path, 'w', 'utf-8') as f:
        for i in o:
            f.writelines(i)


def __scan_file(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            if name == 'skin.xml':
                f = os.path.join(root, name)
                print f
                __modify_skin(f, '@')


if __name__ == '__main__':
    __scan_file(r'C:\Program Files\Baidu Security\Baidu Antivirus\i18n')
