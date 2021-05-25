import random
import string

alphabets=string.ascii_letters
numbers='0123456789'
symbols='@#!().-_*&;/+'

combined_keywords=alphabets+numbers+symbols
password_length=int(input('Enter password length : '))
password=''.join(random.sample(combined_keywords,password_length))
print(password)
input('Press ENTER to exit')