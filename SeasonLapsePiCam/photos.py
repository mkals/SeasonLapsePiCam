import os
from datetime import time as dtime
from datetime import datetime
import time

class SeasonLapsePiCam:
    auto_updating = False

    def take_photo(self):
        # os.system('fswebcam -r 4208x3120 -S 3 --jpeg 95 --save /home/pi/' + file_path + file_name) # uses Fswebcam to take picture
        os.system('fswebcam -r 4208x3120 -S 3 --jpeg 95 --save /home/pi/images/trysil-%H.%M.%S.jpg') # uses Fswebcam to take picture

    def set_auto_update(self):
        now = datetime.now()
        now_time = now.time()
        if now_time >= dtime(20,00) or now_time <= dtime(5,00):
            # at night, do not update

            if self.auto_updating == True:
                print("Stopping auto_update at", now_time)
                self.auto_updating = False

        else:
            # do fetch photos automatically

            if self.auto_updating == False:
                print("Starting auto_update at", now_time)
                self.auto_updating = True

        return self.auto_updating

print("Script to take imageges every minute")
print("current time: ", datetime.now().time())
s = SeasonLapsePiCam()

while True:
    # if s.set_auto_update():
    #     print("taking photo")
    try:
        s.take_photo()
    except:
        print("error, could not take photo")
    # else:
    #     print("not taking photo")

    time.sleep(60)
