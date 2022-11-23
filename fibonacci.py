z=int(input("Enter a num"))
x=0
print("Fibonacci:", x, end=" ")
for i in range(1,10):
    y = x + z
    x = z
    z = y
    print(y, end=" ")