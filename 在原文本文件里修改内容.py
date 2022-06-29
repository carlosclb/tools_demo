"""
修改文本文件的内容，并写回原文件
"""
file_data = ''
with open('test.txt', "r", encoding="utf-8") as f:
    for row in f:
        row = eval(row)
        if ',' in row['q']:
            row['q'] = row['q'].replace(',', '，')
        row = str(row)
        file_data += row + '\n'
with open('test.txt', "w", encoding="utf-8") as f:
    f.write(file_data)
