import time
import random
import RPi.GPIO as GPIO
from sensor22 import setup_sensor, read_sensor
from cue22 import setup_cue, turn_on_cue, turn_off_cue, get_led_state
from csv_write22 import initialize_csv, write_data, get_current_time
from serial_com22 import setup_serial, turn_on_motor

#-------------- declaration with other modules ----------------#
sensor_pin = 22
cue_pin = 17
file_name = 'datafile.csv'
serial_port = '/dev/ttyACM0'
#------------------------ declaration ----------------------#
global sensor_state
sensor_state = False
count = 0
current_time = None
delay_interval = time.perf_counter()
cue_led_time = 2
cue_interval_variable = 5
cue_interval_max = 30
cue_interval = random.uniform(cue_interval_variable, cue_interval_variable + 5)


def get_sensor_state(sensor_pin):
    global sensor_state
    if read_sensor(sensor_pin) == GPIO.HIGH:
        sensor_state = False
    elif read_sensor(sensor_pin) == GPIO.LOW:
        sensor_state = True


#---------------- initalize -----------------#
setup_sensor(sensor_pin)
setup_cue(cue_pin)
setup_serial(serial_port)
file, writer = initialize_csv(file_name)
#---------------- main ---------------------#

GPIO.add_event_detect(sensor_pin, GPIO.BOTH, callback=get_sensor_state, bouncetime=50)

try:
    while True:
        control_time = time.perf_counter() 
        cue_control_time = time.perf_counter()
        while True: 
            # 5 ~ 10초 사이의 첫 큐 인터벌만큼 시간이 지났고, 큐가 꺼져있으면 --> 큐를 실행시키고 큐를 켠 시간을 기록
            if time.perf_counter() - control_time >= cue_interval_variable and not get_led_state(cue_pin): 
                turn_on_cue(cue_pin)
                cue_control_time = time.perf_counter()
            # 큐를 켠 시간으로부터 n초가 지났고, 큐가 켜져있으면 --> 큐를 끄고, 큐 인터벌을 재설정정
            if time.perf_counter() - cue_control_time >= cue_led_time and get_led_state(cue_pin):
                turn_off_cue(cue_pin)
                cue_interval = random.uniform(cue_interval_variable, cue_interval_variable + 5)
                break
            # 큐가 켜져있고, 센서에 감지되면 --> 큐를끄고 모터를 돌리고 성공을 출력하고 큐 인터벌 범위를 5 ~ 10으로 조정하고
            # 성공 카운트를 올리고, 성공 시간과, 카운트를 기록하며, 성공하자마자 실패로 기록되지 않도록 delay를 준다다
            if get_led_state(cue_pin) and sensor_state:
                turn_off_cue(cue_pin)
                turn_on_motor()
                print("헤헤~~")
                cue_interval_variable = 5
                count += 1
                write_data(writer, get_current_time(), count)
                delay_interval = time.perf_counter()
                break
            # 마구마구 실패하지 않도록 if문 체크에 0.5초 딜레이를 주고, 큐가 꺼져있는데 센서가 반응하면, 큐 인터벌을 높이는 과정, 대신 큐 인터벌이 30을 넘기지 못하게 제한
            if time.perf_counter() - delay_interval > 0.5 and not get_led_state(cue_pin) and sensor_state and cue_interval_variable + 10 <= cue_interval_max:
                delay_interval = time.perf_counter()
                cue_interval_variable += 5
                cue_interval = random.uniform(cue_interval_variable, cue_interval_variable + 5)
                print("do not touch without cue")
                print(cue_interval_variable)
                break    

except KeyboardInterrupt:
    print("Interrupted")
finally:
    file.close()  
    GPIO.cleanup() 
    #change
