#***************************************************************************************
#               Code for Controlling Pi Volume Using Rotary Encoder
#                     Original Code: https://bit.ly/2OcaQGq
#                    Re-Written by Sid for Sid's E Classroom
#                    https://www.youtube.com/c/SidsEClassroom
#             All text above must be included in any redistribution.
#  If you find this useful and want to make a donation -> https://paypal.me/sidsclass
# ***************************************************************************************
 
from RPi import GPIO
from time import sleep
import alsaaudio

# Change the following pins based on your application or HAT in use
encoder_clk = 17
encoder_data = 29
encoder_button = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(encoder_clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(encoder_data, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(encoder_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

m = alsaaudio.Mixer()

# Set desired minimum and maximum values
min = 0
max = 100

# Set the volume change step size
volume_step_size=5

is_Muted = m.getmute()[0]
volume = m.getvolume()[0]

if is_Muted == 0:
    is_Muted=False
else:
    is_Muted=True
print("Mute State: " + str(is_Muted))
print("Volume: " + str(volume))
print("")
clkLastState = GPIO.input(encoder_clk)
btnLastState = GPIO.input(encoder_button)

try:
    while True:
        btnPushed = GPIO.input(encoder_button)
        if ((not btnLastState) and btnPushed):
            if is_Muted:
                is_Muted = False
                m.setmute(0)
                print("Mute State: " + str(is_Muted))
                print("Volume: " + str(int(volume)))
                print("")
            else:
                is_Muted = True
                m.setmute(1)
                print("Mute State: " + str(is_Muted))
                print("Volume: " + str(int(volume)))
                print("")
            sleep(0.2)
        else:
            clkState = GPIO.input(encoder_clk)
            dtState = GPIO.input(encoder_data)
            if clkState != clkLastState and clkState == 0:
                if dtState != clkState:
                    volume += volume_step_size
                    if volume > max:
                        volume = max
                else:
                    volume -= volume_step_size
                    if volume < min:
                        volume = min
                print("Mute State: " + str(is_Muted))
                print("Volume: " + str(int(volume)))
                print("")
                m.setvolume(int(volume))
            clkLastState = clkState
        btnLastState = btnPushed
        sleep(0.01)
finally:
    GPIO.cleanup()
