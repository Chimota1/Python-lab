def filter_even_numbers(nums: list[int]) -> list[int]:
    result = []
    num = [num for num in nums if num % 2 == 0]
    result.extend(num)
    return result

print(filter_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))