fibo = []
for i in range(10):
    if i <2:
        fibo.append(1)
    else:
        fibo.append(fibo[i-2]+fibo[i-1])
print(fibo)