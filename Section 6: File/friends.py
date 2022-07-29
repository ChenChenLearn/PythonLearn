# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll have their name to 'nearby_friends.txt'

#hint: readLines()
friends = input(
    'Enter three friend names, separated by commas (no spaces, please: ').split(',')  # 变成list of string
#['Rolf', 'Jose', 'Charlie']
people = open('people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()
                 ]  # [line1, line2, line3, line4]
people.close()

friends_set = set(friends)  # turn list to set
people_nearby_set = set(people_nearby)
friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friend_file = open('nearby_friends.txt', 'w')
for friend in friends_nearby_set:
    print(f'{friend} is nearby! Meet up with them')
    nearby_friend_file.write(f'{friend}\n')
nearby_friend_file.close()


# 注意: Any whiteSpace, tab, new line character, space, that get removed from the start
# to ehd end of the string. -> strip() method does
