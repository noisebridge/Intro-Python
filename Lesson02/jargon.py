''' In this weeks homework we are going to modify our code this week to use
our new string formating skills. We need to create a box in the center of the 
screen that says Welcome to Jargon.
'''
welcomeMsg = "Welcome to Jargon"
msgSize = len(welcomeMsg)
screenWidth = 80



BoxTop = '+{0}+'.format('-' * (msgSize +2))
msgRow = '|{0:^{1}}|'.format(welcomeMsg, msgSize+2)

print '{0:^{1}}'.format(BoxTop, screenWidth)
print '{0:^{1}}'.format(msgRow, screenWidth)
print '{0:^{1}}'.format(BoxTop, screenWidth)