import requests
import signal
import time

import scrollphathd
from scrollphathd.fonts import font3x5

def getTime():
    r = requests.get("http://api.tfl.gov.uk/stopPoint/490013457N/Arrivals")
    json_result = r.json()
    my_stops = []
    for x in json_result:
        y = str(int(x['timeToStation']/60)).zfill(2)
        z = ' min ' + str(x['lineId'])
        my_stops.append(y)
        my_stops.sort()
        str1 = ', '.join(my_stops) +', '
        
    while True:
        print(str1)
        scrollphathd.write_string(str1, y=1, font=font3x5, brightness=0.5)
        scrollphathd.show()
        scrollphathd.scroll()
        time.sleep(0.04)
    
while True:
    getTime()
    time.sleep(10)
        


