def solve():
    n = int(input())
    arr = [int(i) for i in input().split()]
    segmennt_started, segment_ended, start, end, num_segs  = False, False, 0, n-1, 0
    for i in range(n-1):
        if segment_ended and arr[i] > arr[i+1]: num_segs += 1 #extra unordered possible segments
        if not segmennt_started and arr[i] > arr[i+1]:
            start = i
            segmennt_started = True
        elif not segment_ended and segmennt_started and arr[i] < arr[i+1]:
            end = i 
            segment_ended = True
    if num_segs > 0: return 'no' # more than one seqment needs to be reversed
    if not segmennt_started: return 'yes \n1 1' # already sorted
    if start == 0 and end == n-1: return 'yes \n' + f'{start+1} {end+1}' # sorted descendingly
    if end == n-1:
        if arr[end] < arr[start-1]: return 'no' # incresing then decreasing and last elem in the decreasing part is less than the first elem of the increasing part
    else:
        if arr[start] > arr[end+1]: return 'no' # decreasing then increasing and first elem in the decreasing part is bigger than the first elem of the increasing part
    return 'yes \n' + f'{start+1} {end+1}' 

print(solve())