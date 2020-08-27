from requests import get
import json
import pprint

with open('access.log') as log:
    ips = [['1.1.1.1', 'Hannes', "/Home2"]]
    count = 0
    for line in log:
        ip = line.split(' ', 1)[0]
        agent = line.split('"')[5]
        site = line.split('"')[1]
        siteDir = "/"
        if " " in site:
            siteDir = site.split(" ")[1]
        access = [ip, siteDir, agent]
        if ips[count][0] != ip:
            if ips[count][2] != siteDir:
                ips.append(access)
                count += 1

    file = open('cleanLog.log', 'a')
    for access in ips:
        url = 'http://ipinfo.io/' + access[0]
        response = get(url)
        data = json.loads(response.text)
        print(data)
        print(data['country'], data['city'], access[0], access[1], access[2], file=file)
    file.close()
















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
