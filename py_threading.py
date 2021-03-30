import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print('start thread: '+ self.name)
        print_time(self.name, self.counter,5)
        print('end threadL '+ self.name)

def print_time(thread_name, delay, counter):
    while counter:
        if exitFlag:
            thread_name.exit()
        time.sleep(delay)
        print('%s:%s' % (thread_name, time.ctime((time.time()))))
        counter -=1

thread1 = myThread(1,'thread-1',1)
thread2 = myThread(2,'thread-2',2)

thread1.start()
thread2.start()

# thread1.join() #等待至线程终止
# thread2.join()

print('exist main thread')