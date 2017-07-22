import webbrowser
import time
import datetime
count=0
print ("The program started on" + time.ctime())
while (count<3):
    time.sleep(3)
    webbrowser.open("www.facebook.com")
    count=count+1
