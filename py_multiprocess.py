from multiprocessing import Pool, Process
import os, time, random


''' multiprocessing

multiprocessing 模块提供了一个Process类来代表一个进程对象，下面example演示了启动一个子进程并等待其结束
创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比linux里的fork()还要简单
join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
'''

# 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))


# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args = ('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')


''' multiprocessing

如果要启动大量的子进程，可以用进程池的方式批量创建子进程
'''
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(3)
    end = time.time()
    print('Task %s run %0.2f seconds' % (name, (end-start)))


if __name__ == '__main__':
    ''' 输出 (4核CPU)
        Parent process 21984.
        Wait for all sub process done...
        Run child process 0 (22692)...
        Run child process 1 (22700)...
        Run child process 2 (22324)...
        Run child process 3 (20736)...
        Task 0 run 3.00 seconds
        Run child process 4 (22692)...
        Task 1 run 3.00 seconds
        Task 2 run 3.00 seconds
        Task 3 run 3.00 seconds
        Task 4 run 3.00 seconds
        all subprocess done

    # Pool的大小默认是CPU的核数，task 0,1,2,3立即执行，task 4要等前面某个task执行完后才执行，
    # 如果有8核CPU，要至少提交9个子进程才能看到这个等待效果
    '''
    print('Parent process %s.' %os.getpid())
    pool = Pool(4)
    for i in range(5):
        # NewToMe: 多进程 - 进程池
        pool.apply_async(run_proc, args=(i,))
    print('Wait for all sub process done...')
    pool.close()
    # 等待所有子进程执行完毕，调用join之前必须调用close，调用close之后就不能继续添加新的饿Process了
    pool.join()

    print(' all subprocess done')

    