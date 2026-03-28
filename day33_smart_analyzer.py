def count_even_odd(numbers):
    even = 0
    odd = 0
    for num in numbers:
      if num % 2 == 0:
        even += 1
      else:
       odd += 1
    return even, odd

def list_sum(numbers):
  total = 0
  for num in numbers:
    total += num
  return total

def find_max(numbers):
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num

  return max_num

def find_min(numbers):
  min_num = numbers[0]
  for num in numbers:
    if num < min_num:
      min_num = num
  return min_num

def second_largest(numbers):
    unique = list(set(numbers))
    unique.sort()
    return unique[-2]


def unique_elements(numbers):
    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)
    return unique


def sort_list(numbers):
  n = len(numbers)
  for i in range(n):
    for j in range(0, n - i - 1):
      if numbers[j] > numbers[j + 1]: numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers

numbers = list(map(int, input("Enter numbers:").split()))          

while True:
    print("/nchoose Option:")
    print("1. Even/Odd Count")
    print("2. Sum")
    print("3. Max & Min")
    print("4. Second Largest")
    print("5. Unique Elements")
    print("6. Sort List")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
       even, odd = count_even_odd(numbers)
       print("Even:", even, "Odd:", odd)

    elif choice == 2:
      print("Sum:", list_sum(numbers))

    elif choice == 3:
       print("Max:", find_max(numbers))
       print("Min:", find_min(numbers))

    elif choice == 4:
       print("Second Largest:", second_largest(numbers))

    elif choice == 5:
       print("Unique:", unique_elements(numbers))

    elif choice == 6:
       print("Sorted:", sort_list(numbers))

    elif choice == 7:
       print("Exiting...")
       break

    else:
        print("Invalid choice!")
