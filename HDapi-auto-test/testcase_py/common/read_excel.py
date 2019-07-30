import xlrd
import xlwt
from openpyxl import worksheet
from xlutils.copy import copy
class readExcel():
    def __init__(self, path):
        self.path = path

    def open_excel(self):
        xl = xlrd.open_workbook(self.path)
        return xl

    def get_sheetnames(self):
        table = self.open_excel().sheet_names()
        return table


    def get_data(self,name,rows,cols):
        table = self.open_excel().sheet_by_name(name)
        data = table.col_values(rows,cols,table.nrows)  #rows第一行数据   cols，table.nrows  从第cols+1行到所有数据
        return data
    def get_rows(self,name):
        table = self.open_excel().sheet_by_name(name)
        rows = table.nrows
        return rows
    def get_row(self,name):
        table = self.open_excel().sheet_by_name(name)
        row = table.row()
        return row

    def write_excel(self, row, value):
        # 管道作用
        try:
            wb = copy(self.open_excel())
            # 通过get_sheet()获取的sheet有write()方法
            ws = wb.get_sheet(0)  # 1代表是写到第几个工作表里，从0开始算是第一个。
            ws.write(row, 5, value)
            print("'here----------------'")
        except IOError as e:
            print(e.args)

        except Exception as e:
            print(e.args)

        else:
            print("ok-----")

        wb.save(self.path)
    def get_data_ncol(self, name,cols, startrows, endrows):
        table = self.open_excel().sheet_by_name(name)  # sheet页名字
        data = table.col_values(cols, startrows, endrows)  # cols想取第几列数据将   startrows-1开始的行数 endrows结束的行数
        return data




