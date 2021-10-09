import requests
from bs4 import BeautifulSoup
import pandas as pd

# 코스피 200 거래량 상위 크롤링
def get_trading_high():
    trading_high_dict = {}
    url = "https://finance.naver.com/sise/entryJongmok.naver?order=acc_quant&isRightDirection=true"
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    obj_name = bs_obj.find_all("a", {"target": "_parent"})      # 코드 이름
    obj_number = bs_obj.find_all("td", {"class" : "number"})    # 거래량
    obj_per = bs_obj.find_all("td", {"class" : "number_2"})     # 등락률
    # print(str.strip(obj_per[1].text))
    # print(str.strip(obj_per[5].text))

    for i in range(5):
        trading_high_dict[obj_name[i].text] = obj_number[i].text
        df = pd.DataFrame(trading_high_dict.items(), columns=['code_name', 'trading'])

    print(df)
    return df

#get_trading_high()

def get_kospi200_highest():
    highest_dict = {}
    url = "https://finance.naver.com/sise/entryJongmok.naver?order=change_rate&isRightDirection=true"
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    obj_name = bs_obj.find_all("a", {"target": "_parent"})
    obj_per = bs_obj.find_all("span", {"class" : "tah p11 red01"})

    for i in range(5):
        highest_dict[obj_name[i].text] = str.strip(obj_per[i*2+1].text)
        df = pd.DataFrame(highest_dict.items(), columns=['code_name', 'percent'])

    return df



def get_kospi200_lowest():
    lowest_dict = {}
    url = "https://finance.naver.com/sise/entryJongmok.naver?order=change_rate&isRightDirection=false"
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    obj_name = bs_obj.find_all("a", {"target": "_parent"})
    obj_per = bs_obj.find_all("span", {"class" : "tah p11 nv01"})

    for i in range(5):
        #print(obj_name[i].text)
        text = str.strip(obj_per[i*2+1].text)
        lowest_dict[obj_name[i].text] = str.strip(obj_per[i*2+1].text)
        df = pd.DataFrame(lowest_dict.items(), columns=['code_name', 'percent'])
        #print(str.strip(obj_per[i*2+1].text))

    print(lowest_dict)
    print(df)
    return df


# 코스피200 수익률 상위 하위 url
# https://finance.naver.com/sise/entryJongmok.naver?order=change_rate&isRightDirection=true

# company_code를 입력받아 bs_obj를 리턴
def get_bs_obj_num(company_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

# company_code를 입력받아 now_price를 출력
def get_now_price(company_code):
    bs_obj = get_bs_obj_num(company_code)
    no_today = bs_obj.find("p", {"class": "no_today"})
    blind = no_today.find("span", {"class": "blind"})
    blind = blind.text
    now_price = blind.replace(',', '')  # 쉼표(,),제거
    this_close = int(now_price)
    return this_close

# company_code 기준 어제 가격 추출
def get_yesterday_price(company_code):
    bs_obj = get_bs_obj_num(company_code)
    no_yesterday = bs_obj.find("td", {"class" : "first"})
    blind = no_yesterday.find("span", {"class": "blind"})
    blind = blind.text
    yesterday_close = blind.replace(',', '')  # 쉼표(,),제거
    this_close = int(yesterday_close)  # data를 숫자로 인식
    return this_close


# company_code 기준 어제 및 현재 가격 추이 추출
def get_now_yes_price(company_code):
    now_price = get_now_price(company_code)         # 오늘 실시간 현재가 가져오기
    yes_price = get_yesterday_price(company_code)   # 어제 종가 가져오기
    diff = now_price - yes_price
    plus_minus = str(diff)[0]                       # plus_minus로 상승, 하락 판단
    per = abs(round(diff / yes_price * 100, 2))     # per은 %, 부호 제외한 퍼센트 값만 출력

    if plus_minus == '-':
        pass
    else:
        plus_minus = '+'

    print(now_price, yes_price, diff, plus_minus, per)
    return now_price, yes_price, diff, plus_minus, per

