# f = 3
# h = 4
# d = (f * h + 4)
# f1= (d + 1)
# print('итог:' + str (f1))


# text=('nurbolot')
# print (text[0:8])
# print(text[0:1])
# print(text[1:2])
# print(text[2:3])
# print(text[2:3])
# print(text[3:4])
# print(text[4:5])
# print(text[5:6])
# print(text[6:7])
# print(text[7:8])


# a = 80
# if a % 2 ==0:
#     print(a, 'четный')
# else:
#     print(a, 'не четный')


# if a % 3 ==0:
#     print(a, 'с остаток')
# else:
#     print(a, 'без остатка')

    
#     if a ** 2 > 1000:
#         print(a, 'большой')
#     else:
#         print(a, 'не большой')



# for ak in range(2):
#     print (ak)
#     for r in 'gama':
#         print(r)



# ak = {'nubolot'}
# ak . add ('otlichnik')
# print(ak)



# fox = ('baary')
# fox.ubdate('jakshy bolot')
# print(fox)


# tap = {'azamat', 'arystan', 'feruza','door'}
# kars ={'nurbolot', 'arystan', 'feruza','arman'}
# intersection=tap.intersection(kars)
# print(intersection)




# glasnye = {'a','i','o','u'}
# letter = input('ведите свой имя')
# limit = 1





# import sys

# rab = input ('введите свой имя:')
# fat1 =input ('введите свой фамилья:')
# ar2 = sys. getsizeof (rab)
# fat1 = sys. getsizeof (fat1)
# print(fat1, ar2)





# import random

# un = ('nurbolot', 'akmaral', 'jurok', 'temir')
# ta = random.choices (un, k = 4 ) 
# tat = []
# tat . append(ta)
# print(tat)




# file = open('tex.txt', encoding='utf-8')
# print(file.read())# это для копиравать текст на терминала 



# file = open('tex.txt', encoding='utf-8')
# s = file.readline()
# print(s)#  копируюет текст на терминала 


# user = []
# print ("write, your password:")
# name = input("name")
# password = input ("code")
# user [name] = password
# print(user)


# a = []
# for i in range(5):
#     i=int(input())
#     a.append(i)
#     print(min(a))
#     print(a)







# def pay(salary):
#     to_pay = salary * 1.12
#     if to_pay > salary:
#         print("итог:")
#         print("\t{0}". format(to_pay))
#     else:
#         print("вы уволены!")

# pay(1500)
# pay(21000)
# pay(120000)


# def const(salary, percent=12):
#     print(salary * percent)

# const(15000)
# const(17000, percent=15



# *a,b,c = [1,2,3,4,5,6,7,8,9,0]
# print (a,b,c)




# def func (x):
#     if x < 4:
#      print(x)
#     func(x+1)
#     print(x)
# func(1) 




# calculate_pool_volume = lambda a, b, c: f"объём бассейна {a * b * c}"
# print(calculate_pool_volume(1,2,3))







# def ride ():
#     число =int(input("веддите число:"))
#     for _ in range(число):
#         print ("ride")


# ride()





def генерерация_список():
    N = int(input("веддите число N: "))
    список = []

    for i in range(1, N +1):
        список.append (i) 
        return список
    
print(генерерация_список())


