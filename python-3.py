a = int(input("Enter a number: "))
if a % 2 == 0:
    a -= 1

result = []
for i in range(a):
    result.append(str(2 * i + 1))  

print(", ".join(result))  
