sentence = input("Enter a sentence: ").lower()
lst = list(sentence)
dct = {}
for i in lst:
    if i not in dct:
        dct[i] = 0
    dct[i] += 1
print(dct)