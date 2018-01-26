#coding:utf-8

import urllib
import urllib2
import requests
import chardet
import codecs
import re

url ='http://www.budejie.com/text/1'

def download(url):
    if url is None:
        return None
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    headers = {'User-Agent':user_agent}
    r = requests.get(url)
    rs = requests.get(url,files=files)
    print(rs.text)
    with open("budejie.txt","w") as f:
        f.write(str)

    return rs.text


    if r.status_code == 200:
        print(r.encoding)
        print(r.text,'\n{}\n'.format('*'*79),r.encoding)

        return r.text
    return None


if  __name__ == '__main__':
    txtresult = download(url)
    pattern = re.compile(r'<div class="j-r-list-c-desc">\s+(.*)\s+</div>')
    print txtresult

    result = re.findall(pattern,txtresult)
    str = re.match(pattern,txtresult)
    print(str)



    print result




