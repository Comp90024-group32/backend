from datetime import datetime
from dateutil.relativedelta import relativedelta

def generate_time_list(start_year, start_month, end_year, end_month):
    start_date = datetime(start_year, start_month, 1)
    end_date = datetime(end_year, end_month, 1)
    result = []

    current_date = start_date
    while current_date <= end_date:
        result.append([current_date.year, current_date.month])
        current_date = current_date + relativedelta(months=1)

    return result

def check_time_in_range(start_year, start_month, end_year, end_month, timestamp):
    # 解析给定的时间戳
    time = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")

    # 构造起始日期和结束日期
    start_date = datetime(year=start_year, month=start_month, day=1)
    end_date = datetime(year=end_year, month=end_month, day=1)

    # 判断时间是否在范围内
    if start_date <= time <= end_date:
        return True
    else:
        return False
