import string


str_char = input("Enter values: ")
c = 0
for i in str_char:
    c = str_char.count(i)
    print(i,c)