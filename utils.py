from time import time


def elapsed_time(fn, *args, **kwargs):
    start = time()
    result = fn(*args, **kwargs)
    end = time()
    return result, end - start


def print_results(*results):
    for i, (answer, timing) in enumerate(results, start=1):
        print(f"Part {i}: {answer} in {timing:.6f} seconds")
