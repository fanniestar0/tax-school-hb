# 封装读取测试用例的类
import openpyxl

class ReadExcel(object):
    def __init__(self, filename, sheet_name):
        self.filename = filename
        self.sheet_name = sheet_name

    def openfile(self):
        self.wb = openpyxl.load_workbook(self.filename)
        self.sh = self.wb[self.sheet_name]

    def read_data(self):
        self.openfile()
        data = list(self.sh.rows)
        title = list(i.value for i in data[0])
        cases = []
        for i in data[1:]:
            values = list(a.value for a in i)
            case = dict(zip(title, values))
            cases.append(case)
        return cases

    def write_data(self, row, column, value):
        self.openfile()
        self.sh.cell(row=row, column=column, value=value)
        self.wb.save(self.filename)

# 表单需与封装的读取表达的类在同一目录下， 才可读取成功数据
# excel = ReadExcel("api_cases_hb.xlsx", "login")            # 通过定义的类名创建个对象
# case_datas = excel.read_data()                      # 对象调用方法
# print("读取出来的数据为:", case_datas)




