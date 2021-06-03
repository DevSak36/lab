#string
note = 'hello world'


for i in range(len(note)):
    if note[i] == ' ':
        print('เว้นวรรค')
    else :
        print('index ' + str(i)+ ': ' + note[i])
