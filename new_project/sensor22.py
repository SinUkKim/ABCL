import RPi.GPIO as GPIO

# GPIO 초기화
def setup_sensor(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)

# 센서 상태 읽기
def read_sensor(pin):
    return GPIO.input(pin)
