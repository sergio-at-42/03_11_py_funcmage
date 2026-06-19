#!/usr/bin/env python3


from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return (sorted(artifacts, key=lambda artif: artif["power"], reverse=True))


def power_filter(mages: list[dict[str, Any]], min_power: int) \
        -> list[dict[str, Any]]:
    return (list(filter(lambda mage: mage["power"] >= min_power, mages)))


def spell_transformer(spells: list[str]) -> list[str]:
    return (list(map(lambda word: f"*{word}*", spells)))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    return ({"max_power": max(mages, key=lambda p: p["power"])["power"],
             "min_power": min(mages, key=lambda p: p["power"])["power"],
             "avg_power": round(sum(map(lambda p: p["power"], mages))
                                / len(mages), 2)})


def lambda_spells() -> None:
    artifacts = [{'name': 'Earth Shield', 'power': 117, 'type': 'focus'},
                 {'name': 'Shadow Blade', 'power': 116, 'type': 'accessory'},
                 {'name': 'Earth Shield', 'power': 69, 'type': 'weapon'},
                 {'name': 'Ice Wand', 'power': 73, 'type': 'relic'}]
    mages = [{'name': 'Casey', 'power': 62, 'element': 'water'},
             {'name': 'Ember', 'power': 78, 'element': 'wind'},
             {'name': 'River', 'power': 66, 'element': 'shadow'},
             {'name': 'Ash', 'power': 62, 'element': 'water'},
             {'name': 'Morgan', 'power': 68, 'element': 'water'}]
    spells = ['heal', 'freeze', 'darkness', 'earthquake']

    print("Testing artifact sorter...")
    artifacts_sorted: list[dict[str, Any]] = artifact_sorter(artifacts)
    for i in range(1, len(artifacts_sorted)):
        print(f"{artifacts_sorted[i-1]["name"]}", end=" ")
        print(f"({artifacts_sorted[i-1]["power"]} power)", end=" ")
        print("comes before", end=" ")
        print(f"{artifacts_sorted[i]["name"]}", end=" ")
        print(f"({artifacts_sorted[i]["power"]})")
    print("")

    print("Testing mage >= 65 power...")
    mages_filtered = power_filter(mages, 65)
    for mage in mages_filtered:
        print(f"{mage["name"]} : {mage["power"]} power")
    print("")

    print("Testing spell transformer...")
    spells_transformed = spell_transformer(spells)
    for word in spells_transformed:
        print(f"{word}")
    print("")

    print("Testing min/max mage's power level...")
    stats: dict[str, int | float] = mage_stats(mages)
    print(f"Most powerful mage’s power level : {stats["max_power"]}")
    print(f"Least powerful mage’s power level : {stats["min_power"]}")
    print(f"Average power level : {stats["avg_power"]}")
    print("")


if __name__ == "__main__":
    lambda_spells()
