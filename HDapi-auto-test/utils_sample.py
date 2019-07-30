# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 17:03
# @Author  : lizhipeng
# @Email   : lizhipeng@luojilab.com
# @File    : util.py
# @Software: PyCharm Community Edition



import os
import sys
import platform

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 17:03
# @Author  : lizhipeng
# @Email   : lizhipeng@luojilab.com
# @File    : util.py
# @Software: PyCharm Community Edition

import os
import sys
import platform

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

sys.path.insert(0, BASE_DIR)

# 路径
IMG_DIR = os.path.join(BASE_DIR, '/img')
TEST_DIR = os.path.join(BASE_DIR, '/src/test/cases')
LOGFILE_DIR = os.path.join(BASE_DIR, '/log')
ConfigParser_PATH = os.path.join(BASE_DIR, '/config/ConfigParser.ini')
Excel_PATH = os.path.join(BASE_DIR, '/zhishen/Excel')

# url
BASE_URL = 'http://122.112.18.6:30002'
LOGIN_URL = BASE_URL + '/users/sign_in'
DOSSIERS_URL = BASE_URL + '/smt#/court_cases/{0}/dossier_thumbs'
EBOOK_URL = BASE_URL + '/smt#/court_cases/degital/{0}.html'
COMPOSITIONS_URL = BASE_URL + '/smt#/compositions/{0}.html/templates.html'
CASE_INFO_URL = BASE_URL + '/court_cases/{0}/baseinfo?format=json'

# 系统相关配置
ENV_INFO = {
    'os_name': '{0} {1}'.format(platform.system(), platform.release()),
    'browser': 'chrome'
    }

# 报告相关配置
REPORT_INFO = {
    'title': '- 智能辅助办案系统测试报告',
    }

# 邮件相关配置
EMAIL_INFO = {
    'smtp_server': 'smtp.sina.com',
    'subject': '自动化测试报告',
    'user': 'user@email',
    'password': 'password',
    'sender': 'sender@email',
    'nick_name': 'nickname',
    'receiver': 'receiver1@email,receiver2@email',
    }




