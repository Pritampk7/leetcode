def mergeOverlappingIntervals(intervals):
    for i in range(len(intervals) - 1):
        if intervals[i][0] > intervals[i + 1][0]:
            intervals[i], intervals[i + 1] = intervals[i + 1], intervals[i]

    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        if merged[-1][1] >= intervals[i][0]:
            merged[-1][1] = intervals[i][1]
        else:
            merged.append(intervals[i])
    return merged


intervals = [[1, 3], [2, 6], [8, 10], [15, 18], [13,15]]
print(intervals)
print(mergeOverlappingIntervals(intervals))

def mergeOverlappingIntervals(intervals):
    if not intervals:
        return []

    # Sort the intervals based on the start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        # If the current interval overlaps with the last merged interval
        if intervals[i][0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            merged.append(intervals[i])
    return merged
intervals = [[1, 3], [2, 6], [8, 10], [15, 18], [13,15]]
print(mergeOverlappingIntervals(intervals))
