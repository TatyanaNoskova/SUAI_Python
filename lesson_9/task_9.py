import math
#Первый способ решения задания с помощью конструкции try-except
def calculate_square_root(num):
        
        try:                                
            num = math.sqrt(num)
            print(num)
        except:
            print('ValueError:  «Невозможно извлечь квадратный корень из отрицательного числа')
            return


#Второй способ решения задания с помощью условия if

def calculate_square_root_1(num):
     if num<0:
          print('ValueError:  «Невозможно извлечь квадратный корень из отрицательного числа')
          return 'Вывод: ', 0
     return math.sqrt(num)



#Задание №3



class InvalidOperationError(Exception):#создала класс
    pass
   
def check_value(m): #Эта функция проверяет ввод операции пользователем
    
    if m!='+' and m!='-' and m!='/' and m != '*':
        raise InvalidOperationError(f'Проверка  не пройдена, значение {m} не корректное')         
    
    else:
        print(f"Проверка пройдена, значение {m} корректное")

# try:
#     user_val = (input("Введите значение для проверки: "))
#     check_value(user_val)
# except InvalidOperationError as error:
#     print(error)
#     print(f"Знак {user_val} не корректное")  


def cx_5 ():
    try:
         
        a = ((input("Введите любой знак +, -, * , / :  \n")))  
        check_value(a)         
          
        b = int(input("Введите число : \t"))          
        c = int(input("Введите число : \t"))
    
        if a == '+':
            
            s1 = b + c
            print(s1)
        elif a == '-':
            s2 = b - c
            print(s2)
        elif a == '/':
            s3 = b / c
            print(s3)
        elif a == '*':
            s4 = b * c
            print(s4)       
       
    except ZeroDivisionError as error:
        print("Ошибка деления на ноль:", error)
    except ValueError as error:
        print("Ошибка значения:", error)
    except TypeError as error:
        print("Ошибка несоответствующего типа:", error)
    except InvalidOperationError as  error:
        print('Ошибка воода операции: ', error)   
  
    
cx_5()   #Запуск функции


