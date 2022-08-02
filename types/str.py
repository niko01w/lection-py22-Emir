"""
строки в python - набор последовательных символов которые мы используем для хронения и представления текстовой информации.

индексация в строке
"""

#name = 'john'

# j=0=-4
# o=1=-3
# h=2=-2
# n=3=-1

#print(name)
#print(name[1])
#print(name[-1])


#str1= 'berthday'
#print(str1[6], str1[7], str1[6])
#print(str1[0], str1[3], str1[2], str1[4])

#срезы по индексам 
#[start: end: <step>]

#str1= 'birthday'

#print(str1[5:7])

#print(str1[5:])

#print(str1[:5])

#text = 'hello world ! my name is John! i\'m not a king! i\'m not a god! i\'m Deamon  '

#print(text[:13])
#print(text)
#print(text[::])
#print(text[::-1])


#конкатинация строк 
#a = 'hello'
#b = 'world'
#c =' '

#result= (a+c+b + ' ')*6
#print(result)

#экранирование - при помощи которого можно вставлять символы в строку, которые можно ввести с клавиатуры





#\n -> перенос строки 
#\t -> горизонтальная табуляция 
#\v -> вертикальная табуляция 
#\f -> перевод страницы 
#\r -> возврат указателя 

#name = 'John\nSnow'
#print(name)
#print(len(name))



#форматирование строк 
"""
1. с помощью %
2. с использованием метода .format()
3. Интерполяция строк(f-строки)
"""



#from this import s


#name = input('enter your name:' )
#lastName = input('enter yuor last name:')

#print('hello mr/mrs %s %s' %(name,lastName))

#name = input('enter your name:' )
#lastName = input('enter yuor last name:')

#print('hello mr/mrs {} {}'.format(name,lastName) )

#a = input('enter mr/mrs:')
#name = input('enter your name:' )
#lastName = input('enter yuor last name:')
#x=' '
#print(f'hello {a} {lastName}{x}{name} wellcome to the party!')


print(dir(str))

