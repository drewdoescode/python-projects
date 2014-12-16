print('welcome to the quiz game!')
name = input('<what is your name?')
print('ok',name,'lets get started')
print('''
what is the capital of North Carolina?
''')



answer = input().title()
if answer == 'Raleigh':
    print('GOOD JOB')
elif answer in ['Duhram','Charlotte']:
    print('some people think that... but its wrong, try again')
elif answer == 'applepie':
    print('APPLEPIE')
else:
    print(' nope try again')

    
