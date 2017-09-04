import threading
import random
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

device = MonkeyRunner.waitForConnection()

gl_continue = True

#Completly random boundaries
gl_minX = 1
gl_maxX = 1430

gl_minY = 600
gl_minY = 1300
gl_maxY = 2100

def do_n_touchs_fast(n):
  global gl_minX, gl_maxX, gl_minY, gl_maxY
  for i in range(n):
    device.touch(
      random.randint(gl_minX,gl_maxX),
      random.randint(gl_minY,gl_maxY),'DOWN_AND_UP')

# def create_and_launch_threads(threads_number,it_number):
#   l = [threading.Thread(target=do_n_touchs5,args=(it_number,)) for i in range(threads_number)]
#   for t in l:
#     try:
#       t.start()
#     except:
#       print "BBB"

def do_n_touchs(n):
  global gl_continue
  global gl_minX, gl_maxX, gl_minY, gl_maxY
  i=0
  while i < n and gl_continue:
    device.touch(
      random.randint(gl_minX,gl_maxX),
      random.randint(gl_minY,gl_maxY),'DOWN_AND_UP')
    i+=1

def do_n_touchs_endless():
  global gl_continue
  global gl_minX, gl_maxX, gl_minY, gl_maxY
  while gl_continue:
    device.touch(
      random.randint(gl_minX,gl_maxX),
      random.randint(gl_minY,gl_maxY),'DOWN_AND_UP')

def create_and_launch_threads(threads_number,it_number,fast=True,endless=False):
  if fast:
    l = [threading.Thread(target=do_n_touchs_fast,args=(it_number,)) for i in range(threads_number)]
  elif endless:
    l = [threading.Thread(target=do_n_touchs_endless) for i in range(threads_number)]
  else:
    l = [threading.Thread(target=do_n_touchs,args=(it_number,)) for i in range(threads_number)]
  for t in l:
    try:
      t.start()
    except:
      print "BBB"

