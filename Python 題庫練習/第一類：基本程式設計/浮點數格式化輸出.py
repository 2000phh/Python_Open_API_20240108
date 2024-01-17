# 還沒成功的程式碼
# def spacefunction(x):
#     space = ''
#     for i in range(7 - len(str(x))):
#         space += ' '
#     return space


# floatlist = []
# spacelist = []

# for i in range(4):
#     y = '%.2f' % (round(float(input()), 2))
#     floatlist.append(y)


# for i in floatlist:
#     spacelist.append(spacefunction(i))

# print(floatlist)
# print(spacelist)


# print('|' + spacelist[0] + floatlist[0] + ' ' + spacelist[1] + floatlist[1] + '|')
# print('|' + spacelist[2] + floatlist[2] + ' ' + spacelist[3] + floatlist[3] + '|')
# print('|' + floatlist[0] + spacelist[0] + ' ' + floatlist[1] + spacelist[1] + '|')
# print('|' + floatlist[2] + spacelist[2] + ' ' + floatlist[3] + spacelist[3] + '|')



#成功執行的程式碼
def spacefunction(x):
    space = ''
    for i in range(7 - len(str(x))):
        space += ' '
    return space


a = (round(float(input()), 2))
b = (round(float(input()), 2))
c = (round(float(input()), 2))
d = (round(float(input()), 2))

a_format = '%.2f' % (a)
b_format = '%.2f' % (b)
c_format = '%.2f' % (c)
d_format = '%.2f' % (d)

ans1 = spacefunction(a_format)
ans2 = spacefunction(b_format)
ans3 = spacefunction(c_format)
ans4 = spacefunction(d_format)

print('|' + ans1 + a_format + ' ' + ans2 + b_format + '|')
print('|' + ans3 + c_format + ' ' + ans4 + d_format + '|')
print('|' + a_format + ans1 + ' ' + b_format + ans2 + '|')
print('|' + c_format + ans3 + ' ' + d_format + ans4 + '|')

