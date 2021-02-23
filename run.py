# 封装执行测试用例
import os
import unittest
import datetime

from BeautifulReport import BeautifulReport

from Library.HTMLTestRunnerNew import HTMLTestRunner
from common.handle_01path import CASEDIR, REPORTDIR
from common.handle_08email import send_email

date= datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.discover(CASEDIR))

rf = os.path.join(REPORTDIR , date+"report.html")

# runner = HTMLTestRunner(stream=open(rf, "wb"),
#                         title="纳税人学堂项目",
#                         description="纳税人学堂管理端自动化测试",
#                         tester="lily")
# runner.run(suite)


br = BeautifulReport(suite)
br.report("河北学堂项目自动化测试", filename=date+"raport.html", report_dir=REPORTDIR)
send_email(rf, "邮件报告")







