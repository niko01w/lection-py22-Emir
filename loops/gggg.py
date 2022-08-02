# i = 1
# while i <= 11:
#     print( i ** 2)
#     i += 1

# i = 2 
# b = 0
# while b <= 20:
#     print(i ** b)
#     b += 1 

letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
dodik = ''

for i in letters:
    if i.islower():
        dodik+=i
print(dodik)
