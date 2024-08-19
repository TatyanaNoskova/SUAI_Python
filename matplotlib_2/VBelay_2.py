import matplotlib.pyplot as plt
import numpy as np
import math 
import sympy as sym
#задание №1
def grafiki_avstralia():#Австралия и Океания
    
    continents=['Avstralya','New_Gvinea','New_Zeland','Fidji','Solom_islands' ]
    av=[22507]
    n_gv=[6552]
    n_zel=[4402]
    fid=[903]
    sol=[610]
    colors=['blue','yellow','#DC143C','#00FFFF', 'green', '#6A5ACD']
    index=np.arange(5)
    step=0.3# размещение графиков относительно друг друга
    figure = plt.figure(frameon=True,edgecolor='#6A5ACD', dpi = 90)
    explode1 = [0.05,0,0,0,0]
    ex1 = figure.add_subplot(1,2,1,title='Австралия и Океания')
    ex2 = figure.add_subplot(1,2,2, title='Австралия и Океания')# создаем 2 фигур для размещения графиков, 1 ряда, 2 колонки, далее номер фигуры по порядку
  
    ex1.axis([0,5,0,25000])#деление по оси ОУ
  
    ex1.bar(index+step,av,step,color='blue',label='Avstralya' )#гистограмма для населения Австралии
    ex1.bar(index+step*1.5,n_gv,step,color='yellow',label='New_Gvinea') #гистограмма для населения Новой Гвинеи
    ex1.bar(index+step*2,n_zel,step,color='#DC143C',label='New_Zeland') #гистограмма для населения Новой зеландии
    ex1.bar(index+step*2.5,fid,step,color='#00FFFF',label='Fidji') #гистограмма для населения Фиджи
    ex1.bar(index+step*3,sol,step,color='green',label='Solom_islands') #гистограмма для населения Соломоновы Острова
    ex1.legend(loc='upper right', fontsize=10)# легенда на грфике

    ex2.pie([av[0],n_gv[0],n_zel[0],fid[0],sol[0]],labels=continents,explode = explode1,colors=colors,startangle=180, autopct="%2.2f%%",shadow = True )
    
    plt.show()
grafiki_avstralia()   

def grafiki_northern_states():
    continents=['USA','Mexico','Kanada','Guatemala','Cuba' ]
    usa=[321.2]
    mex=[121]
    kan=[35.8]
    guat=[16.1]
    kub=[11.2]
    colors=['blue','#008000','#DC143C', '#B0E0E6', '#FF0000']
    index=np.arange(5)
    step=0.3
    figure = plt.figure(frameon=True,edgecolor='#6A5ACD', dpi = 90)
    explode1 = [0.05,0,0,0,0]
    ex1 = figure.add_subplot(1,2,1,title='Северная Америка')
    ex2 = figure.add_subplot(1,2,2, title='Северная Америка')# создаем 2 фигур для размещения графиков, 1 ряда, 2 колонки, далее номер фигуры по порядку
  
    ex1.axis([0,5,0,350])#деление по оси ОУ
  
    ex1.bar(index+step,usa,step,color='blue',label='USA' )#гистограмма для населения Америки
    ex1.bar(index+step*1.5,mex,step,color='#008000',label='Mexico') #гистограмма для населения Мексика
    ex1.bar(index+step*2,kan,step,color='#DC143C',label='Kanada') #гистограмма для населения Канада
    ex1.bar(index+step*2.5,guat,step,color='#B0E0E6',label='Guatemala') #гистограмма для населения Гватемала
    ex1.bar(index+step*3,kub,step,color='#FF0000',label='Cuba') #гистограмма для населения Куба
    ex1.legend(loc='upper right', fontsize=10)# легенда на грфике

    ex2.pie([usa[0],mex[0],kan[0],guat[0],kub[0]],labels=continents,explode = explode1,colors=colors,startangle=180, autopct="%2.2f%%",shadow = True )
    
    plt.show()

#grafiki_northern_states()

def grafiki_south_america():
    continents=['Brazil','Colombia','Argentina','Venezuela','Peru' ]
    br=[207.3]
    col=[47.7]
    arg=[44.3]
    ven=[31.3]
    per=[31]
    colors=['#228B22','#FFFF00','#4682B4', '#0000FF', '#B22222']
    index=np.arange(5)
    step=0.3
    figure = plt.figure(frameon=True,edgecolor='#6A5ACD', dpi = 90)
    explode1 = [0.05,0,0,0,0]
    ex1 = figure.add_subplot(1,2,1,title='Южная Америка')
    ex2 = figure.add_subplot(1,2,2, title='Южная Америка')# создаем 2 фигур для размещения графиков, 1 ряда, 2 колонки, далее номер фигуры по порядку
  
    ex1.axis([0,5,0,225])#деление по оси ОУ
  
    ex1.bar(index+step,br,step,color='#228B22',label='Brazil' )#гистограмма для населения Америки
    ex1.bar(index+step*1.5,col,step,color='#FFFF00',label='Colombia') #гистограмма для населения Мексика
    ex1.bar(index+step*2,arg,step,color='#4682B4',label='Argentina') #гистограмма для населения Канада
    ex1.bar(index+step*2.5,ven,step,color='#0000FF',label='Venezuela') #гистограмма для населения Гватемала
    ex1.bar(index+step*3,per,step,color='#B22222',label='Peru') #гистограмма для населения Куба
    ex1.legend(loc='upper right', fontsize=10)# легенда на грфике

    ex2.pie([br[0],col[0],arg[0],ven[0],per[0]],labels=continents,explode = explode1,colors=colors,startangle=180, autopct="%2.2f%%",shadow = True )
    
    plt.show()
#grafiki_south_america()

def grafiki_afrika():#Африка
    continents=['Nigeria','Egypet','Ethiopia','Congo','Tanzania' ]
    nig=[194.0]
    egip=[90.0]
    eth=[89.0]
    con=[77.0]
    tan=[56.0]
    colors=['#00FF7F','red','#FFFF00', '#9ACD32', '#20B2AA']
    index=np.arange(5)
    step=0.3
    figure = plt.figure(frameon=True,edgecolor='#6A5ACD', dpi = 90)
    explode1 = [0.05,0,0,0,0]
    ex1 = figure.add_subplot(1,2,1,title='АФрика')
    ex2 = figure.add_subplot(1,2,2, title='Африка')# создаем 2 фигур для размещения графиков, 1 ряда, 2 колонки, далее номер фигуры по порядку
  
    ex1.axis([0,5,0,200])#деление по оси ОУ
  
    ex1.bar(index+step,nig,step,color='#00FF7F',label='Nigeria' )#гистограмма для населения Нигерии
    ex1.bar(index+step*1.5,egip,step,color='red',label='Egypet') #гистограмма для населения Египта
    ex1.bar(index+step*2,eth,step,color='#FFFF00',label='Ethiopia') #гистограмма для населения Эфиопии
    ex1.bar(index+step*2.5,con,step,color='#9ACD32',label='Congo') #гистограмма для населения Конго
    ex1.bar(index+step*3,tan,step,color='#20B2AA',label='Tanzania') #гистограмма для населения Танзания
    ex1.legend(loc='upper right', fontsize=10)# легенда на грфике

    ex2.pie([nig[0],egip[0],eth[0],con[0],tan[0]],labels=continents,explode = explode1,colors=colors,startangle=180, autopct="%2.2f%%",shadow = True )
    
    plt.show()


#grafiki_afrika()

def grafiki_azia():#Азия
    continents=['China','India','Indonesia','Pakistan','Bangladesh' ]
    ch=[1410.0]
    ind=[1268.0]
    indon=[255.0]
    pak=[196.0]
    ban=[160.0]
    colors=['#8B0000','#FF4500','#FFE4B5', '#006400', '#00FF7F']
    index=np.arange(5)
    step=0.3
    figure = plt.figure(frameon=True,edgecolor='#6A5ACD', dpi = 90)
    explode1 = [0.05,0,0,0,0]
    ex1 = figure.add_subplot(1,2,1,title='Азия')
    ex2 = figure.add_subplot(1,2,2, title='Азия')# создаем 2 фигур для размещения графиков, 1 ряда, 2 колонки, далее номер фигуры по порядку
  
    ex1.axis([0,5,0,1600])#деление по оси ОУ
  
    ex1.bar(index+step,ch,step,color='#8B0000',label='China' )#гистограмма для населения Америки
    ex1.bar(index+step*1.5,ind,step,color='#FF4500',label='India') #гистограмма для населения Мексика
    ex1.bar(index+step*2,indon,step,color='#FFE4B5',label='Indonesia') #гистограмма для населения Канада
    ex1.bar(index+step*2.5,pak,step,color='#006400',label='Pakistan') #гистограмма для населения Гватемала
    ex1.bar(index+step*3,ban,step,color='#00FF7F',label='Bangladesh') #гистограмма для населения Куба
    ex1.legend(loc='upper right', fontsize=10)# легенда на грфике

    ex2.pie([ch[0],ind[0],indon[0],pak[0],ban[0]],labels=continents,explode = explode1,colors=colors,startangle=180, autopct="%2.2f%%",shadow = True )
    
    plt.show()
#grafiki_azia()
def grafiki_europe():#Европа
    continents=['Germany','France','England','Italy','Spain' ]
    ger=[84.7]
    fr=[68.14]
    en=[67.79]
    it=[59.0]
    sp=[48.59]
    colors=['#FFD700','#0000CD','#B22222', '#32CD32', '#FF4500']
    index=np.arange(5)
    step=0.3
    figure = plt.figure(frameon=True,edgecolor='#6A5ACD', dpi = 90)
    explode1 = [0.05,0,0,0,0]
    ex1 = figure.add_subplot(1,2,1,title='Азия')
    ex2 = figure.add_subplot(1,2,2, title='Азия')# создаем 2 фигур для размещения графиков, 1 ряда, 2 колонки, далее номер фигуры по порядку
  
    ex1.axis([0,5,0,101])#деление по оси ОУ
  
    ex1.bar(index+step,ger,step,color='#FFD700',label='Germany' )#гистограмма для населения Америки
    ex1.bar(index+step*1.5,fr,step,color='#0000CD',label='France') #гистограмма для населения Мексика
    ex1.bar(index+step*2,en,step,color='#B22222',label='England') #гистограмма для населения Канада
    ex1.bar(index+step*2.5,it,step,color='#32CD32',label='Italy') #гистограмма для населения Гватемала
    ex1.bar(index+step*3,sp,step,color='#FF4500',label='Spain') #гистограмма для населения Куба
    ex1.legend(loc='upper right', fontsize=10)# легенда на грфике

    ex2.pie([ger[0],fr[0],en[0],it[0],sp[0]],labels=continents,explode = explode1,colors=colors,startangle=180, autopct="%2.2f%%",shadow = True )
    
    plt.show()
#grafiki_europe()

#задание №2

def grafiki_region():#Общий
    continents=['Australia','North America','South America','Africa','Asia','Europe' ]
    av=[23]
    nor=[321.2]
    s=[207.3]
    af=[194]
    asi=[1410]
    eur=[84.7]

    colors=['#20B2AA','#8B0000','#008000', '#00FF7F', '#FF0000','#FFA500']
    index=np.arange(6)
    step=0.3
    figure = plt.figure()
    explode1 = [0.05,0.05,0.05,0.05,0.05,0.05]
    #fig = plt.figure(frameon=True,edgecolor='#6A5ACD',dpi = 100)
    ex1 = figure.add_subplot(1,2,1,title='Регионы')
    ex2 = figure.add_subplot(1,2,2, title='Регионы')# создаем 2 фигур для размещения графиков, 1 ряда, 2 колонки, далее номер фигуры по порядку
  
    ex1.axis([0,6,0,1600])#деление по оси ОУ
  
    ex1.bar(index+step,av,step,color='#20B2AA',label='Australia' )#гистограмма для населения Австралии
    ex1.bar(index+step*1.5,nor,step,color='#8B0000',label='North America') #гистограмма для населения Северной Америки
    ex1.bar(index+step*2,s,step,color='#008000',label='South America') #гистограмма для населения Южной Америки
    ex1.bar(index+step*2.5,af,step,color='#00FF7F',label='Africa') #гистограмма для населения Африка
    ex1.bar(index+step*3,asi,step,color='#FF0000',label='Asia') #гистограмма для населения Азия
    ex1.bar(index+step*3,eur,step,color='#FFA500',label='Europe') #гистограмма для населения Европа

    ex1.legend(loc='upper right', fontsize=10)# легенда на грфике

    ex2.pie([av[0],nor[0],s[0],af[0],asi[0],eur[0]],labels=continents,explode = explode1,colors=colors,startangle=180, autopct="%2.2f%%",shadow = True )
    
    plt.show()
#grafiki_region()
