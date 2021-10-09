# import requests
# from bs4 import BeautifulSoup
#
# def get_bs_obj_num():
#     url = "https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd=005930&target=finsum_more"
#
#     result = requests.get(url)
#     bs_obj = BeautifulSoup(result.content, "html.parser")
#     return bs_obj
#
#
# def get_now_price():
#     bs_obj = get_bs_obj_num()
#     #obj =
#     obj = bs_obj.find("span", {"class": "span-sub"})
#     print(obj)
#     #blind = no_today.find("span", {"class": "blind"})
#     #now_price = blind.text
#     #return now_price
#
# get_now_price()


import requests
from bs4 import BeautifulSoup

URL = "https://finance.naver.com/item/main.nhn?code=005930"

samsung_electronic = requests.get(URL)
html = samsung_electronic.text
soup = BeautifulSoup(html, 'html.parser')

finance_html = soup.select('div.section.cop_analysis div.sub_section')
print(finance_html)



# import pandas as pd
# import requests
#
#
# code = '005930'
# URL = f"https://finance.naver.com/item/main.nhn?code={code}"
# r = requests.get(URL)
# df = pd.read_html(r.text)[3]
# print(df)