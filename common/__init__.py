# import requests
# import jsonpath
# # 第一个请求
# # 登录的接口
# headers = {"X-Lemonban-Media-Type":"lemonban.v2"}
# url = "http://api.lemonban.com/futureloan/member/login"
# data = {
#     "mobile_phone": "13367899876",
#     "pwd": "lemonban"
# }
# res = requests.post(url=url,json=data, headers=headers)
# data1 = res.json()
# print(data1)
#
# # 第二个请求
# s = requests.session()   # 创建session对象,以通过鉴权
# url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
# data = {
#     "mobilephone":"13367899876",
#     "pwd":"lemonban"
# }
#
# res = s.post(url=url, data=data)   # 如果这里直接使用request直接请求，则无法通过鉴权
# print(res.json())

# 日志
# import logging
# mylog = logging.getLogger("lily")
# mylog.setLevel("DEBUG")
# sh = logging.StreamHandler()
# sh.setLevel("DEBUG")
# mylog.addHandler(sh)
#
# fh = logging.FileHandler(filename="log.log", encoding="utf8")
# fh.setLevel("ERROR")
# mylog.addHandler(fh)



# class Phone():
#      @staticmethod
#      def huawei():
#          print("华为手机")
#
# res = Phone.huawei()
# print(res)

# 下载图片
# import requests
# url = "https://www.baidu.com/img/flexible/logo/pc/result.png"
# rs = requests.get(url=url)
# with open("baidupicture.png", "wb") as f:
#     f.write(rs.content)

