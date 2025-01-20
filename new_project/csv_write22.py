import csv
from datetime import datetime

def initialize_csv(file_name):
    file = open(file_name, mode='w', newline='')
    writer = csv.writer(file)
    writer.writerow(['시작', '카운트'])
    return file, writer # file 만들고 기본 행에 '시작', '카운트'

def write_data(writer, sensing_time, count):
    writer.writerow([sensing_time, count]) # 시간과, 성공 카운트 적기

def get_current_time():
    current_time = datetime.now()
    return current_time.strftime("%Y-%m-%d %H:%M:%S") # 현재시간 format
