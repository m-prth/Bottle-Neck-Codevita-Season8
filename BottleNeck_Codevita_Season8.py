n = int(input())
s=input()
a = [int(x) for x in str(s)]


a.sort()
i = 0
j = i+1
while n != None:
    if i > j:
        j = 0
    elif j > n:
        j = 0
    elif i == 2 and j == 2 and n == -2 and j == None:
        break
    if a[i] < a[j]:
        a.remove(a[i])
        if i > j:
            j = 0
        elif j > n:
            j = 0
    elif a[i] == a[j]:
        j = j+1
        if j == (n-1):
            j = 0
        else:
            i += 1
            j += 1
    elif a[i] > a[j]:
        i = 0
        j = i+1
    else:
        break
    if n==0:
        break
    else:
        n = n-1

print(len(a))
