print('list l')
l = [1, 20, 4, 50, 2, 1, 2] # 숫자나 문자열을 넣을 수 있음

print(l)

print("#####")

print(l[0])
print(l[-1])
print(l[-2])

print('######')

print(l[0:2])
print(l[:2])
print(l[2:5])
print(l[2:])
print(l[:])

print('#####')

print(len(l))
print(type(l))

print('list l2')

l2 = list('abcdefg')
print(l2)

print('#####')

print('n')
n = [1, 2, 3 ,4, 5, 6, 7, 8, 9, 10]
print(n)
print(n[::2])
print(n[::-1])

print('nest')
a = ['a', 'b', 'c']
b = [1, 2, 3]
c = [a, b]

print(c)

print(c[0])
print(c[1])

print(c[0][1])
print(c[1][1])

######################

s1 = list('abcdefg')
print(s1)

s1[0] = 'X'
print(s1)

print(s1[2:5])
s1[2:5] = ['C', 'D', 'E']
print(s1)

print(s1[2:5])
s1[2:5] = []
print(s1)

s1[:] = []
print(s1)

print('##### n1[1~10]')
n1 = [1, 2, 3 ,4, 5, 6, 7, 8, 9, 10]
print(n1)

n1.append(100)
print('append(100)',n1)

n1.insert(0, 200)
print('insert(0, 200)',n1)

n1.pop()
print('pop()',n1)

n1.pop(0)
print('pop(0)',n1)

del n1[0]
print('del n1[0]',n1)

print('##### n2[1, 2, 2, 2, 3')
n2 = [1, 2, 2, 2, 3]
n1.remove(2)
print('n2.remove(2)',n2)

print('a2 1,2,3,4,5 b2 6,7,8,9,10')
a2 = [1, 2, 3 ,4 ,5]
b2 = [6, 7, 8 ,9 ,10]

a2b2 = a2+b2
print('a2+b2 =',a2b2)

a2 += b2
print('a2 += b2, a2 =',a2)

print('x 1 2 3 4 5,y 6 7 8 9 10')
x = [1, 2, 3 ,4 ,5]
y = [6, 7, 8 ,9 ,10]
x.extend(y)

print('x.extend(y)',x)