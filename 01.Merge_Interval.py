# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example

# intervals = [[1,3],[2,6],[8,10],[15,18]]
# output = [[1,6],[8,10],[15,18]]
# Explanation = Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

 def merge(intervals):
   intervals.sort()
   result = list()
   for i in range(len(intervals)):
     if len(result) == 0 or result[-1][1] <intervals[i][0]:
       result.append(intervals[i])
     else:
       result[-1][1] = max(result[-1][1],intervals[i][1])
  return result

if __name__=="__main__":
  intervals = [[1,3],[2,6],[8,10],[15,18]]
  ans = merge(intervals)
  print(ans)
