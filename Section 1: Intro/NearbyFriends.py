nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend
# Add the name to the empty set
user_friends.add(input("Enter the name of a friend: "))

# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
print(nearby_people.intersection(user_friends))
