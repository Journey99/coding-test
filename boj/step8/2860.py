# 달팽이는 올라가고 싶다
a, b, v = map(int, input().split())
day = (v-a) // (a-b)

if (v -a) % (a-b) == 0:
    print(day+1) # 첫날 올라간거 +1
else:
    print(day+2) # 나머지가 있다는건 다음날 아침에 한번더 올라가야 한다는거