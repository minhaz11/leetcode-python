from collections import Counter
def topKFrequent(nums,k) :
        count = Counter(nums).most_common(k)
        freq = [i[0] for i in count]
        return freq
print(topKFrequent([1,1,1,2,2,3],2))