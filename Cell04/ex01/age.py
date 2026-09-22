age = int(input("Please tell me your age: "))

print(f"*********************************************")

for i in range(0,3):
    j = i + 1
    print(f"In {j*10} years, you'll be {age + j*10} years old.")

print(f"*********************************************")