# https://velog.io/@paori/chart.js-%EA%B7%B8%EB%9E%98%ED%94%84-%EB%A7%8C%EB%93%A4%EA%B8%B0
# https://jsikim1.tistory.com/143 - 날짜 계산


from datetime import datetime
from dateutil.relativedelta import relativedelta


def get_day_before_day7():
    current_date = datetime.now().date()

    # current_date = '2021-09-13'
    # current_date = datetime.strptime(current_date, '%Y-%m-%d').date()

    before_date = current_date - relativedelta(days=9)
    return before_date, current_date


def get_day_before_month():
    current_date = datetime.now().date()

    # current_date = '2021-09-13'
    # current_date = datetime.strptime(current_date, '%Y-%m-%d').date()

    before_date = current_date - relativedelta(months=1)
    return before_date, current_date

print(get_day_before_month())

def get_day_before_month3():
    current_date = datetime.now().date()

    # current_date = '2021-09-13'
    # current_date = datetime.strptime(current_date, '%Y-%m-%d').date()

    before_date = current_date - relativedelta(months=3)
    return before_date, current_date

def get_day_before_year():
    current_date = datetime.now().date()

    # current_date 대신 2줄로 대체
    # current_date = '2021-09-13' # 임시로 설정
    # current_date = datetime.strptime(current_date, '%Y-%m-%d').date()  # strptime : 문자열을 날짜로 바꿔주는 함

    before_date = current_date - relativedelta(years=1) + relativedelta(days=1) # 365일
    return before_date, current_date


def get_day_total():
    current_date = datetime.now().date()

    # current_date = '2021-09-13'
    # current_date = datetime.strptime(current_date, '%Y-%m-%d').date()
    before_date = datetime.strptime('2011-01-01', '%Y-%m-%d').date()

    return before_date, current_date

