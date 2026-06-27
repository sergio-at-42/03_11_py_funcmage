#!/usr/bin/env python3


import functools
import operator
from typing import Any, Callable


def enchantment(power: int, element: str, target: str) -> str:
    return(f"{element} enchantmen with {power} HP to cast on {target}")


def spell_reducer(spells: list[int], operation: str) -> int:
    reduce: int = 0
    if spells:
        match operation:
            case "add":
                reduce = functools.reduce(operator.add, spells)
            case "multiply":
                reduce = functools.reduce(operator.mul, spells)
            case "max":
                reduce = functools.reduce(max, spells)
            case "min":
                reduce = functools.reduce(min, spells)
            case _:
                print(f"{operation} : operation is unknown...")
    return (reduce)


def partial_enchanter(base_enchantment: Callable) -> dict[str,Callable]:
    return ({
        "specialized versions 1": functools.partial(base_enchantment, power=50),
        "specialized versions 2": functools.partial(base_enchantment, power=50),
        "specialized versions 3": functools.partial(base_enchantment, power=50),
    })


@functools.lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return (n)
    return (memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2))


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatcher_func(spell_type) -> str:
        return (f"Unknown spell type : {spell_type}")
    
    @dispatcher_func.register
    def _(spell_type: int):
        return (f"Damage spell: {spell_type} damage")

    @dispatcher_func.register
    def _(spell_type: str):
        return (f"Enchantment: {spell_type}")

    @dispatcher_func.register
    def _(spell_type: list):
        return (f"Multi-cast: {len(spell_type)} spells")

    return (dispatcher_func)


def functools_artifacts() -> None:

    print("Testing spell reducer...")
    spells: list[int] = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    print(f"Sum:   {spell_reducer(spells, "add")}")
    print(f"Product:   {spell_reducer(spells, "multiply")}")
    print(f"Max:   {spell_reducer(spells, "max")}")
    print(f"Min:   {spell_reducer(spells, "min")}")
    print(f"Toto:   {spell_reducer(spells, "toto")}")
    print(f"Empty Spell:   {spell_reducer([], "add")}")
    print("")

    print("Testing memoized fibonacci...")
    print(f"Fib(0):   {memoized_fibonacci(0)}")
    print(f"Fib(1):   {memoized_fibonacci(1)}")
    print(f"Fib(10):   {memoized_fibonacci(10)}")
    print(f"Fib(15):   {memoized_fibonacci(15)}")
    print(f"Cache : {memoized_fibonacci.cache_info()}")
    print("")

    print("Testing spell dispatcher...")
    print(f"{spell_dispatcher()(42)}")
    print(f"{spell_dispatcher()("fireball")}")
    print(f"{spell_dispatcher()([42, 42, 42])}")
    print(f"{spell_dispatcher()({"toto": 42})}")
    print("")


if __name__ == "__main__":
    functools_artifacts()
