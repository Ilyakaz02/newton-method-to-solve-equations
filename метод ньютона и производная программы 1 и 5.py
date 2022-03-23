# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 20:53:05 2022

@author: 425
"""
#(sin x)/x^2 = a при а=1
#В моем уравнении корень находится в промежутке от 0 до 1
#при малых х левая часть функции будет эквивалентна 1/х, которая много больше 1 при малых х#
#при х, близких к 1, синус уже не может превосходить квадрат так как |sin|<1



import math
import numpy as np
def F(x,a):
    return np.sin(x)/math.pow(x,2)-a # описание функции
# а - это параметр, в моей задаче а = 1# 
 
#описание производной
def F1(x,a):
    return np.cos(x)/math.pow(x,2)-2*np.sin(x)/math.pow(x,3)


#b,c - границы рассматриваемого интервала#
def newton(a,b,c, delta): #описание метода ньютона в зависимости от границ отрезка
        x0=(c+b)/2
        xn=F(x0,a)
        xn1=xn-F(xn,a)/F1(xn,a) #xn1 это некст итерация
        while abs(xn1-xn)>delta: # 10^-5 необх точность
            xn=xn1
            xn1=xn-F(xn,a)/F1(xn,a)
        return xn1
def derivative_F(x,h,a):
    Fx=(F(x+h,a)-F(x-h,a))/(2*h)
    return (Fx)
           
print  ("Ответ:", newton(1,0,1,pow(10,-5)))    
print('Производная в а=1:', derivative_F(0.87672,0.0001,1))
print('Аналитически производная в а=1',F1(0.87672,1))      
