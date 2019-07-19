story = """The %s jumped over a %s %s.
Then the %s decided to stop being so %s
 and take up a hobby: %s . """

print("Enter a noun")
#get user input
firstNoun = raw_input()
print("Enter a adjective")
firstAdjective = raw_input()

print("Enter another noun")
secondNoun = raw_input()

print("Enter another noun")
thirdNoun = raw_input()

print("Enter an adjective")
firstAdjective = raw_input()

print("Enter a verb")
firstVerb = raw_input()

#print """The %s jumped over a %s %s. Then the %s decided to stop being so %s and take up a hobby: %s .""" % (firstNoun,firstAdjective,secondNoun,thirdNoun,firstAdjective,firstVerb)
print story % (firstNoun,firstAdjective,secondNoun,thirdNoun,firstAdjective,firstVerb)
