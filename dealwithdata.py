#
# @Time     : 2022/07/17 18:05
# @Author   : Dragon.G
# @File     : dealwithdata.py
import json
import re


def deal_original_data(content):
    p = re.compile(r'@">(.+?)<')
    data = p.findall(content)
    return data


def list_of_group(list_info, lenth):
    listofgroup = zip(*(iter(list_info),) * lenth)
    endlist = [list(i) for i in listofgroup]
    count = len(list_info) % lenth
    endlist.append(list_info[-count:]) if count != 0 else endlist
    return endlist


def data_json(data):
    datajson = []
    for item in data:
        data_cell = {'course_term': item[2].split(' ')[0],
                     'course_name': item[3].split(' ')[0],
                     'course_type': item[4].split(' ')[0],
                     'course_credit': item[5].split(' ')[0],
                     'course_mark': item[6].split(' ')[0],
                     'mark_type': item[7].split(' ')[0],
                     'earned_credit': item[8].split(' ')[0]}
        datajson.append(data_cell)
    return datajson


def write_json(data):
    with open('datas.txt', 'w', encoding='utf-8') as file:
        for i in range(len(data)):
            file.write(json.dumps(data[i], ensure_ascii=False) + '\n')
        file.write('\n')
    file.close()


def deal_with_data(original_data):
    data = deal_original_data(original_data)
    datalist = list_of_group(data, 11)
    datajson = data_json(datalist)
    return datajson
