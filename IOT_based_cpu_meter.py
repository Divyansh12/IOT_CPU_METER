import psutil
from boltiot import Bolt

api_key = "XXXXXXXXXXXXXXXXXXXXXXX"
d_id = "XXXXXXXX"

cpu_red_threshold = 50
client= Bolt(api_key, d_id)

#interval in seconds to check cpu usage
interval = 5

def control_green_led(pin, value):
    response = client.digitalWrite(pin, value)

def control_red_led(pin, value):
    response = client.digitalWrite(pin, value)

while True:
    cpu_usage = psutil.cpu_percent(interval = interval)
    print ("CPU usage is", cpu_usage)
    if cpu_usage > cpu_red_threshold:
        control_green_led('0','LOW')
        control_red_led('1', 'HIGH')
        control_red_led('2', 'LOW')
    else:
        control_green_led('0', 'HIGH')
        control_red_led('1', 'LOW')
