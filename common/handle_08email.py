# # 封装发送邮件模块(引用mime 多组件文本，多元件,  邮件附件
#
# import smtplib
# from email.mime.application import MIMEApplication
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# from common.handle_03config import conf
#
#
# def send_email(filename, title):
#     smtp = smtplib.SMTP_SSL(host = conf.get("email","host"), port = conf.get("email","port"))
#     smtp.login(user=conf.get("email", "user"), password=conf.get("email", "pwd"))
#
#     msg = MIMEMultipart()              # 创建多组件对象
#
#     with open(filename, "rb") as f:
#         content = f.read()
#
#     text_msg = MIMEText(content, _charset="utf8", _subtype="html")   # 创建邮件文本
#
#     msg.attach(text_msg)    # 将文本添加到多组件中
#
#     report_file = MIMEApplication(content)
#     report_file.add_header("content-dispositon", "attachment", filename=filename)
#
#     msg.attach(report_file)
#
#     msg["subject"] = title
#     msg["From"] = conf.get("email", "from_addr")
#     msg["To"] = conf.get("email", "to_addr")
#
#     smtp.send_message(msg, from_addr=conf.get("email", "from_addr"), to_addrs=conf.get("email","to_addr"))
#
"""
email: 1648466124@qq.com
tester: lily
"""
# 封装一个发送邮件的函数
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from common.handle_03config import conf

def send_email(filename, title):           # 封装成发送邮件的函数
    smtp = smtplib.SMTP_SSL(host=conf.get("email", "host"), port=conf.getint("email", "port"))   # 连接邮件， 注意使用getint方法 获取port  端口号是整数类型
    smtp.login(user=conf.get("email", "user"), password=conf.get("email", "pwd"))
    # 创建多组件的邮件
    msg = MIMEMultipart()  # 通过类创建对象

    with open(filename, "rb") as f:  # 使用二进制rb方式进行读取，以防止打开报告出现乱码
        content = f.read()
    # 创建文本内容
    text_msg = MIMEText(content, _subtype="html", _charset="utf8")
    # 添加到多组件的邮件中
    msg.attach(text_msg)
    # 创建邮件的附件
    report_file = MIMEApplication(content)
    report_file.add_header("content-disposition", "attachment", filename=filename)  # 设置发送邮件的头部信息
    # 将邮件添加到多组件的邮件中
    msg.attach(report_file)

    msg["Subject"] = title
    msg["From"] = conf.get("email", "from_addr")
    msg["To"] = conf.get("email", "to_addr")

    smtp.send_message(msg, from_addr=conf.get("email", "from_addr"), to_addrs=conf.get("email", "to_addr"))



