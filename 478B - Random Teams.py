#116545506	May/18/2021 13:58UTC+5.5	Shan_XD	478B - Random Teams	GNU C++17 (64)	Accepted	15 ms	0 KB

import math


def handshakes_max_min(n, m):
    # for min they should be divided equally.
    C = n // m
    e = n % m
    mint = (e) * (math.comb(C + 1, 2)) + (m - e) * (math.comb(C, 2))

    # for max one group should have all the members
    maxt = math.comb(n - m + 1, 2)

    print(str(mint)+" "+str(maxt))



n, m = map(int, input().split())
handshakes_max_min(n,m)
