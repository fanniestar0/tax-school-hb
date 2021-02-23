# 封装读取配置文件数据
import os
from configparser import ConfigParser
from common.handle_01path import CONFDIR

class HandleConfig(ConfigParser):

    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.read(filename, encoding="utf8")

    # def write_data(self,section, options, value):
    #     self.set(section, options, value)
    #     self.write(fp = open(self.filename, "w"))

# 通过类创建对象会自动调用init方法，该类处init方法中有配置文件参数，这里通过os模块获取配置文件路径
conf = HandleConfig(os.path.join(CONFDIR, "config.ini"))
# conf.write_data("test_data", "tester", "lilystar")

