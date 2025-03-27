# x = ['abstract algebra', 'PrOgRaMmErS']
#
#
# def solution(x):
#     x[0] = x[0].replace('a', 'A')
#     print(x[0])
#     return x[0]
#
#
# def solution1(x):
#     x[1] = x[1].lower()
#     x[1] = x[1].replace('a', 'A')
#     print(x[1])
#
#     return x[1]
#
# solution(x)
# solution1(x)

# myString = "PrOgRaMmErS"
#
# def solution(myString):
#     a = myString.lower.replace('a', 'A')
#     return a
#
# solution(myString)

# a = input()
# b = ""
#
# for char in a:
#     if char.isupper():
#         b += char.lower()
#     elif char.islower():
#         b += char.upper()
#     else:
#         b += char
# print(b)

# print(input().swapcase())

# # 10430번
# A, B, C = map(int, input().split())
#
# print((A + B) % C)
# print( ((A%C) + (B%C))%C )
# print( (A*B)%C )
# print( ((A%C) * (B%C))%C )

# # 2588번 - 슬라이싱(slicing)은 문자형 변수만 가능하므로 형변환해야 함
# A = int(input())
# B = int(input())
#
# print(A * int(str(B)[2]))
# print(A * int(str(B)[1]))
# print(A * int(str(B)[0]))
# print(A * B)

# # 11382번
# A, B, C = map(int, input().split())
# print(A + B + C)

# # 10171번
# print('\\    /\\')
# print(' )  ( \')')
# print('(  /  )')
# print(' \\(__)|')

# # 1330번
# A, B = map(int, input().split())
# if A > B:
#     print('>')
# elif A < B:
#     print('<')
# else:
#     print('==')

# # 9498번
# TestScore = int(input())
#
# if 90 <= TestScore <= 100:
#     print('A')
# elif 80 <= TestScore < 90:
#     print('B')
# elif 70 <= TestScore < 80:
#     print('C')
# elif 60 <= TestScore < 70:
#     print('D')
# else:
#     print('F')

# # 2753번
# def yoonyear(a) :
#     return int((a % 4 == 0 and a % 100 != 0) or a % 400 == 0)
#
# print(yoonyear(int(input())))

# # 14681번
# x = int(input())
# y = int(input())
#
# if x>0 and y>0:
#     print('1')
# elif x<0 and y>0:
#     print('2')
# elif x<0 and y<0:
#     print('3')
# elif x>0 and y<0:
#     print('4')

# # 2884번
# H, M = map(int, input().split())
#
# if M-45 <= 0:
#     H -= 1
#     M += 15
#     if H < 0:
#         H += 24
# else:
#     M -= 45
#
# print(H, M)

# # 2525번
# H, M = map(int, input().split())
# T = int(input())
#
# if T + M >= 60:
#     H += (T + M) // 60
#     M = (T + M) % 60
#     if H >= 24:
#         H = H - 24
# else:
#     M = T + M
#
# print(H, M)

# # 2480번
#
# a, b, c = map(int, input().split())
#
# if a == b == c:
#     print(10000+a*1000)
# elif a==b or b==c or c==a:
#     if a==b or b==c:
#         print(1000+b*100)
#     else:
#         print(1000 + c * 100)
# else:
#     print(max(a, b, c)*100)

# #람다식 활용
# print(list(map(lambda x: x ** 2, range(0, 5))))

# #  reduce() : 시퀀스의 원소들을 누적적으로 함수에 적용
# from functools import reduce
# print(reduce(lambda x, y: x + y, [0,1,2,3,4]))
# print(reduce(lambda x, y: y + x, 'hello'))

# # filter() : 리스트의 원소들을 함수에 적용 후 참인 값들을 리스트화
# print(list(filter(lambda x: x < 5, range(10))))

# # 홀수 리스트
# print(list(filter(lambda x: x%2==1, range(10))))

# # 2739번
# N = int(input())
# x = 0
# for a in range(9):
#     print('{} * {} = {}'.format(N, x+1, N*(a+1)))
#     x += 1

# # 10950번
# from functools import reduce
#
# T = int(input())
# l = []
# for x in range(T):
#     l.append(int(reduce(lambda x, y: x + y, map(int, input().split()))))
#
# for x in range(T):
#     print(l[x])

# # 8393번
# from functools import reduce
#
# print(reduce(lambda x, y: x+y, range(1,int(input())+1)))

# 25304번
from functools import reduce

X = int(input())
N = int(input())
price=[]
ammount=[]

for x in range(N):
    p, a = map(int, input().split())  # 가격과 개수 입력
    price.append(p)
    ammount.append(a)

total = sum(price[i] * ammount[i] for i in range(N))
if total == X:
    print("Yes")
else:
    print("No")