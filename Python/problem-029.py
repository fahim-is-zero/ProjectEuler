def distinct_powers(min_range, max_range):
    sequence = set()                        
    for a in range(min_range, max_range + 1):
        for b in range(min_range, max_range + 1):
            c = a**b
            sequence.add(c)
    return f"There are {len(sequence)} ditinct term"

print(distinct_powers(2,100))
