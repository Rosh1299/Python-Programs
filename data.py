import requests
import schedule
import time


def api_call():
    URL = "http://35.239.95.43:8000/exhibitionbanner/bbe534b09fe94a2fa4490816932c5ccc"
    r = requests.get(url=URL)
    data = r.json()
    print(type(data))


api_call()
# print("After 1 min")
# schedule.every(1).minutes.do(api_call)
# while True:

#     # Checks whether a scheduled task
#     # is pending to run or not
#     schedule.run_pending()
#     time.sleep(1)
