#while_continue.py
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(">",i)
else:
  print("Outside while")