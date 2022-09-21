from re import A

# 문자열
print(r'C:\name\name') # raw string, Escape 문자 출력


# 인덱스

num = 1
name = 'Mike'
is_ok = True

print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

word = 'python'
print(word)

word = 'j' + word[1:]
print(word[:])

print("###########")
# method

s = 'My name is Jinn. Hi jinn.'
print(s)

is_start = s.startswith('My')
print(is_start)

print(s.find('jinn'))
print(s.rfind('jinn'))
print(s.count('jinn'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('jinn','fck'))

# 문자 대입
print('a is {}'.format('a'))
print('a is {}'.format('test'))

print('a is {0} {1} {2}'.format(1, 2, 3))
print('a is {2} {1} {0}'.format(1, 2, 3))

print('My name is {0} {1}. I\'m jinn.'.format('jinn','lee'))
print('My name is {name} {family}. I\'m {name}.'.format(name='jinn', family='lee'))

# after python3.6, can use f-strings
name = 'jinn'
family = 'lee'
nf = f"My name is {name} {family}"
print(nf)

