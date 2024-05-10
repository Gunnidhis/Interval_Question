# Question : You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] 
#            and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

#            Return the intersection of these two interval lists.(leetcode Problem- 986)

def intervalIntersection(firstList, secondList):
    i, j = 0, 0
    start, end = 0, 1
    result = list()
    while i < len(firstList) and j < len(secondList):
        if (firstList[i][start] >= secondList[j][start] and firstList[i][start] <= secondList[j][end]) or (secondList[j][start] >= firstList[i][start] and secondList[j][start] <= firstList[i][end]):
            temp_start = max(firstList[i][start], secondList[j][start])
            temp_end = min(firstList[i][end], secondList[j][end])

            result.append([temp_start, temp_end])

        if firstList[i][end] <secondList[j][end]:
            i += 1
        else:
            j += 1

    return result

if __name__=="__main__":
    firstList = [[0,2],[5,10],[13,23],[24,25]]
    secondList = [[1,5],[8,12],[15,24],[25,26]]
    res = intervalIntersection(firstList,secondList)
    print(res)
