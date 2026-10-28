from typing import Iterator
def float_range(start: float, stop: float, step: float) -> Iterator[float]:
    current = start

    if step == 0:
        raise ValueError("Крок не може бути нулем.")
    elif step > 0:
        while current <= stop:
            yield current
            current += step
    elif step < 0:
        while current >= stop:
            yield current
            current += step

print(list(float_range(5.0, 3.0, -0.5)))