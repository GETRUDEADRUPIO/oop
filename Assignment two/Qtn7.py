
year= 2022
default='Getrude Faith'
def paul_details():
    [name,birth_year, weight]
name = input('What is your name?......')
birth_year =int(input('Enter your birth_year?......'))
if birth_year== 2002:
        if not name :
            name = default
        
        weight=int(input('What is your weight?.......'))
        print ('your name is ......',name)
        print('Born in ',birth_year)
        print('with a weight of ....',weight,'kgs')
        
        
        age =( year- birth_year)
        print('your age is ',age)
        paul_details()
