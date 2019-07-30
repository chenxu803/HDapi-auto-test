

import os
import xlrd
from datetime import date,datetime
#切换到目录
# newpath=os.chdir(r'D:\HDapi-auto-test\testcase_excel')
# #文件名字
# filename='api_testcase.xlsx'
# #转换后的路径
# file = os.path.join(os.getcwd(), filename)
# print(file)
# """一，打开文件"""
# xl=xlrd.open_workbook(file)
# """二,获取sheet"""
# print(xl.sheet_names())
# print(xl.sheets())
# print(xl.nsheets)
# print(xl.sheet_by_name('getregion'))
# print(xl.sheet_by_index(0))
# """三，获取sheet内的汇总数据"""
# table=xl.sheet_by_name('getregion')
# print(table.name)
# print(table.nrows)
# print(table.ncols)
# """四，单元格批量读取"""
# print(table.row_values(0))
# print(table.row_values(1))
# print(table.row(0))
# print(table.row_types(1))
# #第0行的第2个到第4个
# print(table.col_values(0,2,5))
# """五，特别单元格的读取,以下效果都一样的"""
# #第二行第三列
# print(table.row(0)[1].value)
# print(table.cell_value(0,1))
# print(table.cell(0,1).value)
# #取类型
# print(table.row(0)[1].ctype)
# print(table.cell_type(0,1))
# print(table.cell(0,1).ctype)
# """六，常用技巧，(0,0)转成AI,表格的表头，A，B，C"""
# print(xlrd.cellname(0,0))
# print(xlrd.cellnameabs(0,0))
# print(xlrd.colname(3))
# print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
# """七，如何获取表格内不同类型的name"""
# print(table.cell_value(1,1)) #字符串 1
# print('字符串',table.cell_type(1,1))
# print(table.cell_value(1,2))#日期,3
# print('日期',table.cell_type(1,2))
# print(table.cell_value(1,3))#整数型2
# print('数字型',table.cell_type(1,3))
# print(table.cell_value(1,4))#布尔型 4
# print('布尔型',table.cell_type(1,4))
# #返回的值比较难以理解，需要封装，可以能看懂

def get_type(table,row,col):
    name = table.cell_value(row,col)
    type = table.cell_type(row,col)
    if type=='0':
        name='""'
    elif type==1:
        name='str'
    elif type==2 and name % 1==0:
        name="int"
    elif type==3:
        #方法一
        # date_value=xlrd.xldate.xldate_as_datetime(name,0)
        # name=date_value
        #方法二
        date_value=xlrd.xldate_as_tuple(name,0)
        name =datetime(*date_value).strftime('%Y/%m/%d %H:%M:%S')
    elif type==4:
        name=True if name==1 else False
    return name
print('↓↓↓↓↓↓↓↓↓封装函数')
newpath=os.chdir(r'D:\HDapi-auto-test\testcase_excel')
#文件名字
filename='api_testcase.xlsx'
#文件路径
file = os.path.join(os.getcwd(), filename)
xl=xlrd.open_workbook(file)
table=xl.sheet_by_name('getregion')

print(get_type(table,1,1)) #字符串 1
print('字符串',table.cell_type(1,1))

print(get_type(table,1,2))#日期,3
print('日期',table.cell_type(1,2))

print(get_type(table,1,3))#整数型2

print(get_type(table,1,4))#布尔型 4
print('布尔型',table.cell_type(1,4))


class XLdata():
    def __init__(self,path=''):
        self.xl=xlrd.open_workbook(path)

    def get_sheetinfo_by_name(self,sheetname):
        self.sheet=self.xl.sheet_by_name(sheetname)
        return self.get_sheet_info
    def get_sheet_info(self):
        infolist=[]
        for row in range(0,self.sheet_nrows):
            data=self.sheet.row_values(row)
            infolist.append(data)
        return infolist









