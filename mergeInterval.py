def merge(intervals) :
    intervals.sort(key = lambda x : x[0])
    output = [intervals[0]]

    for first, second in intervals[1:] :
        last = output[-1][1]

        if first <= last :
            output[-1][1] = max(last,second)
        else:
            output.append([first,second])
    return output

print(merge([[1,3],[2,6],[8,10],[15,18]]))
