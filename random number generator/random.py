
import random

def randommaker(x,a,c,m):
    x=((a*x)+c)%m
    return x;

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

flag=x=random.choice(list1)
a=17
c=43
m=100

n = input("how many random numbers you want to show :: ")
for i in range(0,int(n)):
    x = randommaker(x,a,c,m)
    r = x/100
    print(r ," ",end=" ")
    if(flag==x):
        flag=x=x+1
