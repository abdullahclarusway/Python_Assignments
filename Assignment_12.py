n = int(input("enter a number: "))
count = 0

for i in range(1, n+1):
    if n % i == 0:
        count += 1
if count == 2: # sadece kendisine ve 1'e bölünürse, count = 2 çıkar,asal sayı demektir. 
    print("{} bir asal sayıdır.".format(n))
else:
    print("{} bir asal sayı değildir.".format(n)) 