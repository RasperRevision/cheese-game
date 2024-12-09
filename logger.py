import time


def log(msg):
    current_time = time.localtime(time.time())

    hrs = pad(str(current_time.tm_hour))
    mins = pad(str(current_time.tm_min))
    secs = pad(str(current_time.tm_sec))

    print(f'[{hrs}:{mins}:{secs}] {msg}') 
  
def pad(string):
    while len(string) < 2:
        string = '0' + string
    return string
