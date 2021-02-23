import os
import unittest

from Library.ddt import ddt, data
from common.handle_01path import DATADIR
from common.handle_02readexcel import ReadExcel
from common.handle_03config import conf
from common.handle_05requests import SendRequests
from common.handle_06logs import log


file_data = os.path.join(DATADIR, "api_cases_hb.xlsx")  # 使用路径拼接获取用例文件

@ddt
class LoginTest(unittest.TestCase):
    excel = ReadExcel(file_data, "login")
    cases = excel.read_data()
    print("测试用例数据：", cases)
    request = SendRequests()

    @data(*cases)
    def test_01login(self, case): # 这里的case是用于接收测试用例处的数据
        url = conf.get("evn", "url") + case["url"]
        # print("请求路径：", url)
        headers = eval(conf.get("evn", "headers"))
        method = case["method"]
        # print(method, type(method))
        data = eval(case["data"])
        # print(data, type(data))
        expected = eval(case["expected"])
        # print("预期结果：", expected)
        row = case["case_id"]+1

        response = self.request.send_request(url=url, headers=headers, method=method, json=data)    # 通过对象调用方法
        res = response.json()
        print("实际结果：", res)

        # 添加断言：
        try:
            self.assertEqual(expected["code"], res["code"])
            self.assertEqual(expected["msg"], res["msg"])
        except AssertionError as e:
            self.excel.write_data(row=row, column=8, value="未通过")
            log.error("用例{}执行未通过". format(case["title"]+1))
            log.exception(e)
            raise e
        else:
            self.excel.write_data(row=row, column=8, value="通过")
            log.info("用例{}执行通过".format(case["title"]))











