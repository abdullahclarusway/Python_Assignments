n = int(input("Enter a number : "))
prime= []

for i in range(1, n+1):    
    count = 0
    for b in range(1, n+1): 
        if i % b == 0:
            count += 1
    if count == 2: # sadece kendisine ve 1'e bölünürse, count = 2 çıkar,asal sayı demektir.
        prime.append(i)
            
print(prime)