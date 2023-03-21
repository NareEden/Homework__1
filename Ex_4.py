# Profiling is a way to measure the performance of the software application
# by measuring the resources used(time, memory, etc.) for the particular parts of
# it.

# We want to create a decorator @ profile that we can use to analyze the
# functions.

# The decorator should write all the logs to a file, separate from the application
# output.

# Example
# 1


from datetime import datetime
from time import sleep


def profile(func):
    def wrapper(x):
        start = datetime.now()
        res = func(x)
        print(datetime.now()-start)
        return res
    return wrapper


@profile
def foo(x):
    sleep(2)
    print(x ** 2)
    # return x ** 2


foo(3)


# sleep(60)
# foo(42)


# Output: (In performance.log file)
# 2023 - 03 - 11
# 21: 07:51.998617 - foo(2) - 0: 00:02.000984
# 2023 - 03 - 11
# 21: 0
# 8: 54.013414 - foo(42) - 0:00: 02.001023