# 10. Encontre todos os números primos entre 2 e 20.000.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
primes = []
for num in range(2, 20001):
    if is_prime(num):
        primes.append(num)
print("Números primos entre 2 e 20.000:")
print(primes)
