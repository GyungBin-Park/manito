import requests
from bs4 import BeautifulSoup
import pandas as pd
from pykrx import stock
from datetime import datetime
from dateutil.relativedelta import relativedelta

import time

## 실시간으로 사용

def detail_kospi200():

    # 시가총액 기준 url
    url = "https://finance.naver.com/sise/entryJongmok.naver?order=market_sum&isRightDirection=true&page=1"
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")

    #df = pd.DataFrame()
    stock_head = bs_obj.find("table").find_all("th")
    data_head = [head.get_text() for head in stock_head]
    # print(data_head)
    # df = pd.DataFrame(columns = data_head)
    page_df = pd.DataFrame(columns=data_head)

    for i in range(1, 21):
        url = "https://finance.naver.com/sise/entryJongmok.naver?order=market_sum&isRightDirection=true&page="+ str(i)
        result = requests.get(url)
        bs_obj = BeautifulSoup(result.content, "html.parser")

        stock_name = bs_obj.find_all("td", {"class": "ctg"})
        name_list = [name.get_text() for name in stock_name]
        # print(name_list)

        obj = bs_obj.find_all("td", {"class": "number_2"})
        obj_list = [str.strip(data.get_text()) for data in obj]
        # print(obj_list)

        up_down = bs_obj.find_all("td", {"class": "rate_down2"})
        up_down_list = [str.strip(data.get_text()) for data in up_down]
        # print(up_down_list)

        # 거래량 셋팅
        volume = bs_obj.find_all("td", {"class": "number"})
        volume_list = [data.get_text() for data in volume]
        # print(volume_list)

        for j in range(10):
            page_df = page_df.append(pd.DataFrame([[name_list[j], obj_list[j * 4],
                                                    up_down_list[j], obj_list[j * 4 + 1],
                                                    volume_list[j], obj_list[j * 4 + 2], obj_list[j * 4 + 3]]],
                                                  columns=data_head))

    return page_df

# 현재 날짜를 통해 3달 전 날짜를 가지고 date list와 close list 생성
def get_kospi200_month3():
    current_date = datetime.today().date()
    before_date = current_date - relativedelta(months=3)
    before_date = before_date.strftime(("%Y%m%d"))  # 1달전 날짜 pykrx에 사용
    current_date = current_date.strftime(("%Y%m%d"))  # 현재 날짜 pykrx에 사용

    df = stock.get_index_ohlcv_by_date(before_date, current_date, "1028")
    df['date'] = df.index
    df['date']= df['date'].astype('str')    # date 문자열로 변환
    month_list, close_list = list(df['date']), list(df['종가'])
    print(month_list)
    print(close_list)
    return month_list, close_list




# if __name__ == "__main__":
#     page_df = detail_kospi200()
#     page_df.to_csv("kospi200_list_df.csv", encoding = 'utf-8-sig')
#     df = pd.read_csv("kospi200_list_df.csv")
#     df['id'] = df.index + 1
#     df.drop(['Unnamed: 0'], axis=1, inplace=True)
#     df.rename(columns={'종목별': 'code_name'}, inplace=True)
#     df.rename(columns={'현재가': 'close'}, inplace=True)
#     df.rename(columns={'전일비': 'diff'}, inplace=True)
#     df.rename(columns={'등락률': 'per'}, inplace=True)
#     df.rename(columns={'거래량': 'volume'}, inplace=True)
#     df.rename(columns={'거래대금(백만)': 'amount'}, inplace=True)
#     df.rename(columns={'시가총액(억)': 'market_cap'}, inplace=True)
#
#     my_conn = create_engine('mysql+pymysql://root:1234@127.0.0.1:3306/juju')
#     df.to_sql(con=my_conn, name='juju_kospi200_list', if_exists='replace', index=False)


# kospi 200 list page view
page_df = detail_kospi200()
code_name = list(page_df['종목별'])
close = list(page_df['현재가'])
diff = list(page_df['전일비'])
per = list(page_df['등락률'])
volume = list(page_df['거래량'])
amount = list(page_df['거래대금(백만)'])
market_cap = list(page_df['시가총액(억)'])

# 현재 : {{ kospi200_dict.now_price }}<br>
#         3개월 최저 : {{ kospi200_dict.min_price }}<br>
#         3개월 최고 : {{ kospi200_dict.max_price }}<br>
#         전일 대비 : {{kospi200_dict.plus_minus}}{{kospi200_dict.per}}<br>
#         상승 종목 수 : {{ kospi200_dict.up }}<br>
#         하락 종목 수 : {{ kospi200_dict.down }}<br>
#         보합 종목 수 : {{ kospi200_dict.mid }}<br>
