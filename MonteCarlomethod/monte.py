### coding: UTF-8
import numpy as np
import sys

# 試行回数
n = 1000

if len(sys.argv) > 1:
    n = int(sys.argv[1])

# 総得点
score = 0

for i in range(n):
    point = np.array([np.random.rand(),np.random.rand()])
    if np.linalg.norm(point, ord=2) <= 1:
        score += 1
    print('%06d回目のπの近似値 : %f' %(i+1,4*score/(i+1)))


