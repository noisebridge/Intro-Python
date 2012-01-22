"""
loops.py
Examples that will be used in showing loops in python. 
Created by Kellan Jacobs on 2012-01-04.
"""

# Standard While Loop
i = 0
while i < 5:
	print i
	i += 1

# While True/Break

word = 'dummy'
while word:
	word = raw_input('Enter a Word: ')
	print 'You entered: %s' % (word)

while True:
	better = raw_input('Enter a Word: ')
	if not better: break
	print 'You entered: %s' % (better)

friends = ['Tom', 'Dick', 'Harry']

for friend in friends:
	print friend

print range(10)
for i in range(10):
	if i % 2:
		continue
	print i
