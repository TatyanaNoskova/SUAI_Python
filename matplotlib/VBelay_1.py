import matplotlib.pyplot as plt
import numpy as np
import math 
import sympy as sym
#задание №1
def grafiki1():
    #создание графика
    fig, ax = plt.subplots()
    x1= [-4,-3,-2,-1,0,1,2,3,4]#координаты графика считала в ручном режиме
    y1 = [9,4,1,0,1,4,9,16,25]#координаты графика считала в ручном режиме
    x2 = [-4,-3,-2,-1,0,1,2,3,4]#координаты графика считала в ручном режиме
    y2 = [18,10.5,5,1.5,0,0.5,3,7.5,14]  #координаты графика считала в ручном режиме
    x3 = [-4,-3,-2,-1,0,1,2,3,4]#координаты графика считала в ручном режиме
    y3 = [-0.6,1.4,3.4,5.4,7.4,9.4,11.4,13.4,15.4]#координаты графика считала в ручном режиме

    ax.plot(x1,y1,color='yellow',alpha=0.45,marker='o', label='График ф.  y(x)=x^2+2x+1')#Цвет графика, прозрачность, маркер, легенда на фигуре
    ax.plot(x2,y2,color=(1,0.14,0.57),alpha=0.7,marker='o',label='График ф.  y(x)=-x^2-0.5x')#Цвет графика, прозрачность, маркер, легенда на фигуре
    ax.plot(x3,y3,color='#7CFC00',alpha=0.95,marker='o',label='График ф.  у(x)=e^x+2x')#Цвет графика, прозрачность, маркер, легенда на фигуре
    ax.set_title("Задание №1 Носкова Т.О.", fontsize=18,color ='#7CFC00',loc='left',fontstyle='italic')
    ax.legend(loc='lower right')#легенда в правом нижнем углу
    ax.legend(loc='lower right')
    ax.set_xlim(-10,10) #лимит по оси x для графиков 
    ax.set_ylim(-10,10) #лимит по оси у для графиков        
    plt.show()

#grafiki1()  
#Задание № 2
def grafiki2():
    figure = plt.figure()
    x1= [-4,-3,-2,-1,0,1,2,3,4]
    y1 = [9,4,1,0,1,4,9,16,25 ]
    x2 = [-4,-3,-2,-1,0,1,2,3,4]
    y2 = [18,10.5,5,1.5,0,0.5,3,7.5,14]  
    x3 = [-4,-3,-2,-1,0,1,2,3,4]
    y3 = [-0.6,1.4,3.4,5.4,7.4,9.4,11.4,13.4,15.4]
    x4=[x for x in range(-4,5,1)]
    y4=[0.000336,0.00248,0.018323,0.135363,1,7.387524,54.57551,403.1779,2978.486]    
    x5= [-4,-3,-2,-1,0,1,2,3,4]
    y5 = [math.sin(x) for x in range(-4,5,1)]
    x6= [-4,-3,-2,-1,0,1,2,3,4]
    y6 = [math.cos(3*y) for y in range(-4,5,1)]
    x7= [0,1,2,3,4,5,6,7,8]
    y7 = [np.log2(x) for x in range(0,9,1)]
    x8= [0,1,2,3,4,5,6,7,8]
    y8 = [np.log(math.pi*x) for x in range(0,9,1)]

    ex1 = figure.add_subplot(3,2,1)# создаем пять фигур для размещения графиков, 3 ряда, 2 колонки, далее номер фигуры по порядку
    ex2 = figure.add_subplot(3,2,2)
    ex3 = figure.add_subplot(3,2,3)
    ex4 = figure.add_subplot(3,2,4)
    ex5 = figure.add_subplot(3,2,5)
    ex6 = figure.add_subplot(3,2,6)
    ex1.set_title("Все графики", fontsize=9,color ='#000000',loc='left',fontstyle='italic') #Название фигуры № 1   
    ex1.plot(x1,y1,color='#00FFFF',marker='o', label='График ф.  y(x)=x^2+2x+1')# размещение всех графиков на фигуре № 1
    ex1.plot(x2,y2,color='#000080',marker='o', label='График ф.  y(x)=-x^2-0.5x')
    ex1.plot(x3,y3,color='#A52A2A',marker='o', label='График ф.  у(x)=e^x+2x')    
    ex1.plot(x4,y4,color='#A52A2A',marker='o', label='График ф.  y(x)=e^(-2x)')  
    ex1.plot(x5,y5,color='#FF0000',marker='o', label='График ф.  y(x)=sin(x)#')
    ex1.plot(x6,y6,color='#FF1493',marker='o', label='График ф.  у(x)=cos(3x)')    
    ex1.plot(x7,y7,color='Yellow',marker='o', label='График ф.  y(x)=log2(x)')
    ex1.plot(x8,y8,color='#00FF7F',marker='o', label='График ф.  y(x)=ln(pi*x)')
    ex1.legend(loc='lower right', fontsize=5)


    ex2.plot(x1,y1,color='#00FFFF',marker='o', linewidth=1,label='График ф.  y(x)=x^2+2x+1')# размещение линейных графиков на фигуре № 2
    ex2.plot(x2,y2,color='#00FFFF', alpha=0.5, marker='o', linewidth=1,label='График ф.  y(x)=-x^2-0.5x')# размещение линейных графиков на фигуре № 2
    ex3.plot(x3,y3,color='#A52A2A',marker='o', label='График ф.  у(x)=e^x+2x') # размещение экспоненциальные  графиков на фигуре № 3 
    ex3.plot(x4,y4,color='#A52A2A',alpha=0.5,marker='o', label='График ф.  y(x)=e^(-2x)')# размещение экспоненциальные  графиков на фигуре № 3     
    ex4.plot(x5,y5,color='#FF0000',marker='o', label='График ф.  y(x)=sin(x)#')# размещение тригонометрических графиков на фигуре № 4
    ex4.plot(x6,y6,color='#FF0000',alpha=0.5,marker='o', label='График ф.  у(x)=cos(3x)') # размещение тригонометрических графиков на фигуре № 4
    ex5.plot(x7,y7,color='Yellow',marker='o', label='График ф.  y(x)=log2(x)')# размещение логарифмических графиков на фигуре № 5
    ex5.plot(x8,y8,color='Yellow',alpha=0.5,marker='o', label='График ф.  y(x)=ln(pi*x)')# размещение логарифмических графиков на фигуре № 5         
    plt.show()
 #grafiki2()
#Задание №3
def cx7(func):# функцию для вывода графика применила в качестве декоратора
    def cx8():
        s=func()
        fig, ax = plt.subplots()
        x1= s
        y1 =[len(x1) for x1 in s]
        ax.plot(x1,y1,color=(1,0.14,0.57),marker='o',label='График')    
    
        plt.show()
    return cx8  

#cx7()
@cx7
def cx18():
    a=input('Введите предложение в формате: xxxxx, xxxxx!: ')
    a=a.replace('!', ', !')
    a=a.split()  
           
    return a
#print(cx18())
