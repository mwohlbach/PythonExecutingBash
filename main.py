import subprocess
import signal

def handler(signum,frame):
    print('Forever is ovah!!!')
    raise Exception("end of time")

def loop_forever():
    import time
    while 1:
        print ("sec")
        time.sleep(1)


signal.signal(signal.SIGALRM, handler)

signal.alarm(10)

try:
    loop_forever()
except Exception as exc:
    print (exc)

# output = subprocess.check_output(['bash','-c', 'git commit -m "hi mom"'])



# print(str(output))