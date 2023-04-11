from memory_profiler import profile, memory_usage
from src.list_prime import list_prime
import random
import timeit


@profile
def metricFunction():
    list_prime(random.randrange(2, 28))


if __name__ == "__main__":
    execution_time = timeit.timeit(metricFunction, number=1000)
    print(f"Execution time: {execution_time}")
