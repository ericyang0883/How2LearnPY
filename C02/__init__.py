import json
from collections import Counter
from _abcoll import Sequence
path = "D:\\workspace\\PY\\How2LearnPY\\usagov_bitly_data2013-05-17-1368832207.txt"
records = [json.loads(line) for line in open(path)]
#print records[0]['tz']
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
#print time_zones[:10]



def get_count(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x]= 1
    return counts

counts = get_count(time_zones)
#print counts.items()
#print '\n'

def top_counts(count_dict, n = 10):
    #print count_dict.items()
    #print '\n'
    value_key_pairs = [(count,tz) for tz,count in count_dict.items()]
    #value_key_pairs = count_dict.items()
    value_key_pairs.sort()
    #print value_key_pairs
    #print '\n'
    return value_key_pairs[-n:]
#print top_counts(counts)
#print counts
#print '\n'

counts = Counter(time_zones)
print counts.most_common(10)



