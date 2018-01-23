#coding:utf-8

#import thread
import threading
from time import sleep,ctime

loops = [4,2]

def loop(nloop,nsec):
    print('start loop',nloop,'at:',ctime())
    sleep(nsec)
    print('loop',nloop,'done at:',ctime())
    #lock.release()

def main():
    print 'starting at:',ctime()
    #锁
    #locks = []
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        '''
        lock = thread.allocate_lock()
        lock.acquire
        locks.append(lock)
        '''
        t = threading.Thread(target=loop,
                             args=(i,loops[i]))
        threads.append(t)

    for i in nloops:
        #thread.start_new_thread(loop(i,loops[i],locks[i]))
        threads[i].start()              #start threads

    for i in nloops:                    # wait for all
        #while locks[i].locked():pass
        threads[i].join()               # threads to finish

    print 'all DONE at:',ctime()

if __name__ == '__main__':
    main()



