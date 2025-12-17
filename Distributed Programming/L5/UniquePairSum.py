def unique_pair_sum(numbers, target):
    pairs = set()
    seen = set()

    for num in numbers:
        diff = target - num
        if diff in seen:
            pairs.add(tuple((num, diff)))
        seen.add(num)

    print(pairs)


nums = []
l = int(input("Enter list length:"))
for i in range(0, l):
    n = int(input("Enter number: "))
    nums.append(n)

trgt = int(input("Enter target number: "))
unique_pair_sum(nums, trgt)