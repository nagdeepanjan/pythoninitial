a=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

length = len(a)

for i in range(length-1):
    for j in range(i+1, length):
        if a[i]>a[j]:
            a[i], a[j]=a[j], a[i]
print(a)
print('############################################')

b=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
length = len(b)

for i in range(length-1):
    for j in range(length-i-1):
        if(b[j]>b[j+1]):
            b[j], b[j+1]=b[j+1], b[j]
    print(b)
print('_____________________________________________________')
print(b)