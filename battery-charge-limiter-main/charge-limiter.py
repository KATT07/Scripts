import psutil
import subprocess

tper=20

battery_status = psutil.sensors_battery()
print(battery_status)
if (battery_status!=None):
    print(battery_status.percent)
    if (battery_status.percent<tper):
        subprocess.run(['shutdown','-P','now'],shell=True)
else:
    print("Battery Not Detected!")
