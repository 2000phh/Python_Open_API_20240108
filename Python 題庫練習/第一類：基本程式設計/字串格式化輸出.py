# 請撰寫一程式，輸入四個單字，然後將這四個單字以欄寬為10、欄與欄間隔一個空白字元、每列印兩個的方式
# 先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。


def spacefunction(x):
    space = ''
    for i in range(10-len(x)):
        space += ' '
    return space


# a = input()
# b = input()
# c = input()
# d = input()

inputs = [input() for _ in range(4)]
a, b, c, d = inputs

a_space = spacefunction(a)
b_space = spacefunction(b)
c_space = spacefunction(c)
d_space = spacefunction(d)

spacefunction(a)
spacefunction(b)
spacefunction(c)
spacefunction(d)

print('|' + a_space + a + ' ' + b_space + b + '|')
print('|' + c_space + c + ' ' + d_space + d + '|')
print('|' + a + a_space + ' ' + b + b_space + '|')
print('|' + c + c_space + ' ' + d + d_space + '|')

