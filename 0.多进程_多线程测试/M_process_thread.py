# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'
 
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import freeze_support
 
import urllib2
 
urls = [
  'http://www.python.org',
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
  'http://planet.python.org/',
  'https://wiki.python.org/moin/LocalUserGroups',
  'http://www.python.org/psf/',
  'http://docs.python.org/devguide/',
  'http://www.python.org/community/awards/'
  ]
 
 
import time
 
def w1(func):
    def inner(*args,**kwargs):
        past = time.time()
        func(*args,**kwargs)
        now = time.time()
        cost_time = now - past
        print "The function <%s> cost time: <%s>"%(func.func_name,cost_time)
    return inner
 
 
def test(n):
    print len(urllib2.urlopen(n).read())
 
ppool = Pool(4)
@w1
def MulProcess():
    for n in urls:
        ppool.apply(func=test,args=(n,))
    ppool.close()
    ppool.join()
MulProcess()
tpool = ThreadPool(4)
@w1
def MulThreading():
    for n in urls:
        tpool.apply(func=test,args=(n,))
    tpool.close()
    tpool.join()
MulThreading()