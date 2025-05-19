import influxdb_client
import psutil
from influxdb_client import Point
from influxdb_client.client.write_api import SYNCHRONOUS

token = ""
org = ""
url = "http://192.168.xxx.xxx:xxxxx"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket = "xxx"

write_api = client.write_api(write_options=SYNCHRONOUS)

battery_status = psutil.sensors_battery()
if battery_status is not None:
    print(battery_status.percent)
    point = (
        Point("xxx-battery")
        .field("Bat", battery_status.percent)
    )
    write_api.write(bucket=bucket, org=org, record=point)
else:
    print("No Battery Found")
