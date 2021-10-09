import pandas as pd
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django import forms
from .models import * #모델 불러오기
from django.views.generic import FormView
from .crawling.stock_index import *
from .crawling.main_kospi200 import *
from .code_chart.calculate_day import *
from .crawling.list_kospi200 import *
from django.db import connection
import statistics
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.utils import timezone
import random
import math



def index(request):
    return render(request, 'main/index.html')

def kospi200_page(request):
    # 3개월 주가 그릴 리스트 만들기
    date_list, close_list = get_kospi200_month3()

    # 3개월 주가 중 최소값 최대값 구하기
    max_price = max(close_list)
    min_price = min(close_list)

    # 코스피 실시간 가격, 등락률 및 상승, 하락, 보합 리스트 생성
    kospi200_dict = kospi200_now()

    # 아래 200개 리스트를 위한 column으로 구성된 리스트
    page_df = detail_kospi200()
    code_name = list(page_df['종목별'])
    close = list(page_df['현재가'])
    diff = list(page_df['전일비'])
    per = list(page_df['등락률'])
    volume = list(page_df['거래량'])
    amount = list(page_df['거래대금(백만)'])
    market_cap = list(page_df['시가총액(억)'])

    # 상승, 하락, 보합 계산
    up, down, mid = 0, 0, 0
    for i in per:
        if i[0] == '-':
            down += 1
        elif i[0] == '+':
            up += 1
        else:
            mid += 1

    kospi200_dict['up'] = up
    kospi200_dict['down'] = down
    kospi200_dict['mid'] = mid
    kospi200_dict['max_price'] = max_price
    kospi200_dict['min_price'] = min_price

    ## 날짜, 시간 표시 ##
    now = timezone.now()

    return render(request, 'main/kospi200_page.html',{
        'kospi200_dict':kospi200_dict, 'date_list':date_list, 'close_list':close_list,
        'code_name':code_name, 'close':close, 'diff':diff,
        'per':per, 'volume':volume, 'amount':amount, 'market_cap':market_cap,'now':now
    })




def jongmok_name(request, code_name):

    ## 날짜, 시간 표시 ##
    now = timezone.now()

    myCode = stock_info.objects.get(code_name=code_name)

    now_price, yes_price, diff, plus_minus, per = get_now_yes_price(myCode.code_num)
    rank = kospi200_list.objects.get(code_name=code_name).id

    # 2020년 대비 상승률
    price_obj = db_interaction.objects.get(date='2020-12-30', code_name=code_name)
    price_2020 = price_obj.close
    per_2020 = round((now_price - price_2020) / price_2020 * 100)  # 2020년 대비 상승률

    # 매출액 - sale_rank
    sale_obj = f_summary.objects.filter(date='2020/12')
    sale_obj = sale_obj.order_by('-sale')  # 매출액 내림차순 정렬
    sale_df = pd.DataFrame(list(sale_obj.values('code_num', 'sale')))
    sale_rank = sale_df.index[sale_df['code_num'] == myCode.code_num][0] + 1

    # 업종 내 순위 - 완료
    sector_obj = stock_info.objects.filter(sector=myCode.sector)
    sector_list = list(sector_obj.values('code_num'))
    myList = []

    for i in sector_list:
        myList.append(i['code_num'])

    sector_rank_obj = db_interaction.objects.filter(date='2021-09-13', code_num__in=myList)
    sector_rank_obj = sector_rank_obj.order_by('-market_cap')
    sector_df = pd.DataFrame(list(sector_rank_obj.values('code_num', 'market_cap')))
    sector_rank = sector_df.index[sector_df['code_num'] == myCode.code_num][0] + 1

    # 이거는 아래 업종 내 비교에서 쓰일것임 ( 시총 순서로 나열되어 있음. )
    sector_list = list(sector_df['code_num'])

    # 현재가 시작
    now_price, yes_price, diff, plus_minus, per = get_now_yes_price(myCode.code_num)




    ### 1day chart list ###

    # 예시로 장 마감 기준으로 그래프 하나 만들기
    x_list = ["09:30", "10:00", "10:30", "11:00", "11:30", "12:00",
              "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30"]
    y_list = []
    x_list_append, y_list_append = [], []

    # 현재까지 있는 값 들어가는 코드
    def rangeNum(s, e):
        return int(random.random() * (e - s + 1)) + s

    for i in range(0, len(x_list)):  # 0~ 13 앞까지
        if i < 9 :
            y_day1 = rangeNum(now_price - now_price/50, now_price + now_price/50)
            y_day1 = round(y_day1/100) * 100
            y_list.append(y_day1)
        # 나머지는 NAN으로 처리
        else :
            y_day1 = 'NAN'
            y_list_append.append(y_day1)

    # 아래는 동일
    mean_price_day1 = round(statistics.mean(y_list))
    max_price_day1 = round(max(y_list))
    min_price_day1 = round(min(y_list))

    day1_list = [x_list, y_list, mean_price_day1, max_price_day1, min_price_day1, x_list[0], x_list[len(y_list)-1]]











    ### 7 day data list ###
    x_list, y_close_list, y_trading_list = [], [], []

    before_date, current_date = get_day_before_day7()
    code_obj = db_interaction.objects.filter(date__range=[before_date, current_date], code_name=code_name)
    # code_obj = code_obj.filter(date__range=[before_date, current_date])
    date_obj = list(code_obj.values('date'))
    close_obj = list(code_obj.values('close'))
    trading_obj = list(code_obj.values('trading_volume'))

    for i in range(0, len(date_obj)):
        x_list.append(date_obj[i]['date'])
        y_close_list.append(close_obj[i]['close'])
        y_trading_list.append(trading_obj[i]['trading_volume'])

    # 7일 종가 중 평균, 최소 최고 찾기
    mean_price_day7 = round(statistics.mean(y_close_list))
    max_price_day7 = max(y_close_list)
    min_price_day7 = min(y_close_list)

    # 기간 전달
    before_date_day7 = x_list[0]
    now_date_day7 = x_list[-1]
    day7_list = [x_list, y_close_list, y_trading_list,
                 mean_price_day7, max_price_day7, min_price_day7,
                 before_date_day7, now_date_day7]


### 1 month data list ###
    x_list, y_close_list, y_trading_list = [], [], []

    before_date, current_date = get_day_before_month()
    code_obj = db_interaction.objects.filter(date__range=[before_date, current_date], code_name=code_name)
    date_obj = list(code_obj.values('date'))
    close_obj = list(code_obj.values('close'))
    trading_obj = list(code_obj.values('trading_volume'))

    for i in range(0, len(date_obj)):
        x_list.append(date_obj[i]['date'])
        y_close_list.append(close_obj[i]['close'])
        y_trading_list.append(trading_obj[i]['trading_volume'])

    # 1달 close 중에서 평균, 최고, 최저
    mean_price_month = round(statistics.mean(y_close_list))
    max_price_month = max(y_close_list)
    min_price_month = min(y_close_list)

    before_date_month = x_list[0]
    now_date_month = x_list[-1]
    month1_list = [x_list, y_close_list, y_trading_list,
                   mean_price_month, max_price_month, min_price_month,
                   before_date_month, now_date_month]

### 3 month data list ###
    x_list, y_close_list, y_trading_list = [], [], []

    before_date, current_date = get_day_before_month3()
    #  obj = db_interaction.objects.filter(date__range = ['2020-09-15', '2020-10-01'], code_num='005930')[0].close
    code_obj = db_interaction.objects.filter(date__range=[before_date, current_date], code_name=code_name)
    date_obj = list(code_obj.values('date'))
    close_obj = list(code_obj.values('close'))
    trading_obj = list(code_obj.values('trading_volume'))

    for i in range(0, len(date_obj)):
        x_list.append(date_obj[i]['date'])
        y_close_list.append(close_obj[i]['close'])
        y_trading_list.append(trading_obj[i]['trading_volume'])

    # 3달 close 중에서 평균, 최고, 최저
    mean_price_month3 = round(statistics.mean(y_close_list))
    max_price_month3 = max(y_close_list)
    min_price_month3 = min(y_close_list)

    before_date_month3 = x_list[0]
    now_date_month3 = x_list[-1]
    month3_list = [x_list, y_close_list, y_trading_list,
                   mean_price_month3, max_price_month3, min_price_month3,
                   before_date_month3, now_date_month3]

### 1 year data list ###
    x_list, y_close_list, y_trading_list = [], [], []

    before_date, current_date = get_day_before_year()
    code_obj = db_interaction.objects.filter(date__range=[before_date, current_date], code_name=code_name)
    date_obj = list(code_obj.values('date'))
    close_obj = list(code_obj.values('close'))
    trading_obj = list(code_obj.values('trading_volume'))

    for i in range(0, len(date_obj)):
        x_list.append(date_obj[i]['date'])
        y_close_list.append(close_obj[i]['close'])
        y_trading_list.append(trading_obj[i]['trading_volume'])

# 1년 close 중에서 평균, 최고, 최저
    mean_price_year = round(statistics.mean(y_close_list))
    max_price_year = max(y_close_list)
    min_price_year = min(y_close_list)

    before_date_year = x_list[0]
    now_date_year = x_list[-1]

    year1_list = [x_list, y_close_list, y_trading_list,
                  mean_price_year, max_price_year, min_price_year,
                  before_date_year, now_date_year]

    ##### now price comma 콤마 넣기 #####
    now_price = format(now_price, ',d')
    mean_price_day7 = format(mean_price_day7, ',')
    max_price_day7 = format(max_price_day7, ',')
    min_price_day7 = format(min_price_day7, ',')
    mean_price_month = format(mean_price_month, ',')
    max_price_month = format(max_price_month, ',')
    min_price_month = format(min_price_month, ',')
    mean_price_month3 = format(mean_price_month3, ',')
    max_price_month3 = format(max_price_month3, ',')
    min_price_month3 = format(min_price_month3, ',')
    mean_price_year = format(mean_price_year, ',')
    max_price_year = format(max_price_year, ',')
    min_price_year = format(min_price_year, ',')


######## 주가 차트 데이터 끝 ##########

    ### 기본 재무제표 차트 포괄손익계산서,재무상태표 ###
    ### sale, profit, bi, margin_r, 순이익률 계산
    summary_obj = f_summary.objects.filter(code_num=myCode.code_num)
    summary_df = pd.DataFrame(
        list(summary_obj.values('date', 'code_num', 'sale', 'profit', 'ni', 'margin_r', 'roe', 'ta', 'td', 'debt_r')))

    summary_year_list = [2016, 2017, 2018, 2019, 2020]  # 이거 연도 빠져있는 경우 고려해보자... 특수 case
    print(summary_year_list)
    summary_sale_list = list(summary_df['sale'])
    print(summary_sale_list)

    summary_profit_list = list(summary_df['profit'])
    print(summary_profit_list)

    summary_ni_list = list(summary_df['ni'])
    print(summary_ni_list)

    summary_margin_r_list = list(summary_df['margin_r'])
    print(summary_margin_r_list)

    summary_roe_list = list(summary_df['roe'])
    print(summary_roe_list)

    summary_ta_list = list(summary_df['ta'])
    summary_td_list = list(summary_df['td'])
    summary_debt_r_list = list(summary_df['debt_r'])

    f_summary_list = [summary_year_list, summary_sale_list,
                      summary_profit_list, summary_ni_list,
                      summary_margin_r_list, summary_roe_list,
                      summary_ta_list, summary_td_list,
                      summary_debt_r_list]



   ##### 업종 내 재무제표 비교 매출/당기순이익

    sector_num = len(sector_list)
    print('sector_num : ', sector_num)
    print('sector_list : ', sector_list)

    result_compare_list = []

    # 종목 내 업종 개수가 4개 이상인 경우 -> 그냥 앞에 3개만 가져와
    if sector_num >= 3:
        sector_num = 3
        sector_list = sector_list[0:sector_num]

    # 1개라면 1개, 2개라면 2개, 3개라면 3개의 딕셔너리가 리스트 안에 들어간다.
    for i in sector_list:
        sale_list = []
        ni_list = []
        per_list = []
        roe_list = []
        code_num = i
        code_name = stock_info.objects.get(code_num=code_num).code_name

        # code num에 맞게 재무제표 필터링
        financial_obj = f_summary.objects.filter(code_num=code_num)
        sale_obj = list(financial_obj.values('sale'))
        ni_obj = list(financial_obj.values('ni'))
        per_obj = list(financial_obj.values('per'))
        roe_obj = list(financial_obj.values('roe'))

        for j in range(0, len(per_obj)):
            sale_list.append(sale_obj[j]['sale'])
            ni_list.append(ni_obj[j]['ni'])
            per_list.append(per_obj[j]['per'])
            roe_list.append(roe_obj[j]['roe'])

        sale_list = list(map(float, sale_list))
        ni_list = list(map(float, ni_list))
        per_list = list(map(float, per_list))
        roe_list = list(map(float, roe_list))

        # issue : 종목이 어떤 거는 5년치가 다 있겠지만, 없는 경우는..? 일단 고려 안하기로
        mydict = {'code_name': code_name,
                  'sale': sale_list, 'ni': ni_list, 'per': per_list, 'roe': roe_list}

        result_compare_list.append(mydict)

    compare_date = [2016, 2017, 2018, 2019, 2020]



    ### 투자의견 컨센서스 데이터 가져오기 ###
    concensus_obj = concensus.objects.filter(code_num=myCode.code_num)
    length = len(concensus_obj)

    con_date_list, con_target_list, con_recom_list, con_inst_list, con_close_list = [], [], [], [], []

    for i in range(length):
        con_date_list.append(concensus_obj[i].date)
        con_target_list.append(concensus_obj[i].target_prc)
        con_recom_list.append(concensus_obj[i].recom_cd)
        con_inst_list.append(concensus_obj[i].inst_nm)
        con_close_list.append(concensus_obj[i].close)

    concensus_dict = {'index_end': length - 1, 'date': con_date_list,
                      'target_prc': con_target_list,
                      'recom_cd': con_recom_list,
                      'inst_nm': con_inst_list,
                      'close': con_close_list}

    # 맨 마지막 per, eps 가져오기
    concensus_per_eps_obj = f_summary.objects.filter(code_num=myCode.code_num)
    myEps = format(round(concensus_per_eps_obj[len(concensus_per_eps_obj) - 1].eps),',')
    myPer = round(concensus_per_eps_obj[len(concensus_per_eps_obj) - 1].per , 1)
    concensus_now = {'opinion': round(con_recom_list[-1] ,2), 'goal': format(con_target_list[-1] ,','), 'eps': myEps, 'per': myPer,
                     'inst_nm': con_inst_list[-1]}
    print(concensus_dict)
    print(concensus_now)


    # 마니또
    manito_df = pd.read_csv("C:\projects\manito\juju\LSTM_pred.csv")
    manito_df = manito_df[manito_df["name"] == code_name]
    manito_date = list(manito_df['date'])
    manito_y = list(manito_df['y'])
    manito_yhat = list(manito_df['yhat'])

    # max, min을 구하기 위한 list ( y에서 0 제외 )
    sum_list = manito_y[0:9]

    # nan 없애기
    nan_delete = [x for x in manito_yhat if math.isnan(x) == False]
    sum_list.extend(nan_delete)
    manito_max = max(sum_list) * 1.15
    manito_min = min(sum_list) - min(sum_list) / 10

    for i in range(len(manito_y)):
        if manito_y[i] == 0:
            manito_y[i] = "."

    manito_list = [manito_date, manito_y, manito_yhat, manito_max, manito_min]



    return render(request, 'main/jongmok.html',{'myCode' : myCode, 'now':now,
                'rank': rank, 'per_2020': per_2020, 'sale_rank': sale_rank, 'sector_rank' : sector_rank,
                'now_price' : now_price, 'yes_price' : yes_price,
               'diff' : diff, 'plus_minus' : plus_minus, 'per' : per,

                'day1_list':day1_list,

                'day7_list':day7_list, 'month1_list':month1_list,
                'month3_list':month3_list ,'year1_list':year1_list, 'f_summary_list':f_summary_list,

                'sector_num': sector_num, 'compare_date': compare_date,
                'result_compare_list': result_compare_list,

                'concensus_now': concensus_now, 'concensus_dict': concensus_dict,
     'manito_list':manito_list, 'manito_date':manito_date, 'manito_y': manito_y, 'manito_yhat':manito_yhat,



'mean_price_day7':mean_price_day7, 'max_price_day7':max_price_day7, 'min_price_day7':min_price_day7,
'mean_price_month':mean_price_month,'max_price_month':max_price_month,'min_price_month':min_price_month,
'mean_price_month3':mean_price_month3, 'max_price_month3':max_price_month3,'min_price_month3':min_price_month3,
'mean_price_year':mean_price_year,'max_price_year':max_price_year,'min_price_year':min_price_year
})








def main_page(request):
    # 딕셔너리 형태로
    kospi_dict = kospi_now()
    kosdaq_dict = kosdaq_now()
    nasdaq_dict = nasdaq_now()
    df1 = get_kospi200_highest()
    df2 = get_kospi200_lowest()
    df3 = get_trading_high()


    ## 날짜, 시간 표시 ##
    now = timezone.now()

    return render(request, 'main/index.html',
                  {'dict1' : kospi_dict, 'dict2' : kosdaq_dict, 'dict3': nasdaq_dict,
                   'df1': df1, 'df2': df2, 'df3': df3,'now':now
                   })



 ########## 검색 기능 ##############
def jm_list(request):
    search_key = request.POST.get('search_key')
    print(search_key)

    return jongmok_name(request, search_key)






# def today(request): 실시간 날짜 테스트
#     """Shows todays current time and date."""
#     today = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
#     context = {'today': today}
#     return render(request, 'index.html',context)