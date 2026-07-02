#!/usr/bin/env python3

import random
import functools
import time
from collections.abc import Callable
from typing import Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:    # type: ignore
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        exec_time = time.perf_counter() - start
        print(f"Spell completed in {exec_time:.3f} seconds")
        return (result)

    return (wrapper)


def power_validator(min_power: int) -> Callable[..., Any]:

    def decorator_factory(func: Callable[..., Any]) -> Callable[..., Any]:

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:    # type: ignore
            power: int = 0
            result: str = "Insufficient power for this spell"
            if "power" in kwargs:
                power = kwargs["power"]
            elif args:
                if isinstance(args[0], int) and args[0] >= min_power:
                    power = args[0]
                elif args[2] >= min_power:
                    power = args[2]
            if power >= min_power:
                result = func(*args, **kwargs)
            return (result)

        return (wrapper)

    return (decorator_factory)


def retry_spell(max_attempts: int) -> Callable[..., Any]:

    def decorator_factory(func: Callable[..., Any]) -> Callable[..., Any]:

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:    # type: ignore
            attemp: int = 1
            while attemp <= max_attempts:
                try:
                    return (func(*args, **kwargs))
                except Exception:
                    if attemp < max_attempts:
                        attemp += 1
                        print("Spell failed, retrying... (attempt ", end="")
                        print(f"{attemp}/{max_attempts})")
                    else:
                        return (f"Spell casting failed after {max_attempts
                                                              } attempts")

        return (wrapper)

    return (decorator_factory)


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        validate: bool = False
        if len(name) >= 3:
            validate = True
            for c in name:
                if not c.isalpha() and not c.isspace():
                    validate = False
        return (validate)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (f"Successfully cast {spell_name} with {power} power")


@spell_timer
def fireball(power: int = 10) -> str:
    time.sleep(1)
    return (f"Fireball cast with {power} power !")


@power_validator(42)
def freeze(power: int = 10) -> str:
    time.sleep(0.42)
    return (f"Freeze cast with {power} power !")


@retry_spell(2)
def meteor(power: int = 10) -> str:
    if random.choice([True, False]):
        raise Exception()
    return (f"Meteor cast with {power} power !")


def decorator_mastery() -> None:

    print("Testing spell timer...")
    print(f"Result: {fireball()}")
    print(f"Result: {fireball(42)}")
    print("")

    print("Testing power validator...")
    print(f"Result: {freeze(64)}")
    print(f"Result: {freeze()}")
    print("")

    print("Testing retrying spell...")
    print(f"Result: {meteor(64)}")
    print(f"Result: {meteor()}")
    print(f"Result: {meteor(42)}")
    print(f"Result: {meteor(16)}")
    print("")

    print("Testing MageGuild...")
    merlin = MageGuild()
    zotar = MageGuild()
    print(f"Test merlin's name : {merlin.validate_mage_name("Merlin")}")
    print(f"Test name Toto42 : {MageGuild.validate_mage_name("Toto42")}")
    print(merlin.cast_spell("Lightning", 69))
    print(zotar.cast_spell("Fireball", 2))
    print(zotar.cast_spell("Fireball", power=256))
    print("")


if __name__ == "__main__":
    decorator_mastery()
