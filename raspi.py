import time
from firebase import firebase
firebase = firebase.FirebaseApplication('https://sapj01.firebaseio.com/')
import Rpi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
fanpin=29
tvpin=31
musicpin=33
lightpin=35
GPIO.setup(fanpin,GPIO.out,initial=0)
GPIO.setup(tvpin,GPIO.out,initial=0)
GPIO.setup(musicpin,GPIO.out,initial=0)
GPIO.setup(lightpin,GPIO.out,initial=0)

while True:
    

    fanpin = firebase.get('/','fan')
    tvpin = firebase.get('/','tv')
    musicpin = firebase.get('/','music')
    lightpin = firebase.get('/','light')

    print(fanpin," ",tvpin," ",musicpin," ",lightpin)

    time.sleep(1)
