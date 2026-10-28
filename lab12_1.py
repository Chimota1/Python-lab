def sort_by_age(people: list[dict]) -> list[dict]:
    return sorted(people, key=lambda p: p['age'])

print(sort_by_age([
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Eve", "age": 35},
]))