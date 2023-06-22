#grade_calculator_2.py
result = """---Condition---
(score < 101) and (score >= 80) is Grade A!!
(score < 80) and (score >= 60) is Grade B!!
(score < 60) and (score >= 0) is Grade C!!
"""
print(result)
score = eval(input("Your score is "))
if score >=  0 and score <= 100:
    if score >= 80:
        print("- Grade A!!")
    elif (score < 80) and (score >= 60):
        print("- Grade B!!")
    else:
        print("- Grade C!!")
else:
    if(score < 0):
        print("Can not calculate score lower than 0")
    if(score > 100):
        print("Can not calculate score more than 100")