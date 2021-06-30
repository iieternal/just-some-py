#list ordered mutable, duplicate allowed
mylist = ["banana", "cherry", "apple"]
print(mylist)

item = mylist[-1]
print(item)

for i in mylist:
    print(i)

if "banana" in mylist:
    print("yes")

print(len(mylist))

mylist.append("lemon")
print(mylist)

mylist.insert(1, "blueberry")
print(mylist)

item = mylist.pop()
print(item)
print(mylist)

item = mylist.remove("cherry")
print(mylist)

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

newSortedList = sorted(mylist)

mylist.clear()

mylist = [0] * 5
print(mylist)

mylist2 = [1,2,3,4,5]

newlist3 = mylist + mylist2
print(newlist3)

mylist.clear()

mylist = [0,1,2,3,4,5,6,7,8,9]
print(mylist[1:5])
print(mylist[:5])
print(mylist[1:])
print(mylist[::3]) #every 3rd item
print(mylist[::-2]) #reverse nth items

list_org = ["banana", "cherry", "apple"]
list_cpy = list_org #memory pointer
list_cpy.append("lemon")
print(list_org)

list_cpy2 = list_org.copy() #list(list_org) or list[:]
list_cpy2.append("berry")
print(list_org)

c = [1,2,3,4,5,6]
d = [i*i for i in c] #[expression for loop]
print(d)

#tuple ordered, immutable, allows duplicate
mytuple = ("max", 28, "Boxton")
print(mytuple)
mytuple = "max", 28, "Boxton"
print(mytuple)
mytuple = ("max")
print(type(mytuple)) #becomes string not tuple
mytuple = ("max",)
print(type(mytuple)) #made tuple

qtuples = tuple(["Max", 28])
item = qtuples[1]
for i in qtuples:
    print(i)

if "Max" in qtuples:
    print("yes")

qtuples = ('a','p', 'p', 'l', 'e')
len(qtuples)

print(qtuples.count('p'))
print(qtuples.index('p'))

mylist = list(qtuples)
print(mylist)

qtuples = tuple(mylist)
print(qtuples)

#list same [start:stop] last index not included always

qtuples ="Max",28,"Boston"

name, age, _ = qtuples
print(name)

qtuples = (0,1,2,3,4)

i1, *i2, i3 = qtuples
print(i2)
print(i3)

import sys

mylist = [0,1,2,"hello", True]
my_tuple = (0,1,2,"hello", True)
print(sys.getsizeof(mylist), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

import timeit

print(timeit.timeit(stmt="[0,1,2,'hello', True]",number=1000000))
print(timeit.timeit(stmt="(0,1,2,'hello', True)",number=1000000))

#dictionary key-value, unordered, mutable
mydict = {"name": "Max", "age": 28,"city": "New York"}
print(mydict["name"]) #keyError
#dict(name="Max")
mydict["email"] = "max@xyz.com"
print(mydict)

del mydict["email"] #.pop("age") .popitem(##last item remove##)
print(mydict)

if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["lastname"])
except:
    print("Error")

for key in mydict: #key, value in mydict.items()
    pass
for key in mydict.keys(): #.values()
    pass
for key, value in mydict.items():
    print(key, value)

#copy mechanism is valid dict({}) or .copy()
mydict = {"name": "Max", "age": 28,"city": "New York"}
mydict2 = {"name": "Mary", "age": 27,"email": "mary@xyz.com"}

mydict.update(mydict2) #updates
print(mydict)

mydict = {3: 9, 6: 36, 9:81}
value = mydict[3]
print(value)

mytuple = (8,7)
mydict={mytuple: 15} #can't use list as key
print(mydict)

#sets unordered, mutable, no duplicates
myset ={1,2,3,1,2}
print(myset)
#{} is a dict
myset = set("Hello") #set([1,2,3,4])
print(myset) #no order

myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

myset.remove(3) #.discard(3) without error if not found .clear() .pop() - return arbritary value and remove it as well
print(myset)

#looping
#if x in

odds ={1,3,5,7,9}
evens = {2,4,6,8}
primes = {2,3,5,7}
print(odds.union(evens))
print(odds.intersection(primes))

setA = {1,2,3,4,5,6,7,8,9}
setB = {2,4,6,8,10}
print(setA.difference(setB)) #setA - setB, remove from setA
print(setA.symmetric_difference(setB)) #setA-setB noraml way

setA.update(setB) #intersection_update({}) (2,3,4,8) elements found in both sets
#difference_update({}), symmertric_sifference_update({})
print(setA)

setA = {1,2,3,4,5,6}
setB = {1,2,3}

print(setA.issubset(setB)) #_ is subset of _
print(setA.issuperset(setB))
setC = {7,8}
print(setA.isdisjoint(setB))
print(setA.isdisjoint(setC))

#copy works

#forzen set
a = frozenset([1,2,3,4])
print(a) #immutable


#strings ordered immutable
mystring = "Hello World"
print(mystring)
mystring= """
Hello World
Hello \
World
"""
print(mystring)

mystring = "Hello"
print(mystring[:4])

name = "Tom"
sentence = mystring + " " + name
print(sentence)

#for loop per chara
#if 'xyz' in

mystring = '   Hello World   '
print(mystring)
print(mystring.strip())

mystring = mystring.strip()
#.lower()
#.startswith('e') ###True,False###
#.endswith('ld')
#.find('o') first index find or -1
#.count('o') #2
#.replace('World', 'Universe')

mystring = 'how are you doing'
mylist = mystring.split() #default space , .split(",")
print(mylist)
print(''.join(mylist)) #extremely fast

#formarting

var = "Tom"
print("the variable is %s" % var) #%d %f %.2f
print("the variable is {}".format(var)) # {:.2f}
print(f"the variable is {var}") #{expressions}

#collections -  a few types
from collections import Counter
a ="aaaabbbcccc"
my_counter = Counter(a) #sorted in descending count
print(my_counter) # .items() .keys() .values() -dictionary

print(my_counter.most_common(2)) #tuples output
print(my_counter.most_common(1)[0])
print(my_counter.most_common(1)[0][0])

print(list(my_counter.elements())) #list elements

from collections import namedtuple
Point = namedtuple('Point', 'x,y,z')
pt = Point([1,3,5], [2,4,6], 0)
print(pt)
print(pt.x, pt.y)

from collections import OrderedDict
oredered_dic = OrderedDict()
oredered_dic['d'] = 2
oredered_dic['b'] = 4
oredered_dic['c'] = 3
oredered_dic['a'] = 1
print(oredered_dic)

from collections import defaultdict
d = defaultdict(int) #list float
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['c']) #avoids key error

from collections import deque
d = deque()
d.append(1)
d.append(2)
print(d)
d.appendleft(3)
print(d)
print(d.pop()) #popleft() clear()
d.extend([4,5,6]) #extendleft()
print(d)
d.rotate(2) #move all +2 ahead (-2) for -2 ahead
print(d)

#itertools
from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b)
print(list(prod))

b=[3]
prod = product(a,b)
print(list(prod))
prod = product(a,b, repeat = 2)
print(list(prod))

from itertools import permutations
a = [1,2,3]
perm = permutations(a) #permutations(a,2{length/r})
print(list(perm))

from itertools import combinations, combinations_with_replacement
a = [1,2,3,4]
comb = combinations(a, 2) #no repetions
print(list(comb))

comb_wr = combinations_with_replacement(a,2) #with repeations
print(list(comb_wr))


from itertools import accumulate
a = [1,2,3,4]
acc = accumulate(a)
print(a)
print(list(acc)) #1 ,1+2, 1+2+3, 1+2+3+4

import operator
acc = accumulate(a, func=operator.mul) #multiply eac elem
print(list(acc))

a = [1,2,5,3,4,2]
acc = accumulate(a, func=max) #max
print(list(acc))

from itertools import groupby
a=[1,2,3,4]
def smaller_than_3(x):
    return x<3
group_obj = groupby(a, key=smaller_than_3) #splits/groups a list into two based on a condition
#group_obj = groupby(a, key=lambda x: x<3)
for key, value in group_obj:
    print(key, list(value))

persons = [{'name': 'tom', 'age': 25},{'name': 'dan', 'age': 25},
            {'name': 'dom', 'age': 26},{'name': 'dom', 'age': 27}]
group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))

from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if i==15:
        break
# a=[1,2,3]
# for i in cycle(a): #cycle a list until broken
#for i in repeat(1): #infinite 1 , reapeat(1,4) repeat 1 -> 4 times
#     print(i)

#lambda arguments: expression
print('-----')
add10 = lambda x: x +10
print(add10(5))

add10 = lambda x,y: x + y
print(add10(5, 5))

points2D = [(1,2),(15,1),(5,-1),(10,4)]
points2D_sorted = sorted(points2D) #normal sort by x
print(points2D_sorted)

points2D_sorted = sorted(points2D, key= lambda x: x[1]) #sort by y
print(points2D_sorted)

points2D_sorted = sorted(points2D, key= lambda x: x[0] + x[1]) #sort by sum of x & y
print(points2D_sorted)

#map map(fun, seq)
a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b))

#list comprehension
c = [x*2 for x in a]
print(c)

#filter (func{returns true/false }, sequ)
a = [1,2,3,4,5]
b = filter(lambda x: x%2==0, a)
print(list(b))

c= [x for x in a if x%2==0]
print(c)

#reduce (funx, seq)
from functools import reduce
product_a = reduce(lambda x,y: x*y, a)
print(product_a)

#errors and exceptions
#TypeError
#ModuleNotFoundError
#NameError
#FileNotFoundError
#ValueError
#IndexError
#KeyError

#x = -5
# if x < 0:
#     raise Exception('x is  < 0')

#assert(x>=0), 'x is not +ve'

try:
    a = 5/0 #ZeroDivisionError
except Exception as e:
    print('Error:', e)
else:
    print('else block1')
finally:
    print('finally block1')

try:
    a = 5/1 #no error
except Exception as e:
    print('Error:', e)
else:
    print('else block2')
finally:
    print('finally block2')

class ValueTooHighError(Exception):
    pass
class ValueTooSmallError(Exception):
    def __init__(self, msg, val):
        self.msg = msg
        self.val = val
def test_value(x):
    if x>100:
        raise ValueTooHighError('Value is too high')
    if x<5:
        raise ValueTooSmallError('value is too small', x)

try:
    test_value(1)
except ValueTooSmallError as e:
    print(e.msg, e.val)
except ValueTooHighError as e:
    print(e)

#logging
#import logging
#logging.basicConfig() --- docs
#.debug("msg") .info("msg") .warning("msg") .error("msg") .critical("msg")

#json
import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# convert into JSON:
person_json = json.dumps(person)
# use different formatting style
person_json2 = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True)

# the result is a JSON string:
print(person_json)
print(person_json2)

with open('person.json', 'w') as f:
    json.dump(person, f, indent=4)

#json to python object
person_json = """
{
    "age": 30,
    "city": "New York",
    "hasChildren": false,
    "name": "John",
    "titles": [
        "engineer",
        "programmer"
    ]
}
"""
person = json.loads(person_json) #loads 's'-string
print(person)

with open('person.json', 'r') as f:
    person = json.load(f)
    print(person)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)
#custom encoding to convert class object to json
def encode_user(o):
    if isinstance(o, User):
        return {'name' : o.name, 'age': o.age, o.__class__.__name__:True}
    else:
        raise TypeError('Object not of User Class')
userJSON = json.dumps(user, default=encode_user)
print(userJSON)

#another way
from json import JSONEncoder

class UserEncoder(JSONEncoder):
    def default(self,o):
        if isinstance(o, User):
            return {'name' : o.name, 'age': o.age, o.__class__.__name__:True}
        return JSONEncoder.default(self, o)

userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON)
#mirror2
userJSON = UserEncoder().encode(user)
print(userJSON) #now works with json.loads

#decode to class obj
def decode_user(dct):
    if User.__name__ in dct.keys():
        return User(name=dct['name'], age=dct['age'])
    return dct

user = json.loads(userJSON, object_hook=decode_user)
print(user.name)

#random numbers
import random
print(random.random())
print(random.uniform(1,10))
print(random.randint(1,10)) #10 included
print(random.randrange(1,10)) #10 not included
print(random.normalvariate(0,1)) #mean: 0 std deviation: 1

mylist = list("ABCDEFG")
print(random.choice(mylist))
print(random.sample(mylist,3)) #unique pick
print(random.choices(mylist,k=3)) #pick multiple times
random.shuffle(mylist)
print(mylist)

random.seed(1)
print(random.random())
random.seed(2)
print(random.random())
random.seed(1)
print(random.random())
random.seed(2)
print(random.random()) #reproducable

import secrets
print(secrets.randbelow(10))
print(secrets.randbits(4)) #1111 => upto 15
print(secrets.choice(mylist))

import numpy as np
print(np.random.rand(3,3))
print(np.random.randint(0, 10, 3)) #(range, range, size/(4,5))
arr = np.array([[0.52114419,0.24465269, 0.34738849],[0.76800255, 0.35666828, 0.96722077],[0.5683974, 0.8907352, 0.57893705]])
np.random.shuffle(arr)
print(arr)
np.random.seed(1)
#reporducable
#decorators @
#fun & class decorators
    # @mydecorator
    # def dosomething():
    #     pass
import functools
def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator
def print_name():
    print('Alex')

# print_name = start_end_decorator(print_name)
# same as #start_end_decorator

print_name()

@start_end_decorator
def add5(x):
    return x+5

print(add5(10))
print(help(add5))
print(add5.__name__)

#repeating functions with decorators
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet('Alex')


#nested decorators
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        #print(args_repr) #prints args without key as list
        #print(kwargs_repr) #with key as list
        signature = ", ".join(args_repr + kwargs_repr)
        #print(signature) #creates the function arguments
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs) #calls function, this is main above is just for debug
        #this calls the start_end_decorator
        #func comes in with the next decorator
        print(f"{func.__name__!r} returned {result!r}")
            # !r - convert the value to a string using repr(). Means printable representation of the said object
            # !s - convert the value to a string using str().
            # These flags are placed before the format specifier:
            # "{0!r:20}".format("Hello")
        return result
    return wrapper

print('--------------')

@debug
@start_end_decorator
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

# now `debug` is executed first and calls `@start_end_decorator_4`, which then calls `say_hello`
print(say_hello('Alex'))

#class decorators
class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Times: {self.num_calls}")
        return self.func(*args, **kwargs) #if not returned, the func will not get excecuted
        #useful for debug, cache ,etc


@CountCalls
def say_hello():
    print('Say')
    return 'Hello'

print(say_hello())
print(say_hello())

#generators

def mygenerator():
    yield 1
    yield 3
    yield 2

g = mygenerator()
print(g)

for i in g:
    print(i)

g = mygenerator() #since affected by loop
print(next(g))
print(next(g))
print(next(g))
#print(next(g)) #stop iteration gets called
g = mygenerator()
print("Sum:",sum(g))
g = mygenerator()
print("Sum:",sorted(g))

def countdown(num):
    print('Starting...')
    while num>0:
        yield num
        num -=1
cd = countdown(4) #a list of 4, saves memory on large data

for i in cd:
    print(i)

#example
#faster than loop assignment and less bulky
# def firstn(n):
#     nums = []
#     num = 0
#     while num < n:
#         nums.append(num)
#         num += 1
#     return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sum(firstn_generator(10)))

#fibanocci with generator
def fibonacci(limit):
    # 0 1 1 2 3 5 8 13 21
    a,b = 0 , 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)
for i in fib:
    print(i)

#syntax for generator

mygenerator = (i for i in range(30) if i%2 == 0) #() creates a generator & [] creates list
for i in mygenerator:
    print(i)
#print(next(mygenerator)) #is a generator

#multi processing
from multiprocessing import Process
import os, time

processes = []
num_processes = os.cpu_count()
print(num_processes)

#create a fun to execute
def square_numbers(x):
    for i in range(50):
        i*i

#create a process
for i in range(num_processes):
    p = Process(target=square_numbers, args=[0])
    processes.append(p)

#start : on windows wrap inside the main module like this
if __name__ == '__main__':
    #start
    for p in processes:
        #p.start()
        pass

    #join #makes main thread wait
    for p in processes:
        #p.join()
        pass

    print('end main 1') #executed only once
print('end main') #gets printed out twice as the execution continues from the point of start

#multi threading similar to process
from threading import Thread

threads = []
num_threads = 10

#create threads
for i in range(num_threads):
    t = Thread(target=square_numbers, args=[0])
    threads.append(t)

#start : on windows wrap inside the main module like this
if __name__ == '__main__':
    #start
    for t in threads:
        #t.start()
        pass

    #join #makes main thread wait
    for t in threads:
        #t.join()
        pass

    print('end main thread 1')
print('end main thread')

#threading: sharing data possible: local data update
from threading import Lock
database_value = 0

def increase(lock):
    global database_value

    # # lock the state
    # lock.acquire()

    # local_cpy = database_value
    # local_cpy += 1
    # time.sleep(0.1) #other thread becomes active at this time

    # database_value = local_cpy
    # lock.release() #always release

    #or in easy way using context manager
    with lock:
        local_cpy = database_value
        local_cpy += 1
        time.sleep(0.1) #other thread becomes active at this time

        database_value = local_cpy


if __name__ == '__main__':

    lock = Lock() #initiate lock
    print('Start value', database_value)

    thread1 = Thread(target=increase, args=(lock,)) # , tuple with just one elemetn
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value:', database_value) #outputs 1 on test 1 without lock
    print('end main')

#queue in threading
from queue import Queue


# if __name__ == '__main__':
#     q = Queue()

#     q.put(1)
#     q.put(2)
#     q.put(3)

#     #q.empty() true/false
#     #q.task_done() call always
#     first = q.get()
#     print(first)

#     q.task_done()
#     #q.join() blocks main thread
#     print('end main')
from threading import current_thread
def worker(q, lock):
    while True:
        value = q.get()
        with lock: #to avoid 2 threads accesing data at same time
            print(f'in {current_thread().name} got {value}')
        q.task_done()

if __name__ == '__main__':
    q = Queue()
    lock = Lock()

    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        #to kill thread loops running without main thread
        thread.deamon = True #background thread that dies when main dies
        thread.start()

    for i in range(1, 21):
        q.put(i)

    q.join()

    print('end main')

#processes
#from multiprocessing import Process, Value, Array
from multiprocessing import Value, Array

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

    # p1 = Process(target=add_100, args=(shared_number, lock1))
    # p2 = Process(target=add_100, args=(shared_number, lock1))

#commented out as too many processes, runs fine as self {test_proccess.py}
    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    print('number at end:', shared_number.value) #race condition as common var read write
#can be done with queue as well
def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(i*-1)

if __name__ == "__main__":

    numbers = range(1, 6)
    q = Queue()
#commented out as too many processes, runs fine as self {test_proccess.py}

    # p1 = Process(target=square, args=(numbers,q))
    # p2 = Process(target=make_negative, args=(numbers,q))

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    # order might not be sequential
    while not q.empty():
        print(q.get())

    print('end main')

# from multiprocessing import Pool

# def cube(number):
#     return number * number * number


# if __name__ == "__main__":
#     numbers = range(10)

#     p = Pool()

#     # by default this allocates the maximum number of available
#     # processors for this task --> os.cpu_count()
#     result = p.map(cube,  numbers)

#     # or
#     # result = [p.apply(cube, args=(i,)) for i in numbers]

#     p.close()
#     p.join()

#     print(result)

#funcs

def foo(a, b, *args, **kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1,2,3,4,5, six=6, seven=7)

def foo2(a, b, *, c, d):
    print(a,b, c, d)

foo2(1,2,c=3,d=4) #after args must be key call

def foo3(a,b,c):
    print(a,b,c)

my_list = [0,1,2]
foo3(*my_list)
foo3(**{'a': 1, 'b': 2, 'c':3})

#fun can access global variable but not modify without global call

#mutable obj like lists gets modified(append, +=) when passed to function
#rebinding like reinitiatinfg the variable removes this connection

print([0, 1] * 10)
print((0, 1) * 10)
print('AB' * 10)

numbers = [1,2,3,4,5,6]

*begining, last = numbers #* can be at any position
print(begining, last)

my_tuple = (1,2,3)
my_list = [4,5,6]

new_list = [*my_tuple, *my_list] #merges lists, tuples, sets and more
#for dict use ** due to keys
print(new_list)

#shallow vs deep
#copying
#list,class,.. direct assignment leads to pointing to the same location
#shallow copy - one lvl deep, copys until 1 level then refers the original location
#deep - full copy
#import copy
#.copy()
#list()
#var = copy.copy([]) - shallow copy
#copy.deepcopy([])

#context managers ############
# with open('notes2344.txt', 'w') as file:
#     file.write('some todooo...')

#simplifies this
# file = open('notes2344.txt', 'w')
# try:
#     file.write('some todooo...')
# finally:
#     file.close()

#class as context manager with __enter__ and __exit__
# class ManagedFile:
#     def __init__(self, filename):
#         print('init', filename)
#         self.filename = filename

#     def __enter__(self):
#         print('enter')
#         self.file = open(self.filename, 'w')
#         return self.file

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         if self.file:
#             self.file.close()
#         print('exc:', exc_type, exc_value)
#         if exc_type is not None:
#             print('Exception has been handled')
#         print('exit')
#         return True

# # No exception
# with ManagedFile('notes1233455654.txt') as f:
#     print('doing stuff...')
#     f.write('some todo...')
# print('continuing...')

# print()

# # Exception is raised, but the file can still be closed
# with ManagedFile('notes1233455654.txt') as f:
#     print('doing stuff...')
#     f.write('some todo...')
#     f.do_something()
# print('continuing...')

#function as context manager
from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f #temporary suspension and after this operation is done, file gets closed as what generators does
    finally:
        f.close()

with open_managed_file('notes3342.txt') as f:
    f.write('some todos...')









