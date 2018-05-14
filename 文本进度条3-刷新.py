import time
scale = 10
print("执行开始".center(scale//2,'-'))
t = time.clock()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    t -= time.clock()
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,-t),end='')
    time.sleep(1)
print("\n"+"执行结束".center(scale//2,'-'))
