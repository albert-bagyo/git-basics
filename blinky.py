import threading
from gpiozero import PWMLED
from time import sleep

stop = threading.Event()
state = {'change_speed': False, 'q': 1.0, 'stop': False }
led = PWMLED(17)

lock = threading.Lock()
        
def blink():
    global state
    sleep_time = 1
    with lock:
        while True:
            if state['stop']:
                break
            if state['change_speed']:
                sleep_time *= state['q']
                state['change_speed'] = False
            led.pulse(fade_in_time=1, fade_out_time=1, background=False)
            sleep(sleep_time)
            led.off()
            sleep(sleep_time)

thread = threading.Thread(target = blink)
thread.start()

print("Enter a mode for blinking.\n1.Faster\n2.Slower\n3.Stop")
while True:
     i = input("::")
     if i.lower() == 'faster':
         print('Blinking Faster! :)')
         state['q'] = 0.5
         state['change_speed'] = True
     elif i.lower() == 'slower':
         print('Blinking Slower :(')
         state['q'] = 2
         state['change_speed'] = True
     elif i.lower() == 'stop':
         state['stop'] = True
         break 
