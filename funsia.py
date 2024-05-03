# def  hello_world():
#     print( 'hello world')
#     hello_world()



# /def add(a, b) -> int:
#         return a + b
    


# result = add(12, 5)
# print (result)

 

# def add (s, f)  -> int:
#     return s * f


# result = add(123, 55)
# print (result)


# def add (g, t ) -> int:
#     return g - t


# result = add (142, 34)
# print (resul)

# gat = ['aman', 'anat','23', '1']
# def split_and_reverse(gat):
#     # Разделение списка на две части
#     middle = len(gat) // 2
#     left_half = gat[:middle]
#     right_half = gat[middle:]

#     # Разворот обеих частей
#     left_half_reverse= left_half[::-1]
#     right_half_reverse=right_half[:: -1]

#     # Объединение развернутых частей
#     reversed_list = right_half_reverse+ left_half_reverse
#     return reversed_list

# # Пример использования:
# result = split_and_reverse(gat)
# print(result)



# a = min (12, 333 ,34 , 2)
# b = max(12,min(3, 50 ), abs(- 13), max (12,34,47))
# print(b)

# def square(a):
#     return a ** 2
# so = square(222)
# print(so)


# def even(x):
#     return x % 2 == 0   
# for i in range(1, 11):
#     print(i, even(i))



# x = int (input('namber:'))
# def even(x):
#     return x + 1

# print(even(x))

# def bolshe(num):
#     if num <= 100:
#         return f'your number{num}'
#     else:
#         return 'incorrect num'
# print(bolshe(even (x)))



# def pay(salary):
#     to_pay = salary * 1.12
#     if to_pay > salary:
#         print("итог:")
#         print("\t{0}". format(to_pay))
#     else:
#         print("вы уволены!")

# pay(-1500)
# pay(-21000)
# pay(-120000)



# def const(salary, percent=12):
#     print(salary * percent)

# const(15000)
# const(17000, percent=15)


# *a,b,c = [1,2,3,4,5,6,7,8,9,0]
# print (a,b,c)


# def func(a,b,c,d):
#     return a, b, c, d

# print(func(1,2,3,4,5))
# a = ['hello', True 233, [1,2,3,4]]
# print(func(*a))



# def func1(*nums):
#     res = 0
#     for num in nums:
#         res += num
#     return res
# print(func1(1,2,3,4,5,6,7,8,9))





    

# def func(**kwargs):
#     for num, val in kwargs.item():
#      print (num, val)
# func(a = 12, b=112)





# def student(name, ** lessons):
#    print(f"hello, {name}")
#    for names, times in lessons.items():
#       print(f"{names} : {times}")
# student ('oomat', chemstry =4, marth=7, kyrgyzlang=)



# def func (x):
#     if x < 4:
#      print(x)
#     func(x+1)
#     print(x)
# func(1) 


 


# def summa(x):
#    if x == 1:
#       return 1
#    else:
#       return x + summa(x -1)
# print(summa(10))





