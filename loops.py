# Loop 1
i = 1
while i < 7:
    print(i)
    i += 1

# Loop 2
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# Loop 3

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)