if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        
    first = 101.0
    second = 101.0
    
    for students in students:
        
        studentsScore = students[1]
        
        if studentsScore < first:
            
            second = first
            first = studentsScore
            
        elif studentsScore < second and studentsScore != first:
            second = studentsScore
       
    secondLowestNames = []
print(students)
print(secondLowestNames)
            
  
        
        
