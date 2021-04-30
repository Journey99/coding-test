A, B, V = map(int, input().split())
# 시간에러!
# day = 0
# n = 0
# while True:
#     day += 1
#     n += A
#     if n >= V:
#         print(day)
#         break
#     else:
#         n -= B

res = (V -A) // (A-B)  # A칸만큼 올라갈수 있는 일수
if (V - A) % (A -B) == 0:
    print(res + 1)
else: print(res + 2)

