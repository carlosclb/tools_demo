import xlrd


def get_all(file_path, subtable):
    # 打开excel表格
    filename = xlrd.open_workbook(file_path)
    # 打印excel所有子表格的名字
    form_name = filename.sheet_names()
    # 获取选择子表格的位置
    subtable_location = form_name.index(subtable)
    # 选择子表格为操作对象
    sheet = filename.sheet_by_index(subtable_location)
    # 获取选取对象的行数
    row_num = sheet.nrows
    value_library = []
    for row_location in range(1, row_num):
        row_location_value = sheet.row_values(row_location)
        if row_location_value[0]:
            row_location_value[0] = row_location_value[0].replace('(', '（').replace(')', '）')
            row_location_value[2] = row_location_value[2].replace('对', 'A').replace('错', 'B').replace('\n', '')
            value_library.append(row_location_value)
    return value_library


value_lib = get_all(r"2.xlsx", "sheet1")  # 读全部数据
with open('all.txt', 'a', encoding='utf-8') as f:
    for value in value_lib:
        temp_dic = {'q': value[0], 'a': value[1], 'ans': value[2]}
        f.write(str(temp_dic))
        f.write('\n')
