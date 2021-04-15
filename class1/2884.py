H, M = map(int, input().split())
M -= 45

if M < 0:
    H -= 1
    if H < 0:
        print(24+H, 60+M)
    else:
        print(H, "{}".format(60+M))
else:
    print(H, M)




