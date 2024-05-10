#Author
#Gunnidhi Sharma

# question :You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent
#           the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also 
#           given an interval newInterval = [start, end] that represents the start and end of another interval.

#           Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals
#           still does not have any overlapping intervals (merge overlapping intervals if necessary).

#           Return intervals after the insertion.

#           Note that you don't need to modify intervals in-place. You can make a new array and return it.

# Example = intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]],   newInterval = [4,8]

# Output = [[1,2],[3,10],[12,16]]

#explanation = Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].



def insert(intervals,newInterval):
    start = newInterval[0]
    end = newInterval[1]
    n = len(intervals)
    i = 0
    result = list()
#step 1 :we only push the elements whose current_interval'end is less than newIntervals'start because they are not overlapping
    while i < n and  intervals[i][1] < start:
        result.append(intervals[i])
        i += 1
#Step 2 : here is merging the interval because overlapping will stop when current interval's start > newIntervals's end so merging will occur when end >= intervals[i][0]
    while i < n and end >= intervals[i][0]:
        start = min(start, intervals[i][0])
        end = max(end,intervals[i][1])
        i += 1
        
    result.append([start,end])
#step 3: last some reaming element from the intervals list
    while i < n and result[-1][1] < intervals[i][0]:
        result.append(intervals[i])
        i += 1

    return result

if __name__=="__main__":
    interval =[[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    res = insert(interval,newInterval)
    print(res)
