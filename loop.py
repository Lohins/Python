#!/usr/bin/env python
# -*- coding:utf-8 -*-

# circlr.py

def addSum(x,y):
	return x+y

def showMeg(name , gender , age = 8):	
	print name , gender , age

def add_end(l = None):
	if l is None:
		l = []
	l.append('end')
	return l

def calc(*nums):
	sum = 0
	for x in nums:
		sum  = sum + x
	return sum
def person(name , age , **kw):
	print name, age, kw
@tail_call_optimized
def fact(n):
    return fact_tail(1,1,n)

def fact_tail(product , index , n):
	if index > n:
		return product
	return fact_tail(product * index , index + 1 , n)


print(fact(10))

person('das',12)
person('sitong',  56 , **{'s':12 , 'asd':43})

print calc(1,2,3)
print calc(*[1,2,5])

print(add_end())
print(add_end())
print(add_end())
print(add_end([1,2,3]))
list = (1,2,3,'sitong')

for name in list:
	print name

n = 0
for x in xrange(1,10):
	n = addSum(x,n)
print n

showMeg( 'sitong' , '男')
showMeg( 'houqi' , '男', 78)

