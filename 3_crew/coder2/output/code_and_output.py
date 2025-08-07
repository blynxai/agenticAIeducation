def calculate_series(num_terms):
    total = 0.0
    for n in range(num_terms):
        term = (-1)**n / (2 * n + 1)
        total += term
    return total * 4

# Calculate the series for the first 10,000 terms
result = calculate_series(10000)

# Output the result
print(f'Output: {result}')