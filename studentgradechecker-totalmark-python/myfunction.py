from collections import OrderedDict

def getTotalMarks(input_text) :
    total_marks = ""
    lines = input_text.split("newline")
    module_marks = []
    total_marks = 0
    for line in lines :
        line_array = line.split(',')
        module_marks_array = OrderedDict([("module",line_array[0]),("marks",line_array[1])])
        if int(line_array[1]) <= 100 and int(line_array[1]) >= 0 :
            module_marks.append(int(line_array[1]))           
        else :
            return 'you have entered an incorrect value, module score must not be more than 100 or less than 0'

    for i in module_marks:
                total_marks = sum(module_marks)
                
                return str(total_marks)
    