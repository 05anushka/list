# student_marks=[12,13,14,15,16,17]
# lenght=len(student_marks)
# index=(0)
# total_marks=0
# while index<len(student_marks):
#    total_marks=student_marks[index]+total_marks
#    index=index+1
# print(total_marks)


marks=[55,64,45,49,50,37,18,47,48,69,70]
length=len(marks)
index=0
more_than50=0
less_than50=0
equal_marks=0
while index<len(marks):
    if marks[index]>50:
        more_than50=more_than50+1
    elif marks[index]==50:
        equal_marks=equal_marks+1
    else:
        less_than50=less_than50+1
index=index+1
print(more_than50)
print(less_than50)
print(equal_marks)




        
        



