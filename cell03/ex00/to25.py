try:

    number = int(input("Enter a number: "))
    
    if number > 25:
        print("Error")
    else:

        while number <= 25:
            print(f"Inside the loop... {number}")
            number += 1
            
except ValueError:
    print("Please enter a valid number.")