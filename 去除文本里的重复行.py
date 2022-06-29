"""
去除文本文件里的重复行
"""
temp_list = []
topic_list = []
with open('test.txt', 'r', encoding='utf-8') as f:
    for row in f:
        row = eval(row)
        if row['q'] not in temp_list:
            temp_list.append(row['q'])
            topic_list.append(row)
topic_list.sort(key=lambda x: x['q'])
with open('test.txt', 'w', encoding='utf-8') as f:
    for i in topic_list:
        f.write(str(i))
        f.write('\n')