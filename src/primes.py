import math
from timeit import default_timer as timer

def num_primes_python(lower, upper):
    total = 0
    for num in range(lower, upper + 1):
        # 0 and 1 are not primes
        if num > 1:
            prime = True
            for i in range(2, num):
                if (num % i == 0):
                    prime = False
            if prime:
                total+=1

    return total


start_python = timer()
num_primes_python(0, 10000)
end_python = timer()
print("Python time:", end_python - start_python)

start_rust = timer()
math.num_primes_rust(0, 10000)
end_rust = timer()
print("Rust time:", end_rust - start_rust)


# print("")
# print("-------------")
# print("Python:  ", num_primes_python(0, 1000))
# print("Rust:    ", math.num_of_primes_rust(0, 1000))
# print("-------------")
