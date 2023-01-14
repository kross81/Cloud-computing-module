from collections import OrderedDict

def getClassification(input_text) :
    total_marks = ""
    lines = input_text.split("newline")
    module_marks = []
    total_marks = 0
    for line in lines :
        line_array = line.split(',')
        module_marks_array = OrderedDict([("module",line_array[0]),("marks",line_array[1])])
        module_marks.append(int(line_array[1]))

        
    for i in module_marks:
                total_marks = sum(module_marks) 
    
    grade = total_marks / len(module_marks)

    if grade >= 70 and grade <= 100 :
        grade = "Distinction"
    elif grade >= 60 and grade <= 69 :
        grade = "Commendation"
    elif grade >= 50 and grade <= 59 :
        grade = "Pass"
    elif grade >= 30 and grade <= 39 :
        grade = "Fail"
    elif grade >= 0 and grade <= 29 :
        grade = "Low Fail"
    else : 
        grade = "Sorry there has been a problem, please make sure your score for each module is between 0 and 100. Press clear and start again"

    return grade
    