import time

def wait1():
    print("sleep 1")
    time.sleep(1)
    
def wait2():
    print("sleep 2")
    time.sleep(2)
    
wait1()
wait2()

time.sleep(3)