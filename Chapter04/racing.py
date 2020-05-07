
import time, random 
from threading import Thread, Lock 
g = 0

def add_one(t):
    global g
    for i in range(0, 10):
        a = g 
        time.sleep(random.randrange(1, 5) * 0.001) 
        g = a + 1 
        print('\t' * t + ':' + str(g)) 
        time.sleep(random.randrange(1, 5) *0.05)

threads = [] 
for i in range(0, 3):
    threads.append(Thread(target=add_one, args=[i])) 
    print (i * '\t' + "starts threads " + str(i)) 
    threads[i].start()

for thread in threads:
    thread.join()

print("\nFinal g = " + str(g))
