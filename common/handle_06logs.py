# 封装日志模块

import os
import logging

from common.handle_01path import LOGDIR
from common.handle_03config import conf


class HandleLog(object):

    @staticmethod
    def create_logger():
        mylog = logging.getLogger(conf.get("log", "name"))  # 日志收集器对象
        mylog.setLevel(conf.get("log", "level"))            # 设置日志等级

        sh = logging.StreamHandler()                  # 日志输出渠道--》控制台
        sh.setLevel(conf.get("log", "sh_level"))
        mylog.addHandler(sh)

        # fh = logging.FileHandler(filename="log.log", encoding="utf8")   # 日志输出渠道-->在当前文件包下生成文件
        fh = logging.FileHandler(filename=os.path.join(LOGDIR, "log.log"), encoding="utf8")   # 日志输出渠道--》日志文件
        fh.setLevel(conf.get("log", "fh_level"))
        mylog.addHandler(fh)

        format = "%(asctime)s-[%(filename)s-->line:%(lineno)d]-%(levelname)s-%(message)s"
        fm = logging.Formatter(format)

        sh.setFormatter(fm)  # 输出格式和渠道进行绑定
        fh.setFormatter(fm)
        return mylog

log = HandleLog.create_logger()   # 通过类调用类属性， 可获取到属性值








