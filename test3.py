def array_diff(a, b):
    for i in range(len(a)):
        print('yea')
        for j in range(len(b)):
            if i > len(a) - 1:
                break
            elif a[i] == b[j]:
                a.remove(a[i])
    print(a)

#array_diff([1,2,2],[1,2])

a = [2,2,2]
a.remove(2)
