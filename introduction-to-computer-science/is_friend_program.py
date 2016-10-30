# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'

#First method
def is_friend(a):
    if a[0] == 'D':
        return True
    else:
        return False

# Second Method
def is_friend(name):
    return name[0] == 'D' or name[0] == 'N'

print is_friend('Diane')
#>>> True

print is_friend('Fred')
print is_friend('Nancy')
#>>> False