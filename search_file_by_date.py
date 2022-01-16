import os
import time
import datetime


date_today = datetime.date.today()
input_folder_name = "D:/Movies/Hollywood"
directory = os.listdir(input_folder_name)
for f in directory:
    if datetime.datetime.strptime(time.ctime(os.path.getmtime(os.path.join(input_folder_name, f))),
                                  "%a %b %d %H:%M:%S %Y").date() == date_today:
        print("name = "+f)
        size = os.path.getsize(os.path.join(input_folder_name, f))
        print("size = " + str(size) + " Byte")
