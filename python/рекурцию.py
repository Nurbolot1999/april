# def func (x):
#     if x < 4:
#      print(x)
#     func(x+1)
#     print(x)
# func(1) 



# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
# print(fact(3))

# def main(number):
#  print(number)
#  if number == 0:
#    return number
#  else:
#     main(number + 1)
#     main (-20)



# def sum (a, c):
#     return a + c


# print(sum(12, 2))
# l = lambda b, o: b + o
# print(l(11,22))
# p = lambda num : True if num > 5 else False



# def compare(n):
#     if n > 5:
#         return True
#     else:
#         return False
#     print (compare(12)) 







# list  = [12, 3, 5,6 , 7, 8,9]


# def get_filter(a, filter_None):
#     if filter is None:
#         result = []
#         for i in a:
#             if filter(i):
#                 result.append (i)
#     return result  
# print(get_filter(list, lambda x: x > 5))         



# (lambda x, y: f"количкство пикселей на карте { x*y}") 

# (lambda weight, height: f'{(height-100) - weight} кг')

# print (l(22, 55)f) 



# calculate_pool_volume = lambda a, b, c: f"объём бассейна {a * b * c}"
# print(calculate_pool_volume(1,2,3))



# def ride ():
#     число =int(input("веддите число:"))
#     for _ in range(число):
#         print ("ride")


# ride()



# def информация(имя, зарплата=5000):
#     return f ("{имя} - {зарплата}")

# print(информация ("нурболот"))
# print(информация("жаркын", 6000))




# def генерерация_список():
#     N = int(input("веддите число N: "))
#     список = []

#     for i in range(1, N +1):
#         список.append (i) 
#         return список
    
# print(генерерация_список())






# def генерация_список():
#     N = []



#     for i in range (1, N + 1 ):
#         список.append (i)
#         return список
    
#     print (генерация_список)

     
    

# multiply = lambda x, y, z: "обьем:" 
# str(x * y * z)

# result = multiply (2, 3, 4)
# print (result) # вывед : обьем: 24





# days_until_new_year = lambda days_passsed: 354 - days_passed


# days_passed = 120
# remaining_days = days_until_new_year(days_passed)
# print(f"до нового года осталось{remaining_days} дней.")




# def print_add_numbers(n):
#     if n <= 0:
#         return
#     if n % 2 != 0:
#         print(n)
#         print_add_numbers(10)



# def remove_one_by_one(my_set):
#     if not my_set:
    #     return
    # print(my_set)

    # my_set.pop()
    # remove_one_by_one(my_set)


 
    # my_set = {1, 2, 3, 4, 5,}
    # remove_one_by_one




# def main (name):
#     print('hello')
#     def inner():
#         print('hello', name)
#     inner()
# main('oomat')



# # def my_func(integer):
# #     def inner (num):
# #         return integer + num
# #     res = inner (100)
# #     print(res)
# # my_func(100)

# def total_callory(p):
#     def cout_callory(p):
#        res = 0
#        for i in p.values():
#            res += i
#        return res
#     print(cout_callory(p))

# products = {
#     'aplle':100,
#     'bread':200,
#     'egg' : 300
# }
    
# total_callory(products)



# def sum(a):
#     def inner(b):
#         return a + b
#     return inner

# inner = sum(1)
# print(inner(10))
# print(inner(500))
# print(inner(110))





# def sum():
#     a = 100
#     def inner(b):
#         return a + b
#     return inner
# s = sum()
    

 

# def sum ():
#     g = 50
#     def inner (n):
#         return g * n
#     return inner
# s = sum()
# print (s)





# def decotator (func):
#     def inner():
#         print('hello')
#         func()
#         print('finish')
#     return inner
    

# @decotator
# def func():
#      print("oomat")

print(res)
return individual
    
@unical
def random_100():
        lst = []
        for i in range(100):
            result = random.randint(10, 50)
            lst.append(result)
        return lst
random_100()# func()     



import random

def unical (random_100):
    def individual():
        result = list(random_100())
        res = (random.choices(result, k=50))
        res = list(set (res))
        random.shuffle(res)


