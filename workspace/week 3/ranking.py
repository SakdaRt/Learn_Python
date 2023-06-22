#ranking.py
result = """---Condition---
(score < 101) and (score >= 80) is Rank S!!
(score < 80) and (score >= 60) is Rank A!!
(score < 60) and (score >= 40) is Rank B!!
(score < 40) and (score >= 0) is Rank C!!
"""
print(result)
score = eval(input("Your score is "))
if score >=  0 and score <= 100:
    if score >= 80:
        print("- Rank S!!")
    elif (score < 80) and (score >= 60):
        print("- Rank A!!")
    elif (score < 60) and (score >= 40):
        print("- Rank B!!")
    else:
        print("- Rank C!!")
else:
    if(score < 0):
        print("Can not calculate score lower than 0")
    if(score > 100):
        print("Can not calculate score more than 100")