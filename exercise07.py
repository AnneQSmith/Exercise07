scores = open('scores.txt')
score_dict = {}
temp_list = []
for line in scores:
    temp_list = line.split(':')
    temp_list[1].rstrip('\n')
    if score_dict.get([temp_list[0]])