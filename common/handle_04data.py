# 封装正则表达式， 替换测试用例中的变量数据
import re
from common.handle_03config import conf # 快捷的导入方式：选中内容按快捷键Alt+Enter

class CaseData():
    pass
def replace_data(s):
    r = r"#(.*?)#"
    while re.search(r, s):
        res = re.search(r, s)
        key = res.group(1)
        # 替换后的value值首先从配置文件中找，配置文件中如无则从封装的空类中找（CaseData类是存储所有提取的变量信息）
        try:
            value = conf.get("test_data", key) # 括号前是实值， key是用例中符合规则的变量
        except Exception:
            value = getattr(CaseData, key)
        finally:
           s = re.sub(r, value, s, 1)
    return s





