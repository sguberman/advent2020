from time import perf_counter


def elapsed_time(fn, *args, **kwargs):
    start = perf_counter()
    result = fn(*args, **kwargs)
    end = perf_counter()
    return result, end - start


def print_results(*results):
    for i, (answer, timing) in enumerate(results, start=1):
        print(f"Part {i}: {answer} in {timing:.6f} seconds")
