#Exercise 7
#In this directory, you will find a text file, scores.txt, containing a series of local restaurant 
#ratings. Each line looks like this:

#Restaurant Name:Rating
# out the ratings in alphabetical order by restaurant



#TODOs:
#Open the file

scores = open('scores.txt')
#
# Read entries line by line; assign to dictionary as key value pairs
# 
# Restaurante name will be keys, rating is value
# use some sorting method to sort
#print

rest_dict = {}
for line in scores:
#split each line by ":"

    line_tokens = line.split(':')

#create dictionary entry for each restaurant, assign a rating value

    rest_dict[line_tokens[0]]= int(line_tokens[1])
 
    sorted_keylist = sorted(rest_dict.keys())

#print sorted_keylist

for restaurant in sorted_keylist:
    print"%s gets %d stars!" % (restaurant, rest_dict[restaurant])
