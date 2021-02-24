# 封装添加课件测试用例类
import os
import unittest
import jsonpath

from Library.ddt import ddt, data
from common.handle_01path import DATADIR
from common.handle_02readexcel import ReadExcel
from common.handle_03config import conf
from common.handle_04data import CaseData, replace_data
from common.handle_05requests import SendRequests
from common.handle_06logs import log

file_data = os.path.join(DATADIR, "api_cases_hb.xlsx")

@ddt
class CourseWare(unittest.TestCase):
    excel = ReadExcel(file_data, "courseware")
    cases = excel.read_data()
    request = SendRequests()

    @classmethod
    def setUpClass(cls):
        url = conf.get("evn", "url") + "/server//adminLogin/byPassword"
        headers = eval(conf.get("evn", "headers"))
        data = {"phone": "18502183690", "password": "123456Aa"}
        response = cls.request.send_request(url=url, headers=headers, json=data, method="post")
        res = response.json()
        print("实际结果:", res)
        accessToken = jsonpath.jsonpath(res, "$..accessToken")[0]
        CaseData.accessToken = accessToken
        print("提取的token值：", CaseData.accessToken)


    def setUp(self):
        url = conf.get("evn", "url") + "/server//file/upload"
        headers = eval(conf.get("evn", "headers"))
        headers["accessToken"] = getattr(CaseData, "accessToken")

        files = {
            "file": ("filename.doc",open(r"D:\下载\Automation Code study\tax-school-hb\testcases\filename.doc", "rb"),
                     "msword")

        }
        response = self.request.send_request(url=url, files=files, headers=headers,  method="post")
        res = response.json()
        print("文件上传实际结果：", res)
        data = jsonpath.jsonpath(res, "$..data")[0]
        CaseData.data = data
        print("提取的filekey值：", CaseData.data)


    @data(*cases)
    def test_addcourse(self, case):
        url = conf.get("evn", "url") + case["url"]
        print("新增课件的url:", url)
        headers = eval(conf.get("evn", "headers"))
        headers["accessToken"] = getattr(CaseData, "accessToken")
        method = case["method"]
        data = eval(replace_data(case["data"]))
        expected = eval(case["expected"])
        row = case["case_id"] + 1


        response = self.request.send_request(url=url, method=method, json=data, headers=headers)
        res = response.json()
        print("新增课件的实际请求：", res)



        try:
            self.assertEqual(expected["code"], res["code"])
            self.assertEqual(expected["msg"], res["msg"])
        except AssertionError as e:
            self.excel.write_data(row=row, column=8, value="未通过")
            log.error("用例{}执行未通过".format(case["title"]))
            log.exception(e)
            raise e
        else:
            self.excel.write_data(row=row, column=8, value="通过")
            log.info("用例{}执行通过".format(case["title"]))

