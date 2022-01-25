from selenium import webdriver
import time
import pandas as pd
import requests
import re
import pandas as pd
import json

# 实例化一款浏览器
bor = webdriver.Chrome(executable_path='chromedriver.exe')
# getting to ppl's pages
mainUrl = "https://www.behance.net/search/users?field=graphic%20design"
# 对指定的url发起请求
bor.get(mainUrl)
# login
time.sleep(60)
# maxlink
maxLinkNum = 1300
# 讲link写入文件
fileIO = open("link.txt", 'a+')
linkList = []
# scroll length
scoll = 0
while True:
    links = bor.find_elements_by_xpath("//a[@class='UserSummary-displayName-3EE']")
    for link in links:
        # get link
        link = link.get_attribute('href')
        if link not in linkList:
            linkList.append(link)
            # 将link写入文件
            link = link.split('?')
            link = link[0] + "/info"
            fileIO.write(link + '\n')
            fileIO.flush()
    scoll = scoll + 8888
    # scroll down
    js = "var q=document.documentElement.scrollTop={}".format(scoll)
    bor.execute_script(js)
    # wait for loading
    time.sleep(2)
    if len(linkList) > maxLinkNum:
        break

# VPN
proxy = {
    'http': 'socks5h://127.0.0.1:10808',
    'https': 'socks5h://127.0.0.1:10808'
}
# cookie
headers = {
    'content-type': 'application/x-www-form-urlencoded',
    'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
    'cookie': 'gk_suid=77253252; gki=%7B%22feature_stock_rail%22%3Afalse%7D; bcp=b79d1c3e-ba37-4739-9132-007d69b508a1; AMCVS_9E1005A551ED61CA0A490D45%40AdobeOrg=1; s_cc=true; feds_privacy_consent={"hasUserProvidedConsent":true,"userHasCustomConsent":false}; _fbp=fb.1.1642923640553.1940926288; bcp_susi_initiated_at=1642926575789; iat0=eyJhbGciOiJSUzI1NiIsIng1dSI6Imltc19uYTEta2V5LTEuY2VyIn0.eyJpZCI6IjE2NDI5MjY1OTU4MjdfNTI2ODQwNTYtZTc0Mi00NGVkLWE5OTUtMzg0MzFmMmRjM2ExX3VlMSIsInR5cGUiOiJhY2Nlc3NfdG9rZW4iLCJjbGllbnRfaWQiOiJCZWhhbmNlV2ViU3VzaTEiLCJ1c2VyX2lkIjoiQzBCMDI1Qjg2MUVEMTIwMTBBNDk1RUQzQEFkb2JlSUQiLCJzdGF0ZSI6IntcImFjXCI6XCJiZWhhbmNlLm5ldFwiLFwiY3NyZlwiOlwiYjc5ZDFjM2UtYmEzNy00NzM5LTkxMzItMDA3ZDY5YjUwOGExXCJ9IiwiYXMiOiJpbXMtbmExIiwiYWFfaWQiOiJDMEIwMjVCODYxRUQxMjAxMEE0OTVFRDNAQWRvYmVJRCIsImN0cCI6MCwiZmciOiJXRUlEM0tBQ1hMRTdJN1dDRk9RRlJIUUE3TT09PT09PSIsInNpZCI6IjE2NDI5MjY1OTQzNTVfZTVkNDcyMDktMjEzNy00OGVlLWI5ZjktN2Q0ZjhkMzI2NjA5X3VlMSIsIm1vaSI6IjJiODRiNzYzIiwicGJhIjoiIiwiZXhwaXJlc19pbiI6Ijg2NDAwMDAwIiwic2NvcGUiOiJBZG9iZUlELG9wZW5pZCxnbmF2LHNhby5jY2VfcHJpdmF0ZSxjcmVhdGl2ZV9jbG91ZCxjcmVhdGl2ZV9zZGssYmUucHJvMi5leHRlcm5hbF9jbGllbnQsYWRkaXRpb25hbF9pbmZvLnJvbGVzIiwiY3JlYXRlZF9hdCI6IjE2NDI5MjY1OTU4MjcifQ.hm-xC6HSPrZlEJbRt_9IZadNFDsSBOjpz_mdnzvu-a52F23gzEdtJD7Lt6v1V8FPp8FIuVEH4HyNbDCx5USVURyFCi7wddzxMU46hnePzVCXgDRwtKSGP0OB778VPzeMFzyvq8aNV1TOfwBULI_8VMcupxA4q0n5OLyUZyZikfXN_PsN4CMyMWinmkVEpSV-qXqPzbmHuKEzBQ-CGfawVat6HInjnsPYBk8EulJUfh3mTEajo8NVYVzmwWwWNkaM0CRLZAxh73AgZiiVeFkJdT-a2F0R-vB_be8jjIe-1vWd3IBVO2Sgm9HLWdkcEnypmXXGM9_BgzPgVznhiDdXew; bein=true; s_sq=%5B%5BB%5D%5D; AMCV_9E1005A551ED61CA0A490D45%40AdobeOrg=870038026%7CMCMID%7C64138611472712500244354885131298221940%7CMCAID%7CNONE%7CMCOPTOUT-1642951421s%7CNONE%7CMCAAMLH-1643549021%7C3%7CMCAAMB-1643549021%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCCIDH%7C-274907240%7CvVersion%7C5.0.0; s_ppv=[%22www.behance.net/modern_hero%22%2C98%2C0%2C2117.4444580078125%2C1536%2C849%2C1536%2C960%2C2.25%2C%22P%22]; gpv=behance.net:profile:default; OptanonConsent=isIABGlobal=false&datestamp=Sun+Jan+23+2022+23%3A04%3A31+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=6.9.0&hosts=&consentId=9b90ada9-b6d5-4ec1-a19b-53c8b3e76fd7&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false'
}
# 对指定的url发起请求
csv_data = {"USERNAME": [], "ABOUT": []}
data = open('link.txt')
cnt = 0
for line in data:
    line = line.strip('\n')
    bor.get(line)
    # get returned content
    response = requests.get(line, headers=headers, proxies=proxy)
    resp = response.text
    pattern = re.compile(r'"about":\[\{[^}]*}]')
    result1 = pattern.search(resp).group(0)
    time.sleep(1)
    name = bor.find_element_by_xpath("//h1[@class='ProfileCard-userFullName-3jr']").text
    csv_data["USERNAME"].append(name)
    csv_data["ABOUT"].append(result1)
# write csv
csv = pd.DataFrame(csv_data)
csv.to_csv("60045.csv")
# read csv
data = pd.read_csv("60045.csv").values
csvData = {"USERNAME": [], "ABOUT": []}
for line in data:
    username = line[1]
    about = line[2]
    about = about[9:-1]
    about = json.loads(about)
    name = str(about['name']).lower()
    value = about['value']
    # selecting info
    if (name == 'about me' or name == 'обо мне' or name == 'about' or name == 'about us') == False:
        value = "None"
    else:
        # remove tags 
        value = value.replace("\n", "")
        value = value.replace("<br />", "")
        value = value.replace("<div class='variable-text variable-text-short'>", "")
    csvData['USERNAME'].append(username)
    csvData['ABOUT'].append(value)
# enter into csv
csvData1 = pd.DataFrame.from_dict(csvData)
csvData1.to_csv("1.csv", index=0)
