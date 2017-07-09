import time
import multiprocessing

area = []
def calc_square(a,lock):
    #global area
    for n in a:  #注意，这里是for、不是if
        time.sleep(3)
        lock.acquire()
        area.append(n * n) #注意append的用法，list，以及本身输出即可
        print("square area: ",area) #注意缩进与程序的结构关系
        #area.append(n * n)
        lock.release()
def calc_cube(a,lock):
    for n in a:
        time.sleep(3)
        lock.acquire()
        area.append(n*n*n)
        print("cube area: ",area)
        lock.release()


if __name__ == "__main__":  #main是线程0
    arr = [2,5,3,8]
    lock = multiprocessing.Lock() #加锁
    process_1 = multiprocessing.Process(calc_square(arr,lock)) #线程1
    process_2 = multiprocessing.Process(calc_cube(arr,lock))  #线程2

    process_1.start()
    process_2.start()
    process_1.join()  #等待前面程序完成
    process_2.join()

    print(area)
    print("Done!")


