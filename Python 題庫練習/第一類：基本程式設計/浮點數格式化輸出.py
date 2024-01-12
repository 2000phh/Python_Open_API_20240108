def spacefnc(x):
    space = ''
    for i in range (7-len(list(x))):
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

print('|' + space1 + '%.2f' % float(a) + " " + space2 + '%.2f' % float(b) + '|')
print('|' + space3 + '%.2f' % float(c) + " " + space4 + '%.2f' % float(d) + '|')
print('|' + '%.2f' % float(a) + space1 + " " + '%.2f' % float(b) + space2 + '|')
print('|' + '%.2f' % float(c) + space3 + " " + '%.2f' % float(d) + space4 + '|')

