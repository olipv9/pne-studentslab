# exercise 1:
l = []
for i in range(12):
    if len(l) < 11:
       if len(l) < 2:
           l.append(i)
       else:
           x = l[i - 1]
           y = l[i - 2]
           z = x + y
           l.append(z)

# exercise 2:
def fibon(n):
    l = []
    for i in range(n + 1):
        if len(l) < n:
            if len(l) < 2:
                l.append(i)
            else:
                x = l[i - 1]
                y = l[i - 2]
                z = x + y
                l.append(z)
    return l
# exercise 3:
def fibon_sum(n):
    x_x = fibon(n)
    sum = 0
    for i in x_x:
        sum += i
    return sum
print(fibon_sum(16))