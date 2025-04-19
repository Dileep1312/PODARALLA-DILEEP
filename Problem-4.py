#Get the total count of number listed in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]
def count_multiples(numbers):
    result = {}
    for i in range(1, 10):
        count = sum(1 for num in numbers if num % i == 0)
        result[i] = count
    return result


numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]


multiples_count = count_multiples(numbers)
print("Output:")
print(multiples_count)
