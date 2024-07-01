import time
start_time = time.time()


def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_primes_between(start, end):
    """Get a list of prime numbers between start and end."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def save_primes_to_file(primes, file_path):
    """Save the list of prime numbers to a file."""
    with open(file_path, 'w') as file:
        for prime in primes:
            file.write(f"{prime}\n")

def main():
    start = 1
    end = 2500000
    file_path = 'results.txt'  # Update this to the desired file path

    # Get the list of prime numbers
    primes = get_primes_between(start, end)

    # Save the prime numbers to a file
    save_primes_to_file(primes, file_path)

    # Output the location of the saved file
    import os
    abs_file_path = os.path.abspath(file_path)
    print(f"Prime numbers between {start} and {end} have been saved to {abs_file_path}")

if __name__ == "__main__":
    main()


print("--- %s seconds ---" % (time.time() - start_time))