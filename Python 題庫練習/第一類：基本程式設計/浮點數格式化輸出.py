def spacefunction(x):
    space = ''
    for i in range(7 - len(str(x))):
        space += ' '
    return space


floatlist = []
spacelist = []

for i in range(4):
    y = '%.2f' % (round(float(input()), 2))
    floatlist.append(y)


for i in floatlist:
    spacelist.append(spacefunction(i))

print(floatlist)
print(spacelist)


print('|' + spacelist[0] + floatlist[0] + ' ' + spacelist[1] + floatlist[1] + '|')
print('|' + spacelist[2] + floatlist[2] + ' ' + spacelist[3] + floatlist[3] + '|')
print('|' + floatlist[0] + spacelist[0] + ' ' + floatlist[1] + spacelist[1] + '|')
print('|' + floatlist[2] + spacelist[2] + ' ' + floatlist[3] + spacelist[3] + '|')



# a = (round(float(input()), 2))
# b = (round(float(input()), 2))
# c = (round(float(input()), 2))
# d = (round(float(input()), 2))

# ans1 = spacefunction('%.2f' % (a))
# ans2 = spacefunction('%.2f' % (b))
# ans3 = spacefunction('%.2f' % (c))
# ans4 = spacefunction('%.2f' % (d))

# print('|' + ans1 + '%.2f' % (a) + ' ' + ans2 + '%.2f' % (b) + '|')
# print('|' + ans3 + '%.2f' % (c) + ' ' + ans4 + '%.2f' % (d) + '|')
# print('|' + '%.2f' % (a) + ans1 + ' ' + '%.2f' % (b) + ans2 + '|')
# print('|' + '%.2f' % (c) + ans3 + ' ' + '%.2f' % (d) + ans4 + '|')
