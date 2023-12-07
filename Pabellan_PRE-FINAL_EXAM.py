def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

while True:
    try:
        start = int(input("Enter a non-negative number for start: "))
        end = int(input("Enter a number greater than the start: "))
        if start < 0:
            print("Enter a non-negative number.")
        elif end < start:
            print("Enter a number greater than the start.")
        else:
            for num in range(start, end + 1):
                if check_prime(num):
                    print(num)
    except ValueError:
        print("Enter a valid number.")

    continue_prompt = input("Do you want to continue? (yes/no): ")
    if continue_prompt.lower() != "yes":
        break
