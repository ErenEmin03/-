def avg (lst, x='1'):

    if not x.isnumeric():
        print('Wuwedi chislo: ')
        return

    x=int(x)
    counter=0
    sum=0

    for element in lst:
        if type(element)==int or type(element)==float or element.isnumeric():
            element=int(element)
            sum += element * x
            counter += 1
    if counter==0:
        print('Error')
        return

    return sum / counter
y=int(input("Wuwedi chislo: "))
lst=[]
for i in range(y):
    lst.append(input("Wuwedi chislo: "))
print(lst)
b=avg(lst)
print(b)