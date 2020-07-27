student = ['A','B','C','D','E']
kor_score = [49,79,20,100,80]
math_score = [43,59,85,30,90]
eng_score = [49,79,48,60,100]

mid_term_score = [kor_score, math_score, eng_score]

student_score =[ 0 for _ in range(len(student)) ] 
# print(mid_term_score[0])
for i in range(len(mid_term_score)):
    for j in range(len(student)):
        student_score[j] += (mid_term_score[i][j])

for i in range(len(student)):
    print('{}\'s total score : {} , average score : {}'.format(student[i], student_score[i], int(student_score[i]/len(mid_term_score))))
    