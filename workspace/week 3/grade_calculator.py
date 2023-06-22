#grade_calculator.py
score = eval(input("Your score is "))
if score >=  0 and score <= 100:
    print("---Result---")
if score >= 80:
    print("Grade A!!")
elif (score < 80) and (score > 60):
    print("Grade B!!")
else:
    print("Grade C!!")
