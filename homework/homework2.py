# Ansat
#1
# ismler=['lesson3.py','lesson4.py','lesson5.py']
# print(ismler[0])
# print(ismler[1])
# print(ismler[2])


#2
# a=list(range(1,11))
# print(a)
# a.remove(a[1])
# print(a)
# a.append('100')
# print(a)


#3
# a=['Nukus','Almati','Tashkent','Shimbay','Taqtakopir']
# print(sorted(a))



#Ortasha

#1
# sanlar=[]
# san=int(input("a:"))
# sanlar.append(san)
# san=int(input("a:"))
# sanlar.append(san)
# san=int(input("a:"))
# sanlar.append(san)
# san=int(input("a:"))
# sanlar.append(san)
# san=int(input("a:"))
# sanlar.append(san)

# sanlar_sum=sum(sanlar)
# print(sanlar_sum)

# orta_arifmetigi = sanlar_sum / len(sanlar)
# print(orta_arifmetigi)


#2
# a=['a','b','c','d','e','f','g','o']
# print(a)
# a.remove('a')
# a.remove('o')
# print(a)
# a.append('h')
# print(a)



#qiyinroq


#1
# a=[]
# b=int(input("b:"))
# a.append(b)
# b=int(input("b:"))
# a.append(b)
# b=int(input("b:"))
# a.append(b)
# b=int(input("b:"))
# a.append(b)
# b=int(input("b:"))
# a.append(b)
# b=int(input("b:"))
# a.append(b)
# b=int(input("b:"))
# a.append(b)
# b=int(input("b:"))
# a.append(b)
# b=int(input("b:"))
# a.append(b)
# b=int(input("b:"))
# a.append(b)
# print(a)


# taq=[]
# for i in a:
#     if i % 2 ==1:
#         taq.append(i)
# print(taq)
# jup=[]
# for i in a:
#     if i % 2 ==0:
#         taq.append(i)
# print(taq)


#2
# student=[]
# while(True):
#     a=input("a: ")
#     student.append(a)
#     if len(student) == 5:
#         break

# print(student)
# student.pop(2)
# print(student)




#Chelli

#1
# bahalar=[1500,1600,15000,10000,150000]
# print(max(bahalar))
# print(min(bahalar))


# for i in bahalar:
#     b= i / 100
#     print(f"{b * 10}")


#2
# list=[]
# while(True):
#     a=input("a: ")
#     list.append(a)
#     if len(list) == 5:
#         break
# print(list[0]+list[1]list[2]+list[3]+list[4])

import turtle
import math
import random
wn = turtle.Screen()
wn.bgcolor('black')
Albert = turtle.Turtle()
Albert.speed(0)
Albert.color('white')
rotate=int(360)
def drawCircles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
def drawSpecial(t,size,repeat):
  for i in range (repeat):
    drawCircles(t,size)
    t.right(360/repeat)
drawSpecial(Albert,100,10)
Steve = turtle.Turtle()
Steve.speed(0)
Steve.color('yellow')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Steve,100,10)
Barry = turtle.Turtle()
Barry.speed(0)
Barry.color('blue')
rotate=int(80)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-5
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Barry,100,10)
Terry = turtle.Turtle()
Terry.speed(0)
Terry.color('orange')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-19
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Terry,100,10)
Will = turtle.Turtle()
Will.speed(0)
Will.color('pink')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-20
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Will,100,10)