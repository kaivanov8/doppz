# дополнительное практическое задание по модулю

grades_ = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students_ = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}
grades_[0] = sum(grades_[0])/len(grades_[0])
grades_[1] = sum(grades_[1])/len(grades_[1])
grades_[2] = sum(grades_[2])/len(grades_[2])
grades_[3] = sum(grades_[3])/len(grades_[3])
grades_[4] = sum(grades_[4])/len(grades_[4])
sorted_students = sorted(students_)
students_book = {sorted_students [0] :grades_[0],
                 sorted_students [1] :grades_[1],
                 sorted_students [2] :grades_[2],
                 sorted_students [3] :grades_[3],
                 sorted_students [4] :grades_[4]}
print(students_book)
