from datetime import datetime
from pydub import AudioSegment
from pydub.playback import play

#simple program that doesn't do anything but play sound at a certain time.

# playing alarm sound

tune  = AudioSegment.from_wav("mixkit-rooster-crowing-in-the-morning-2462.wav")

#getting the time
alarm_time = input("Enter the alarm time in HH:MM:SS\n")

alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:]

alarm_period = input("Enter alarm period (AM or PM)\n")

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alarm_seconds==current_seconds):
                    print("Wake Up!")
                    play(tune)
                    break