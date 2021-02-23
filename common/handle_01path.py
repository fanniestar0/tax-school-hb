# 封装路径信息
import os
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFDIR = os.path.join(BASEDIR, "conf")
DATADIR = os.path.join(BASEDIR, "datas")
LOGDIR = os.path.join(BASEDIR, "logs")
REPORTDIR = os.path.join(BASEDIR, "reports")
CASEDIR = os.path.join(BASEDIR, "testcases")
