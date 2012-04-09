phrase = "bow ties are cool"

# show the phrase unmodified.
print "Unmodified Phrase", phrase

#Using a string method to title case
print "Title Case: ", phrase.title()
print "Phrase has not changed", phrase

# Lets do some string replacement
phrase = phrase.replace('bow', 'neck')
print "Modified the phrase:", phrase

# Python also has built in functions that help with strings.
print "Phrase lenght:", len(phrase)
