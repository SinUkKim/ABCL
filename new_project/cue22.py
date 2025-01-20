import RPi.GPIO as GPIO 

def setup_cue(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    global led_state
    led_state = False
    GPIO.output(17, GPIO.LOW)

def turn_on_cue(pin):
    GPIO.output(17, GPIO.HIGH)
    global led_state
    led_state = True
    print("CUE_ON") # 큐 켜고 state true


def turn_off_cue(pin):
    GPIO.output(17, GPIO.LOW)
    global led_state
    led_state = False
    print("CUE_OFF") # 큐 끄고 state false

def get_led_state(pin):
    return led_state # 큐가 ON인지 OFF인지 boolean output

