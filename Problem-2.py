# With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]10
def generate_series(a):
    series = []
    for i in range(a):
        series.append(2 * i + 1)
    return series


a = int(input("Enter a value for a: "))
result = generate_series(a)

print("Output:", ", ".join(map(str, result)))
