#!/usr/bin/env python3


import random
from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return (f"Heal restores {target} for {power} HP")


def fireball(target: str, power: int) -> str:
    return (f"Attack {target} with fireball of {power} HP")


def is_a_dragon(target: str, power: int) -> bool:
    if target == "Dragon":
        return (True)
    return (False)


def is_a_wizard(target: str, power: int) -> bool:
    if target == "Wizard":
        return (True)
    return (False)


def power_over_20(target: str, power: int) -> bool:
    if power >= 20:
        return (True)
    return (False)


def spell_combiner(spell1: Callable[[str, int], str], spell2: Callable[[str, int], str]) -> Callable[[str, int], tuple[str, str]]:
    def combiner(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return (combiner)


def power_amplifier(base_spell: Callable[[str, int], str], multiplier: int) -> Callable[[str, int], str]:
    def amplifier(target: str, power: int) -> str:
        return (base_spell(target, power * multiplier))
    return (amplifier)


def conditional_caster(condition: Callable[[str, int], bool], spell: Callable[[str, int], str]) -> Callable[[str, int], str]:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return (spell(target, power))
        else:
            return ("Spell fizzled")
    return (caster)


def spell_sequence(spells: list[Callable[[str, int], str]]) -> Callable[[str, int], list[str]]:
    def sequence(target: str, power: int = 10) -> list[str]:
        return (list(spell(target, power) for spell in spells))
    return (sequence)


def higher_magic() -> None:
    def target() -> str:
        return (random.choice(['Dragon', 'Goblin', 'Wizard', 'Knight']))

    def power() -> int:
        return (random.choice([21, 16, 17, 18, 23, 27, 15]))

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result : {combined(target(), power())}")
    print("")

    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball, 8)
    print(f"Spell Amplified : {mega_fireball(target(), power())}")
    print("")

    print("Testing conditional caster...")
    dragon = conditional_caster(is_a_dragon, fireball)
    t = target()
    p = power()
    print(f"Target : {t}   -   Power : {p}")
    print(f"Spell casted only for Dragon : {dragon(t, p)}")
    wizard = conditional_caster(is_a_wizard, heal)
    t = target()
    p = power()
    print(f"Target : {t}   -   Power : {p}")
    print(f"Spell casted only for Wizard : {wizard(t, p)}")
    big_power = conditional_caster(power_over_20, fireball)
    t = target()
    p = power()
    print(f"Target : {t}   -   Power : {p}")
    print(f"Spell casted only for power over 20 : {big_power(t, p)}")
    print("")

    print("Testing spell sequence...")
    sequence = spell_sequence([fireball, heal, mega_fireball])
    print("Spells sequence result :")
    for s in sequence(target(), power()):
        print(s)
    print("")


if __name__ == "__main__":
    higher_magic()
