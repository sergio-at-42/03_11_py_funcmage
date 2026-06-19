#!/usr/bin/env python3


import random
from typing import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Attack {target} with fireball of {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return (spell1, spell2)


# def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
#     pass


# def conditional_caster(condition: Callable, spell: Callable) -> Callable:
#     pass


# def spell_sequence(spells: list[Callable]) -> Callable:
#     pass


def higher_magic() -> None:
    test_values = [21, 16, 17, 16, 18, 23, 27, 15]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    print("Testing spell combiner...")
    print(f"Combined spell result:{spell_combiner(heal(random.choice(test_targets), random.choice(test_values)), fireball(random.choice(test_targets), random.choice(test_values)))}")
    print("")


if __name__ == "__main__":
    higher_magic()
