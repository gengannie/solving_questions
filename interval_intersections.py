# given two lists of closed intervals, a <= x <= b [a,b]
# find intersection of closed intervals, thus [1,5] and [5, 10] intersect on [5,5] as well
# clarify what happens in these bounds

# return a list of intersections
# trick to this problem:
# stop considering the interval with min endpoint
# time complexity: O(M + N), M and N the length of the two lists given

def interval_intersections(firstList, secondList):
    len_f, len_s = len(firstList), len(secondList)
    if len_f == 0 or len_s == 0:
        return []
    ans = []
    first, second = 0
    while first < len_f and second < len_s:
        if secondList[second][0] <= firstList[first][1] and secondList[second][1] >= firstList[first][0]:
            ans.append([max(secondList[second][0], firstList[first][0]), min(firstList[first][1], secondList[second][1])])
        if firstList[first][1] < secondList[second][1]:
            first += 1
        else:
            second += 1
    return ans