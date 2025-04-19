# With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]
def generate_series(a):
    count = a if a % 2 != 0 else a - 1
    series = []
    for i in range(count):
        series.append(2 * i + 1)
    return series
a = int(input("Enter a value for a: "))
result = generate_series(a)
print("Output:", ", ".join(map(str, result)))
