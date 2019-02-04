from classifier import *
from nltk import bigrams, trigrams
from math import pow



'''
A sample script that classifies tweets into different award types
'''

tweet_dict_by_award = get_and_classify_tweets('./data/gg2013.json', 1000000, gg2013_categories)

print("Printing results to file...")
date = datetime.datetime.now()
file = open(dir_path + '/output/' + str(date) + ".txt", "w")

d_view = [ (v,k) for k,v in tweet_dict_by_award.iteritems() ]
for twts, award in d_view:
    file.write("\n\n\n%s:\n" % award.encode('ascii', 'ignore'))
    for t in twts:
        file.write("%s\n" % t.encode('ascii', 'ignore'))
file.close()