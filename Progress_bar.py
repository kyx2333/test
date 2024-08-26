# print('string333\rstring2')

# print('\rsomestring',end='')
from time import sleep
# res = 1
# list = ['|','/','—','\\']
# while 1:
    
#     # print(f'\r{res}',end='')
#     # res += 1
#     for i in list:
#         print('\r loading..... %s'%i,end='')
#         sleep(0.05)

# list1 = ['(づ｡◕ᴗᴗ◕｡)づ','(づ｡—ᴗᴗ—｡)づ','(づ｡◕ᴗᴗ◕｡)づ','(づ｡—ᴗᴗ—｡)づ','(づ｡◕ᴗᴗ◕｡)づ',
# '(づ｡◕ᴗᴗ◕｡)づ','(づ｡◕ᴗᴗ◕｡)づ','(づ｡◕ᴗᴗ◕｡)づ','(づ｡◕ᴗᴗ◕｡)づ','(づ｡◕ᴗᴗ◕｡)づ']
# #第一个动态表情图的所有样式
# list2 = ['u~(@_@)~*','u~(@_@)~*','u~(@_@)~*','u~(@_@)~*','u~(@_@)~*',
# 'u~(@_@)~*','u~(—_—)~*','u~(@_@)~*','u~(—_—)~*','u~(@_@)~*']
# while 1:
#     for a,b in zip(list1,list2):
#         print('\r %s %s'%(a,b),end='')
#         sleep(0.15)

from time import sleep

for i in range(51):
    print('\r加载进度: [%-50s]%.2f%%  '%('#'*i,i*2),end='')
    sleep(0.005)
print('\n load success!','\a')






