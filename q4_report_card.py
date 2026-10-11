scores = {"Ali": 18, "Sara": 19.90, "Reza": 9, "Mina": 14, "Omid": 11.5 , "Neda":16}
passed=[]
total_score=0

for name, score in scores.items():
    
    if score >= 17:
        print(f"{name} great with this score {score}.")
    elif score>=14 and score<17:
        print(f"{name} good with this score {score}.")
    elif score>=10 and score<14:
        print(f"{name} passed with this score {score}.")
    else:
        print(f"{name} fail with this score {score}.")

    if score >=10:
        passed.append(name)
        total_score+=score

average_score=total_score/len(passed)

print("Number of students who passed:", len(passed))
print("Average score of passed students:", average_score)

top_student=max(scores, key=scores.get)
print(f"The top student is {top_student} with a score of {scores[top_student]}.")
