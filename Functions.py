def studentdeets(nameVar,ageVar):
    if len(nameVar) > ageVar:
        print('Your name has more letters than years you have lived')
        nameGtAge = True   
    else:
        print('You are older in years than your name has letters')
        nameGtAge = False   
    return {'name':nameVar,'age':ageVar,'namelengtthanage':nameGtAge}
    
studentName = str(input('Put in a name: '))
studentAge  = int(input('Type in your Age: '))
funcReturn = studentdeets(studentName,studentAge)
print(funcReturn)
    
    
      