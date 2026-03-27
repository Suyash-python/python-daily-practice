def count_occurrence(numbers, target):
    count = 0

    for num in numbers:
      if num == target:
        count += 1

    return count

print(count_occurrence([1,2,2,3,2],2))
