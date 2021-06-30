from multiprocessing import Process, Value, Array, Lock
import time

def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            number.value +=1
        # for i in range(len(numbers)):
        #     with lock:
        #         numbers[i] += 1

if __name__ == '__main__':
    lock1 = Lock()

    shared_number = Value('i', 0) #i-integer , 0-start
    #shared_array = Array('d', [0.0,100.0, 200.0])
    print('Begins at:', shared_number.value)
    #print('Begins at:', shared_array[:])

    p1 = Process(target=add_100, args=(shared_number, lock1))
    p2 = Process(target=add_100, args=(shared_number, lock1))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('number at end:', shared_number.value) #race condition as common var read write
#pooling
from multiprocessing import Pool

def cube(number):
    return number * number * number


if __name__ == "__main__":
    numbers = range(10)

    p = Pool()

    # by default this allocates the maximum number of available
    # processors for this task --> os.cpu_count()
    result = p.map(cube,  numbers) #map splits proccess, data and returns result as list
    #map,apply,join,close
    # or
    # result = [p.apply(cube, args=(i,)) for i in numbers]
    #apply does it one by one

    p.close()
    p.join()

    print(result)

#queue
from multiprocessing import Queue

def square(numbers, queue, lock):
    for i in numbers:
        with lock:
            queue.put(i*i)

def make_negative(numbers, queue, lock):
    for i in numbers:
        with lock:
            queue.put(i*-1)

if __name__ == "__main__":

    numbers = range(1, 6)
    q = Queue()
    lock = Lock() #without lock randomness exists

    p1 = Process(target=square, args=(numbers,q,lock))
    p2 = Process(target=make_negative, args=(numbers,q,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # order might not be sequential
    while not q.empty():
        print(q.get())

    print('end main')
