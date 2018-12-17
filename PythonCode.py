#Pythonexercises

#Exercise5

numberFound = 0
x = 11
while numberFound < 20:
    if x % 5 == 0 or x % 7 == 0 or x % 11 == 0:
        print(x)
        numberFound+=1
    x+=1

#Exercise6
#a
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True
#b
def is_prime(x):
    if (x > 1):
      divisor = 2
      for i in range(divisor,x):
           if (x % i) == 0:
               return False
    else:
        return False
    return True
#c
for num in range(2,101):
    if all(num % i!=0 for i in range(2,num)):
       print(num)
#d
r=int(input("Enter upper limit: "))
for a in range(2,r+1):
    k=0
    for i in range(2,a//2+1):
        if(a%i==0):
            k=k+1
    if(k<=0):
        print(a)
#this code allows you to enter the amount of values you want to be evaluated, the first n primes you want to see

#Exercise7
#a
mylist = [4, 76, 34, 2]
for element in mylist:
        print(element)
#b
mylist = ['78', '1', '90']
>>> for elem in mylist:
        mylist.reverse()
print(mylist)

#c
mylist = [1,2,3,4,5,6,7,8,9,12,3,34,45,6,7]
len(mylist)
#the len function returns 15, which is the amount of values within the list

#Exercise8
a = [1,2,3,4,5,6,7]
b=a
b[0] = 20
print(a[0]) #changing b[0] will also change a[0]
c = a[:]
c[2] = 20
print_list(a) #a was not updated after c was changed

def set_first_elem_to_zero(l):
	l[0] = 0
	return l
set_first_elem_to_zero(a)
print_list(a)

#Exercise9
def concat(A):
	l = []
	for each in A:
		l += each
	return l
print(concat([[7,8,9],[9,8,7],[8]]))

#Exercise10
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
a = np.arange(0.0, 2.0, 0.01)
b = (np.sin(a - 2) **2) * np.exp(-a **2)

fig, ax = plt.subplots()
ax.plot(a, b)

ax.set(xlabel='x', ylabel='y', title='Thats all, folks')
fig.savefig("test.png")
plt.show()

#Exercise11
def product_loop(l):
    p = 1
    for each in l:
        p *= each;
    return p

print(product_loop([4,5,6,7]))

def product_rec(l):
    if(len(l)==1):
        return l[0];
    else:
        return l[0]*product_rec(l[1:])

print(product_rec([4,5,6,7]))

#Exercise12
def fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(25))

#Exercise13
file  = open("emails.txt", "r")
print(re.search('[a-zA-Z]*@[a-zA-Z]*\.[a-zA-Z]*', 'asdfd@asfsd.afs'))
for line in file:
    match = re.search('[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+', line)
    print(match)
