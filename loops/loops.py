

# i = 1
# while i <= 99:
#     print(f'{i}')
#     i += 1 



# name1 = ''
# name2 = ''
# i = 0

# while name1.lower() != 'john' or name2.lower()!= 'raichel':
#     name1 = input('vvedi')
#     name2 = input('vvedi')
#     i += 1 
#     if i > 5:
#         print('ahahaha')
#         break
# else:
#     print('ty loh, ahhahahah')
    

# admin = ['john', 'i love python 123']
# i = 3 
# password = None

# while admin[1] != password:
#     password = input(f'{admin[0]}')
#     i -= 1
#     if i == 0:
#         print('ti loh ahahha')
#         break
# else:
#     print(f'{admin[0]} чел харощ ')


# list_ = [0,1,2,3,4,5,6,7,8,9]

# i =iter(list_)
# print(i)
# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))

# for i in list_[::-1]:
#     print(i)

# secret_list = ['DeltaViski', 'lotr123', 'twenty two']
# nick = input('введи свой ник')
# while nick not in secret_list:
#     print('incorect type nick')
#     nick = input('vvedi nick')
# else:
#     print(f'you are welcome to the panic room {nick}' )


# list_ = (23436, 190187200, 380457890232)

numb = int(input("Введите целое число: "))
print("Результат:", end = " ")
for i in range(numb - 1, 1, -1):
    if (numb % i == 0):
        print(i, end = " ")

                                                                                                                                                                                                                                                                                                                                                                    