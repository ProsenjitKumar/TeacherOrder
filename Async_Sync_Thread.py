# -------------------------- Synchronous, Multi Threading, Asynchronous ------------------------
'''
import time

def get_food(c_id):
   print("Customer %s's food is cooking...." % c_id)
   time.sleep(5)
   print("Customer %s's food is ready" % c_id)


def make_order(c_id):
   print("Customer %s's food is Ordering...." % c_id)
   get_food(c_id)


cust = 5

print("=====Starting time: " + str(time.ctime()))
for c in range(cust):
   make_order(c)

print("=====Ending time: " + str(time.ctime()))


# --------------------------- Multi Threading -----------------------------------

import time
from threading import Thread
import threading
def get_food(c_id):
   print("Customer %s's food is cooking...." % c_id)
   time.sleep(5)
   print("Customer %s's food is ready" % c_id)
   print("=======Ending time: " + str(time.ctime()))

def make_order(c_id):
   print("Running Thread: " + str(threading.current_thread().name))
   print("Customer %s's food is Ordering...." % c_id)
   get_food(c_id)

cust = 5

threads = []

print("=======Starting time: " + str(time.ctime()))

for c in range(cust):
   thread = Thread(target=make_order, args=(c,))
   thread.start()

   for t in threads:
       t.join()



# --------------------- Asynchronous ------------------------------

import time
import asyncio
import logging

logging.basicConfig(
        level=logging.INFO,
        format=' %(message)s: %(threadName)10s',
    )

async def get_food(c_id):
   logging.info("Running thread: ")
   print("Customer %s's food is cooking...." % c_id)
   await asyncio.sleep(5)
   print("Customer %s's food is ready" % c_id)


async def make_order(c_id):
   print("Customer %s's food is Ordering...." % c_id)
   await get_food(c_id)


cust = 5
tasks = []

for c in range(cust):
   tasks.append(make_order(c))

print("=======Starting time: " + str(time.ctime()))
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
print("=======Ending time: " + str(time.ctime()))
'''
# suppose a teacher order his 5 every single student to do something several thing
# but with same time. that means different tasks will do same time.
import asyncio
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(message)s: %(threadName)5s',
)

def add():
    x = 10
    y = 99
    p = x + y
    return print(p)

def sub():
    x = 125
    y = 99
    p = x - y
    return print(p)

def multi():
    x = 10
    y = 99
    p = x * y
    return print(p)

def divide():
    x = 1000
    y = 99
    p = x / y
    return print(p)


async def do_tasks(student_id):
  if student_id == 0:
      logging.info("Running Thread")
      print("Student %s's doing...." % student_id)
      await asyncio.sleep(7)
      add()
  elif student_id == 1:
      logging.info("Running Thread")
      print("Student %s's doing...." % student_id)
      await asyncio.sleep(7)
      multi()
  elif student_id == 2:
      logging.info("Running Thread")
      print("Student %s's doing...." % student_id)
      await asyncio.sleep(7)
      divide()
  elif student_id == 3:
      logging.info("Running Thread")
      print("Student %s's doing...." % student_id)
      await asyncio.sleep(7)
      sub()
  else:
      print("Something Went Wrong")


async def order_create(student_id):
    print("Teacher Ordering of %s Studendt" % student_id)
    await do_tasks(student_id)


students = 4
tasks = []

for student in range(students):
    tasks.append(order_create(student))

print("== == Starting Time: "+ str(time.ctime()))
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
print("== == Ending Time: " + str(time.ctime()))

