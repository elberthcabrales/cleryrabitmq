from proj.celery import app
#from django.shortcuts import render
from djcelery import celery

@app.task
def hello_world():
    print('Hello World')

@app.task
def calculo():
   j = 1
   for i in xrange(100000):
       if j % 2 and i:
           j *= i
       else:
           j += i
   print j
