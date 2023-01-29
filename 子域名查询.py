# https://www.dnsgrep.cn/subdomain/csdn.net
import json
import requests
from bs4 import BeautifulSoup
from flask import Flask, request

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def index():
    key = request.args.get("wd")
    ret = ''
    if key == None:
        ret = '操你妈'
    else:
        re = requests.get('https://www.dnsgrep.cn/subdomain/'+key)
        soup = BeautifulSoup(re.text, 'lxml')
        soup = soup.find_all('td')
        s = []
        for i in soup:
            i = i.text.replace(' ', '').replace('\n', '')
            # print(i)
            s.append(i)
        ret = json.dumps(s, ensure_ascii=False)
    return ret


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=2224, debug=True)
