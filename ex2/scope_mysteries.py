#!/usr/bin/env python3


from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    counter: int = 0

    def count() -> int:
        nonlocal counter
        counter += 1
        return (counter)

    return (count)


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    power: int = initial_power

    def accumulate(amount: int) -> int:
        nonlocal power
        power += amount
        return (power)

    return (accumulate)


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:

    def enchantment(item_name: str) -> str:
        return (f"{enchantment_type} {item_name}")

    return (enchantment)


def memory_vault() -> dict[str, Callable[..., Any]]:
    memory: dict[str, str] = {}

    def store(key: str, value: str) -> None:
        memory[key] = value

    def recall(key: str) -> str:
        return (memory.get(key, "Memory not found"))

    return ({"store": store, "recall": recall})


def scope_mysteries() -> None:

    print("Testing mage counter...")
    counter_a = mage_counter()
    for i in range(1, 5):
        print(f"counter_a call {i} : {counter_a()}")
    counter_b = mage_counter()
    for i in range(1, 3):
        print(f"counter_b call {i} : {counter_b()}")
    print("")

    print("Testing spell accumulator...")
    base: int = 100
    accumulator = spell_accumulator(base)
    print(f"Base {base}, 20 :   {accumulator(20)}")
    print(f"Base {base}, 30 :   {accumulator(30)}")
    print("")

    print("Testing enchantment factory...")
    factory_1 = enchantment_factory("Flaming")
    factory_2 = enchantment_factory("Frozen")
    print(factory_1("Sword"))
    print(factory_2("Shield"))
    print("")

    print("Testing memory vault...")
    memory_managment = memory_vault()
    memory_managment["store"]("secret", "42")
    print("Store ’secret’ = 42")
    print(f"Recall ’secret’ : {memory_managment["recall"]("secret")}")
    print(f"Recall ’unknown’ : {memory_managment["recall"]("unknown")}")
    print("")


if __name__ == "__main__":
    scope_mysteries()
