def generate_series(a):
    result=[]
    for i in range(a):
        result.append(2*i+1)
    return  result
a=int(input("enter the number"))
print(generate_series(a))