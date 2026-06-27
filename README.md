
# OPERATOR
| Fonction            | Équivalent | Usage principal               |
| ------------------- | ---------- | ----------------------------- |
| `itemgetter("x")`   | `obj["x"]` | Dictionnaires, listes, tuples |
| `attrgetter("x")`   | `obj.x`    | Objets                        |
| `methodcaller("m")` | `obj.m()`  | Appel de méthode              |
| `add(a, b)`         | `a + b`    | Arithmétique                  |
| `sub(a, b)`         | `a - b`    | Arithmétique                  |
| `mul(a, b)`         | `a * b`    | Arithmétique                  |
| `truediv(a, b)`     | `a / b`    | Arithmétique                  |
| `floordiv(a, b)`    | `a / b`    | Arithmétique                  |
| `mod(a, b)`         | `a % b`    | Arithmétique                  |
| `pow(a, b)`         | `a ** b`   | Arithmétique                  |
| `eq(a, b)`          | `a == b`   | Comparaison                   |
| `ne(a, b)`          | `a != b`   | Comparaison                   |
| `lt(a, b)`          | `a < b`    | Comparaison                   |
| `le(a, b)`          | `a <= b`   | Comparaison                   |
| `gt(a, b)`          | `a > b`    | Comparaison                   |
| `ge(a, b)`          | `a >= b`   | Comparaison                   |
| `and_(a, b)`        | `a and b`  | Opérateurs Logiques           |
| `or_(a, b)`         | `a or b`   | Opérateurs Logiques           |
| `xor(a, b)`         | `a xor b`  | Opérateurs Logiques           |
| `not_(a, b)`        | `a not b`  | Opérateurs Logiques           |

---

# FUNCTOOLS
| Fonction         | Usage                                                 |
| ---------------- | ----------------------------------------------------- |
| `wraps`          | Écriture de décorateurs                               |
| `cache`          | Mémorisation infinie                                  |
| `lru_cache`      | Cache limité                                          |
| `partial`        | Pré-remplir des arguments                             |
| `reduce`         | Réduction d'une séquence                              |
| `cmp_to_key`     | Compatibilité avec anciennes fonctions de comparaison |
| `singledispatch` | Polymorphisme selon le type                           |
