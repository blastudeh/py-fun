import math


class Calculator:
    """A singleton calculator that understands numbers and number names."""

    _instance = None

    def __new__(cls):
        # Create one calculator, then reuse it for every Calculator() call.
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    _words = {}

    # Each row lists the names for zero through nine.
    for _language in (
        "zero one two three four five six seven eight nine",
        "null eins zwei drei vier fünf sechs sieben acht neun",
        "cero uno dos tres cuatro cinco seis siete ocho nueve",
        "ноль один два три четыре пять шесть семь восемь девять",
        "零 一 二 三 四 五 六 七 八 九",
    ):
        for _value, _word in enumerate(_language.split()):
            _words[_word] = _value

    _words.update({
        "i": 1,
        "ii": 2,
        "iii": 3,
        "iv": 4,
        "v": 5,
        "vi": 6,
        "vii": 7,
        "viii": 8,
        "ix": 9,
        "x": 10,
    })

    @classmethod
    def _number(cls, value):
        """Convert supported input into an integer or decimal number."""
        if isinstance(value, bool):
            raise TypeError("Use a number, not True or False.")

        if isinstance(value, (int, float)):
            result = value
        elif isinstance(value, str):
            text = value.strip().casefold()

            if text in cls._words:
                return cls._words[text]

            try:
                result = int(text)
            except ValueError:
                try:
                    result = float(text)
                except ValueError:
                    raise ValueError(
                        f"Unknown number: {value!r}"
                    ) from None
        else:
            raise TypeError("Use a number or a supported number name.")

        if isinstance(result, float) and not math.isfinite(result):
            raise ValueError("The number must be finite.")

        return result

    def add(self, a, b):
        return self._number(a) + self._number(b)

    def sub(self, a, b):
        return self._number(a) - self._number(b)

    def mul(self, a, b):
        return self._number(a) * self._number(b)

    def div(self, a, b):
        return self._number(a) / self._number(b)

    def factorize(self, n):
        """Return prime factors; 1 has no prime factors."""
        n = self._number(n)

        if n < 1 or int(n) != n:
            raise ValueError("Factorization requires a positive whole number.")

        n = int(n)
        factors = []
        divisor = 2

        while divisor * divisor <= n:
            while n % divisor == 0:
                factors.append(divisor)
                n //= divisor

            divisor = 3 if divisor == 2 else divisor + 2

        if n > 1:
            factors.append(n)

        return factors