import time, random 
from threading import Thread, Lock 
lock = Lock()
lock2 = Lock()
g = 0

def add_one(t):
    global g 
    for i in range(0, 10):
        k = (random.randrange(1, 10) > 3) 
    if k:
        lock2.acquire() # lock 
        time.sleep(random.randrange(1, 5) *0.05)
        lock.acquire() # lock 
    else:
        lock.acquire() # lock
        time.sleep(random.randrange(1, 5) *0.05) 
        lock2.acquire() # lock

    a = g 
    time.sleep(random.randrange(1, 5) * 0.001) 
    g = a + 1 
    print('\t' * t + ':' + str(g)) 
    lock2.release() # unlock 
    lock.release() # unlock lock 2

threads = [] 
for i in range(0, 3):
    threads.append(Thread(target=add_one, args=[i])) 
    print (i * '\t' + "starts threads " + str(i)) 
    threads[i].start()

for thread in threads:
    thread.join()
    
print("\nFinal g = " + str(g))
