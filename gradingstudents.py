grades_count = int(raw_input().strip())
grades = []
for _ in xrange(grades_count):
    grades_item = int(raw_input().strip())
    if grades_item<38:
        grades.append(grades_item)
    else:
        if (((grades_item//5)+1)*5-grades_item<3):
            grades.append(((grades_item//5)+1)*5)
        else:
            grades.append(grades_item)
for i in range (len(grades)):
    print(grades[i])
    
