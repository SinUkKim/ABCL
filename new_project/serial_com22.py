import serial
import time

arduino = None
def setup_serial(port): 
    global arduino
    arduino = serial.Serial(port, 9600) 
    time.sleep(1) # 첫 세팅, 선언, 초기화 과정이라 딜레이 1

def turn_on_motor():
    global arduino
    arduino.write(b'1') # 아두이노에 1 보내기기
