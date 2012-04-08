''' Prompts the user for their name. Checkes to see if the name matches the stored
username in var USERNAME. If it does it prints out hello username.
'''

# Set username we are checking for. Change this to your name.
YOURNAME = 'Kellan'

# Ask the user to type in their name.
username = raw_input('Please tell me your name: ')

# Test if our built in name matches what the user typed.
if (username == YOURNAME):
    print "Welcome %s" % (username)