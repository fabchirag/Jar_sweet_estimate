from statistics import mean

# Estimate of people, how many sweets in the jar
Estimates = [1000, 232323, 4546, 300, 234, 2344, 542, 121, 444, 232, 122, 3344]
# Sorting it in ascending order
Estimates.sort()
# calculating trimmed value of length of estimate. its a float value so I have type cast it to int so it can take floor value.
tv = int(0.1*len(Estimates))
# Deleting a smallest and largest 10% values
Estimates = Estimates[tv:]
for i in range(len(Estimates)):
    print(Estimates[i])
Estimates = Estimates[:len(Estimates)-tv]
# Using a mean function defining it from library statistics
print("\nFinal calculation: ")
print(mean(Estimates))
