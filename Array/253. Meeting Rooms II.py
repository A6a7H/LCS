class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        used_rooms = 0
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        end_pointer = 0
        start_pointer = 0

        while start_pointer < L:
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                used_rooms -= 1
                end_pointer += 1
            used_rooms += 1    
            start_pointer += 1   

        return used_rooms

#more logic
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        used_rooms = 0
        start = sorted([i[0] for i in intervals])
        end = sorted(i[1] for i in intervals)

        p1 = p2 = 0
        result = 0
        count = 0

        start.sort()
        end.sort()

        while p1 < len(start) and p2 < len(end):
            if start[p1] < end[p2]:
                count += 1
                p1 += 1
                result = max(result, count)
            else:
                count -= 1
                p2 += 1
                result = max(result, count)
        return result