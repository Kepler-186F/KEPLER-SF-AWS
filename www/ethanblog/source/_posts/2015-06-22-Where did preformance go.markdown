---
layout: post
title: "Where did preformance go? Dive into multi-process/multi-threads in CPython"
date: 2015-06-22 15:31:14 -0500
comments: true
categories:
---
I've been run in to this kind of problem recently: one day I found out a solution written in python multi-thread approach take more running time than single thread. This is really confusing. I decided to dive into that...and some interesting stuff were found out.

Note that my computer is multi-core processor cpu. i7 2.3Ghz QuardCore CPU, 16G DDR3 Memory. With SSD Hard Drive.

Essentially every thing starts from this little piece of code recursively solving a permutation problem



```
#!/usr/bin/python
import datetime


L = [1,2,3,4,5,7,8,9,10,11]

def gen(index,value):
	if index==len(L):
		return 1
	count=0
	for i in range(len(value)+1):
		count+=gen(index+1,value[:i]+[L[index]]+value[i:])
	return count
```


Below are how it was wroted in single thread, multi-thread and multi-process. Along with the running time.
```

#Single thread approach
#time0=datetime.datetime.now()
#print gen(1,[1]) #runtime 480ms-10   4500ms-11  50sec-12 11>>>>>0:00:04.823974
#time1=datetime.datetime.now()
#print time1-time0



pointer1=0
pointer2=0
def t1_start():
	global pointer1
	pointer1=gen(2,[2,1])
	print pointer1

def t2_start():
	global pointer2
	pointer2=gen(2,[1,2])
	print pointer2


#from threading import Thread
#t1=Thread(target=t1_start,args=())
#t2=Thread(target=t2_start,args=())
#time0=datetime.datetime.now()
#t1.start()
#t2.start()
#t1.join()
#t2.join()
#time1=datetime.datetime.now()
#print pointer1+pointer2,time1-time0 #runtime 650ms-10  6392ms-11 72sec -12 11>>>>>>>0:00:05.082194



import multiprocessing
p1=multiprocessing.Process(target=t1_start,args=())
p2=multiprocessing.Process(target=t2_start,args=())
time0=datetime.datetime.now()
p1.start()
p2.start()
p1.join()
p2.join()
time1=datetime.datetime.now()
print pointer1+pointer2,time1-time0 #runtime 480ms-10 4400ms-11 48sec-12   >>>>>>>02.225561

#
#
```


Also, I simply increased the task from 10 digit array to 12 digit array, this takes roughly 1 min for the node to solve the problem. so the new result is this: single thread: 50 sec; multi-thread: 72 sec. I also tried implement it using multi-process. surprisingly multi-process cut the time in half. so the basically result is:


single thread  RUNTIME T
multi-thread   RUNTIME T
multi-process  RUNTIME T/2


This does not explain why there is no improvement from single thread to multi-threads. therefore I took a snapshot of CPU workload.
{% img /images/img/CPU_History.jpg %}




Note that even single thread it actually involves all my cpu cores. I'm now suspecting maybe CPython interpreter/optimizer or Intel CPU instruction set is pretty smart to handle even single thread solution to force it run on multiple CPUs.
