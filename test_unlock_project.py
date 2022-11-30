vault = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]


def approx_equal(a, b, epsilon):
    return abs(a - b) < epsilon


x = 2.1

for point in vault:
    if approx_equal(x, point[0], 1):  # 阈值过小合法用户可能不能解锁，阈值过大安全性下降
        print([x, point[1]])
