#while_break.py
i = 0
while i < 6:
    i += 1
    if i == 4:
        break
    print(">",i)
else:
  print("Outside while")