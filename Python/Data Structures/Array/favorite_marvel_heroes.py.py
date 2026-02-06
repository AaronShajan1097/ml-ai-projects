heros=['spider man','thor','hulk','iron man','captain america']

#1
print(f"1. Length of List Heros: {len(heros)}")

#2
heros.append("black panther")
print(f"2. {heros}")

#3
heros.pop()
print(f"3. {heros}")
heros.insert(3, "black panther")
print(f"{heros}")

#4
heros.remove('thor')
heros.remove('hulk')
print(f"4. {heros}")

#5
heros.sort()
print(f"5. {heros}")