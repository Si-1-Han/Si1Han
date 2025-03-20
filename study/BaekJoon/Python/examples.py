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

