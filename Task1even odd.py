numbers = [2,5,7,8,10,13]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2== 0:
        even_count += 1
    else:
        odd_count += 1

print("Even =", even_count)
print("Odd =", odd_count)