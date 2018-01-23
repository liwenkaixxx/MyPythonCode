#coding:utf-8

import re
import requests

p_common = re.compile('\d{3}[1-9]00')
p_special = re.compile('\d{2}0000')

citys_result = []

with open('citys_ori')as f_city_ori,open('citys_cleared','wb')as f_city_cleared:
    city_ori_list = f_city_ori.read().split("\n")
    city_ori_list.append("\n")
    city_ori_list = map(lambda x:x.strip().strip('　').
                        replace('     '," ").replace('         　',' ').
                        replace("     　"," "),
                        city_ori_list)
    for index,city_ori in enumerate(city_ori_list):
        if p_common.findall(city_ori) and not ('市辖区' in city_ori) and\
                not('县'in city_ori):
            print city_ori
            citys_result.append(city_ori)

        elif p_special.findall(city_ori) and\
            ("市辖区"in city_ori_list[index+1] or
             p_special.findall(city_ori_list[index+1]) or
            city_ori_list[index+1]==""):
            print city_ori
            citys_result.append(city_ori)

    f_city_cleared.write("\n".join(citys_result))





