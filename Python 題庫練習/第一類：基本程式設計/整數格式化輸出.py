def spacefnc(x):
    space = ''
    for i in range (5-len(x)):
        space += ' '
    return space


a = input()
b = input()
c = input()
d = input()


space1 = spacefnc(a)
space2 = spacefnc(b)
space3 = spacefnc(c)
space4 = spacefnc(d)



print('|' + space1 + a + " " + space2 + b + '|')
print('|' + space3 + c + " " + space4 + d + '|')
print('|' + a + space1 + " " + b + space2 + '|')
print('|' + c + space3 + " " + d + space4 + '|')


