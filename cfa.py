import datetime
import random
import re
import requests
import selenium
import time
from requests import session

US_PROXIES = 'https://www.us-proxy.org/'

def main():
    while True:
        proxy_list = get_proxy_list()
        working_list = []
        print('Building New Proxy List...')
        for proxy, port in proxy_list.items():
            formatted_proxy = 'http://' + proxy + ':' + port
            if check_proxy(formatted_proxy):
                working_list.append(formatted_proxy)
        print('# of Working Proxies in List: ' + str(len(working_list)))
        
        for x in working_list:
            print('Current Proxy: ' + x)
            while True:
                proxy = {'http':x}
                code = code_gen()
                try:
                    if check_code(code, proxy):
                        print(*code)
                        complete_survey(code, proxy)
                except Exception as e:
                    print(e)
                    print('Switching proxies...\n')
                    break


def get_proxy_list():
    data = requests.get(US_PROXIES).text
    data_sect = data.split('<td>')
    proxy_port = []
    for x in data_sect:
        x = x.replace('</td>','')
        results = re.search('[a-zA-Z]', x)
        if results is None:
            proxy_port.append(x)
    proxy_list = {}
    count = 0
    for x in proxy_port:
        if count % 2 == 0:
            proxy_list[x] = proxy_port[count+1]
        count = count + 1
    return proxy_list


def check_proxy(proxy):
    try:
        requests.get('https://api.ipify.org', proxies={'http': proxy}, timeout=10).text
        return True
    except:
        return False


def code_gen():
    orderNum = str(random.randint(0, 999)).zfill(3)
    digFive = str(random.randint(1, 3))
    registerNum = "5"
    firstSeven = orderNum + "0" + digFive + "0" + registerNum
    storeNum = "01336"
    hour = str(random.randint(7, 21)).zfill(2)
    minute = str(random.randint(0 ,59)).zfill(2)
    time =  hour + minute
    curMon = str(datetime.date.today().strftime("%m"))
    curDay = str(datetime.date.today().strftime("%d"))
    date = curMon + curDay
    year = "9"
    digSeven = str(random.randint(0,9))
    lastTwo = year + digSeven
    result = [firstSeven, storeNum, time, date, lastTwo]
    return result


def check_code(code, proxy):
    s = session()
    c_result = s.get('https://www.mycfavisit.com/', timeout=10, proxies=proxy).text
    c_result = c_result.split('\n')
    c = ''
    for r in c_result:
        if 'Survey.aspx?c=' in r:
            c = r.split('c=')[1].split('"')[0]
            break
    payload = {'JavaScriptEnabled':'1', 'FIP':'True', 'CN1':code[0], 'CN2':code[1], 'CN3':code[2], 'CN4':code[3], 'CN5':code[4], 'NextButton':'Start', 'AllowCapture':''}
    request_url = 'https://www.mycfavisit.com/Survey.aspx?c=' + c
    response = s.post(request_url, data=payload, timeout=10, proxies=proxy).text
    if 'Sorry, we are unable to continue the survey based on the information you provided.' in response:
        return False
    elif 'Please rate your overall satisfaction with your most recent visit to this' in response:
        return True
    else:
        raise Exception('Hit Block Page')


def complete_survey(code, proxy):
    return 0


if __name__ == "__main__":
    main()