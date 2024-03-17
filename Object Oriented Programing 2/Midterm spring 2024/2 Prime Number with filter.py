def prime_number(n):
    #"""Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):   # square root operation
        if n % i == 0:
            return False
    return True

numbers = list(range(1,101))
prime_numbers =list(filter(prime_number, numbers))
print(f"1 to 100 Prime Number List :{prime_numbers}")


def is_prime(n):
    #"""Check if a number is prime."""
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

prime_numbers = [num for num in range(1, 101) if is_prime(num)]
print("Prime numbers from 1 to 100:", prime_numbers)



