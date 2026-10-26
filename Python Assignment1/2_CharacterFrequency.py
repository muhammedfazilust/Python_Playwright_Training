s = "programming"
frequency = {}

for i in s:
    frequency[i] = frequency.get(i,0)+1

print(frequency)