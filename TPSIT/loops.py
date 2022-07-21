def round_scores(student_scores):
    return [round(item) for item in student_scores]
def count_failed_students(student_scores):
    return sum(1 for score in round_scores(student_scores) if score <= 40)   
def above_threshold(student_scores, threshold):
    best = []
    for score in student_scores:
        if score >= threshold:best.append(score)
    return best
def letter_grades(highest):
    step = int((highest-40)/4)
    return [41 + step*i for i in range(4)]
def student_ranking(student_scores, student_names):
    rank = list()
    for i in range(len(student_scores)):
        rank.append("{}. {}: {}".format(i+1,student_names[i],student_scores[i]))
    return rank
def perfect_score(student_info):
    for student in student_info:
        if student[1] == 100:return student
    return []