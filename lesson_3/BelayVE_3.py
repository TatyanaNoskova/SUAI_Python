import math# импорт библиотеки math для определения корня чисел
flag = True# переменной flag присвоили значение Истина
while flag:#Цикл while с условием flag = True, выполняет подсчет до тех пор пока условие flag равно истина

    var_1 = input("Введите любой знак +, -, * , / : , ** , // : \n") 
    """
          С помощью функции input воодим значение в консоли и присваивае значение переменной var_1
    """
    var_2 = 4#Переменной var_2 присвоили значение 4
    var_3 = 3#Переменной var_3 присвоили значение 3
    
    """
    С помощью кострукции условного оператора if-elif считаем значения переменной var_2 и var_3
    """

    if var_1 == '+':
        s1 = var_2 + var_3
        print(f"Сумма {var_2} + {var_3 } равна {s1}")
    elif var_1 == '-':
        s2 = var_2 - var_3
        s3 = var_3 - var_2
        print("Разность", var_2, '-', var_3 , 'равна', s2)
        print(f"Разность {var_3} - {var_2 } равна {s3}")        
    elif  var_1 == '/':
        s4 = var_2/var_3
        s5 = var_3/var_2
        
        print("Частное от деления", var_2, "на", var_3,"равно", s4)
        print(f"Частное от деления {var_3} на {var_2} равно {s5}")
        print("Частное от деления %i на %i равно %.2f" % (var_2, var_3, s4))
    elif var_1 == '*':
        s6 = var_2 * var_3
        print(f"Умножение {var_2} на {var_3} равно {s6}")
    elif var_1 == '**':
        s7 = var_2 ** var_3
        s8 = var_3**var_2
        print(var_2, "в степени", var_3, "равно",s7)
        print(f"{var_3} в степени {var_2} равно {s8}")
    elif var_1 == '//':
        print('Корень из',var_2, 'равен', math.sqrt(var_2))
        print('Корень из',var_3, 'равен', math.sqrt(var_3))    
    elif not var_1:# Вводим условие при котором цикл завершит работу, т.е, если var_1 это пустая строка, то цикл завершит работу
        flag = False# Если flag принимает значение ложь, цикл прекращает работу и выводит сообщение "Цикл прерван!"
            
print('Цикл прерван!')         
