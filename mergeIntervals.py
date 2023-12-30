def merge_intervals(intervals):
    # sort the intervals
    for i in range(len(intervals)-1):
        if intervals[i][0] > intervals[i+1][0]:
            intervals[i], intervals[i+1] = intervals[i+1], intervals[i]

    outputlist = [intervals[0]]
    for i, j in intervals[1:]:
        end = outputlist[-1][1]
        if i < end:
            outputlist[-1][1] = max(end, j)
        else:
            outputlist.append([i, j])
    return outputlist

# Test case
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))  # Should return [[1,6], [8,10], [15,18]]
#print(merge_intervals([[1, 4], [4, 5]]))  # Should return [[1,5]]
#print(merge_intervals([[6, 8], [1, 9], [2, 4], [4, 7]]))  # Should return [[1,9]]
#print(merge_intervals([[1, 3], [7, 9], [4, 6]]))  # Should return [[1,3], [4,6], [7,9]]
# print(merge_intervals([]))  # Should return []
print(merge_intervals([[2, 3], [5, 5]]))
