# coding=utf8
__author__ = 'sunyawei'
import xlsxwriter


class Excel(object):
    @staticmethod
    def create_workbook(filename):
        workbook = xlsxwriter.Workbook(filename)
        return workbook

    @staticmethod
    def create_workbook_in_memory(output):
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        return workbook

    @staticmethod
    def add_worksheet(workbook, sheet_name):
        worksheet = workbook.add_worksheet(sheet_name)
        return worksheet

    @staticmethod
    def set_column_width(worksheet, column_map):
        for _, column in column_map.items():
            cell_flag = column['column_name'] + ':' + column['column_name']
            worksheet.set_column(cell_flag, column['width'])

    @staticmethod
    def write_column_title(worksheet, column_map, bold):
        for _, column in column_map.items():
            cell_flag = column['column_name'] + str(1)
            worksheet.write(cell_flag, column['column_title'], bold)

    @staticmethod
    def write_cell(worksheet, column_name, row_id, content, bold=False):
        cell_flag = column_name + str(row_id)
        if bold:
            worksheet.write(cell_flag, content, bold)
        else:
            worksheet.write(cell_flag, content)

def test1():
    excel = Excel()
    workbook1 = excel.create_workbook(u"天上掉下个玲妹妹.xls")
    sheet1 = excel.add_worksheet(workbook1, u"你是我的")
    bold1 = workbook1.add_format({'bold': 1})
    column_map1 = {
        'find_time': {'column_name': 'A', 'column_title': u'发现威胁时间', 'width': 20},
        'threat_time': {'column_name': 'B', 'column_title': u'威胁发生时间', 'width': 20},
        'ip': {'column_name': 'C', 'column_title': u'受害IP', 'width': 20},
        'skyeye_type': {'column_name': 'D', 'column_title': u'类别', 'width': 20},
        'detail': {'column_name': 'E', 'column_title': u'简介', 'width': 20},
        'collect': {'column_name': 'F', 'column_title': u'关注', 'width': 20},
        'alarm_state': {'column_name': 'G', 'column_title': u'状态', 'width': 20}
    }
    results = [{
        'find_time': 1,
        'threat_time': 2,
        'ip': 3,
        'skyeye_type': 4,
        'detail': 5,
        'collect': 6,
        'alarm_state': 7
    }
    ]
    excel.set_column_width(sheet1, column_map1)
    excel.write_column_title(sheet1, column_map1, bold1)

    row = 2
    for result in results:
        for field_name, field_value in result.items():
            excel.write_cell(sheet1, column_map1[field_name]['column_name'], row, field_value)
        row += 1
    workbook1.close()


def test2():
    workbook1 = xlsxwriter.Workbook(u"玲妹妹.xls")
    sheel1 = workbook1.add_worksheet(u"天上掉下来的")
    # 4. 定义一个加粗的格式对象
    bold = workbook1.add_format({'bold': True})
    sheel1.write(0, 0, u"我是第一列", bold)
    workbook1.close()
test2()
