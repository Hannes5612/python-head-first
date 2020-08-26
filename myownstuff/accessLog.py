from requests import get
import json
import pprint

with open('access.log') as log:
    ips = [['1.1.1.1', 'Hannes']]
    count = 0
    for line in log:
        ip = line.split(' ', 1)[0]
        agent = line.split('"')[5]
        access = [ip, agent]
        if ips[count][0] != ip:
            ips.append(access)
            count += 1
    print(ips)

    file = open('cleanLog.log', 'a')
    for access in ips:
        url = 'http://ipinfo.io/' + access[0]
        response = get(url)
        data = json.loads(response.text)
        print(data['country'], data['city'], access[0], access[1], file=file)
    file.close()
    #
    #
    #
    # city = data['city']
    # region = data['region']
    # country = data['country']
    # postal = data['postal']
    # timezone = data['timezone']
    # ip = data['ip']
    #
    # print("ip:", ip)
    # print("city:", city)
    # print("region:", region),
    # print("country:", country)
    # print("postal:", postal)
    # print("timezone", timezone)
