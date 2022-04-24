from asyncio.windows_events import INFINITE

n = 1
sum = 0

def Leibniz(n):
    return 4*(( -1 ) ** n / ( 2*n + 1 ))
time = input("試行回数を入力")

for i in range(0,int(time)):
    sum += Leibniz(i)
print('{:.30f}'.format(sum))  

input("input some key")
