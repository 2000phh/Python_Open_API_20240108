# def spacefnc(x):
#     space = ''
#     for i in range (5-len(x)):
#         space += ' '
#     return space


# a = input()
# b = input()
# c = input()
# d = input()


# space1 = spacefnc(a)
# space2 = spacefnc(b)
# space3 = spacefnc(c)
# space4 = spacefnc(d)



# print('|' + space1 + a + " " + space2 + b + '|')
# print('|' + space3 + c + " " + space4 + d + '|')
# print('|' + a + space1 + " " + b + space2 + '|')
# print('|' + c + space3 + " " + d + space4 + '|')






def spacefunction(x):
    space = ''
    for i in range(5 - len(x)):
        space += ' '
    return space

a = input()
b = input()
c = input()
d = input()

ans1 = spacefunction(a)
ans2 = spacefunction(b)
ans3 = spacefunction(c)
ans4 = spacefunction(d)

print('|' + ans1 + a + ' ' + ans2 + b + '|')
print('|' + ans3 + c + ' ' + ans4 + d + '|')
print('|' + a + ans1 + ' ' + b + ans2 + '|')
print('|' + c + ans3 + ' ' + d + ans4 + '|')


