# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.


def find_second(search_string, target_string):
    first_occurance = search_string.find(target_string)
    return search_string.find(target_string, first_occurance+1)

def find_second_short(search_string, target_string):
    return search_string.find(target_string, search_string.find(target_string)+1)

danton = "De l'audace, encore de l'audace, toujours de l'audace"
print find_second(danton, 'audace')

print find_second_short(danton, 'audace')


#>>> 25

#twister = "she sells seashells by the seashore"
#print find_second(twister,'she')
#>>> 13