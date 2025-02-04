# 회의실 배정 최적화

import ast

def max_meetings(meetings):
    meetings.sort(key=lambda x: x[1])
    
    cnt = 0
    last_end_time = 0  
    
    for start, end in meetings:
        if start >= last_end_time:
            cnt += 1
            last_end_time = end  

    return cnt

meetings = ast.literal_eval(input())
print(max_meetings(meetings))