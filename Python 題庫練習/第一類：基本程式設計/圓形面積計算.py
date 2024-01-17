# 請撰寫一程式，輸入一圓的半徑，並加以計算此圓之面積和周長，最後請印出此圓的半徑（Radius）、周長（Perimeter）和面積（Area）。

# 提示1：需import math模組，並使用math.pi。
# 提示2：輸出浮點數到小數點後第二位。

# import math

# radius = float(input())
# perimeter = radius * 2 * math.pi
# area = radius ** 2 * math.pi


# print('Radius =' ,'%.2f' % (radius))
# print('Perimeter =' ,'%.2f' % (perimeter))
# print('Area =' ,'%.2f' % (area))



# # 另一種格式化輸出
# # print(f'Radius = {radius:.2f}') 
# print('%.1f' % 1.11)
# print(type('%.1f' % 1.11))



#正確解答
import math
n = eval(input())

print("Radius = {:.2f}".format(n))
print("Perimeter = {:.2f}".format(2*n*math.pi))
print("Area = {:.2f}".format(n*n*math.pi))
