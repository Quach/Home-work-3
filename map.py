# -*- coding: utf-8 -*-
"home work 3"

import time

def map_rq(func, iterator):
    "map rererererecursion"

    res = []
    if len(iterator) == 0:
        return res
    res.append(func(iterator[0]))
    res += map_rq(func, iterator[1:])
    return res

def map_yield(func, iterator):
    "map generator"

    for i in iterator:
        yield func(i)

def map_rq_yield(func, iterator):
    "map rereregenerator"
    
    yield func(iterator[0])

    for x in map_rq_yield(func, iterator[1: ]):
        yield x

def time_me(func, stat_dict):
    "function with params"
    stat_dict.setdefault('num_calls', 0)
    stat_dict.setdefault('cum_time', 0)
    def decorator(main_func):
        "decorator"

        def wrapper(*args, **kwargs):
            "rapper function to profilling func"

            stat_dict['num_calls'] += 1
            time_1 = func()
            res = main_func(*args, **kwargs)
            time_2 = func()
            stat_dict['cum_time'] += time_2 - time_1
            return res
        return wrapper
    return decorator

def main():
    "main"

    assert map_rq(lambda x : x ** 2, [1, 2, 3]) == [1, 4, 9]
    gen = map_yield(lambda x : x ** 2, [1, 2, 3])
    print "Map recurse OK!"

    assert next(gen) == 1
    assert next(gen) == 4
    assert next(gen) == 9
    print "Map generator OK!"

    gen1 = map_rq_yield(lambda x : x ** 2, [1, 2, 3])
    assert next(gen1) == 1
    assert next(gen1) == 4
    assert next(gen1) == 9
    print "Map recurse generator OK!"

    statistics = {}
    @time_me(time.clock, statistics)
    def som_func(param_x, param_y):
        "temp fucntion to profill"
        time.sleep(1.1)

    som_func(1, 2)
    som_func(1, 2)

    assert statistics['num_calls'] == 2
    assert 2.5 > statistics['cum_time'] > 2
    print "Decorator OK!"

    raw_input()
    return 0


if __name__ == "__main__":
    exit(main())