import timeit
from  typing import Callable

from bm import boyer_moore_search
from kmp import kmp_search
from rabina import rabin_karp_search


def read_file(filename):
    with open(filename, 'r', encoding='cp1251') as f:
        return f.read()


def benchmark(func: Callable, text_: str, pattern_: str):
    setup_code = f"from __main__ import {func.__name__}"
    stmt = f"{func.__name__}(text, pattern)"
    return timeit.timeit(stmt=stmt, setup=setup_code, globals={'text': text_, 'pattern': pattern_}, number=10)


if __name__ == '__main__':
    text1 = read_file('1.txt')
    text2 = read_file('2.txt')
    text1_real_pattern = "найпростіший алгоритм пошуку"
    text2_real_pattern = "Було проведено 4 серії експериментів"
    fake_pattern = "мама мила раму"

    results = []
    for pattern1 in (text1_real_pattern, fake_pattern):
        time = benchmark(boyer_moore_search, text1, pattern1)
        results.append(('Стаття 1', boyer_moore_search.__name__, pattern1, time))
        time = benchmark(kmp_search, text1, pattern1)
        results.append(('Стаття 1', kmp_search.__name__, pattern1, time))
        time = benchmark(rabin_karp_search, text1, pattern1)
        results.append(('Стаття 1', rabin_karp_search.__name__, pattern1, time))

    for pattern2 in (text2_real_pattern, fake_pattern):
        time = benchmark(boyer_moore_search, text2, pattern2)
        results.append(('Стаття 2', boyer_moore_search.__name__, pattern2, time))
        time = benchmark(kmp_search, text2, pattern2)
        results.append(('Стаття 2', kmp_search.__name__, pattern2, time))
        time = benchmark(rabin_karp_search, text2, pattern2)
        results.append(('Стаття 2', rabin_karp_search.__name__, pattern2, time))

    title = f"{'Стаття':<30} | {'Алгоритм':<30} | {'Підрядок':<40} | {'Час виконання, сек'}"
    print(title)
    print("-" * len(title))
    for result in results:
        print(f"{result[0]:<30} | {result[1]:<30} | {result[2]:<40} | {result[3]}")