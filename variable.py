def total(a, b):
    if a + b > 100:
        return 100
    else:
        return a + b

def keepup(a, b):
    if a + b < target:
        return target
    else:
        return a + b

x = 10
y = 20

print(total(x,y))
target = total(x,y)
print(keepup(30,5))
