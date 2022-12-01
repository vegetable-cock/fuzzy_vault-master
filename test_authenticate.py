def approx_equal(a, b, epsilon):
    return abs(a - b) < epsilon


vault = [[1, 2], [3, 4], [5, 6]]
template = [[1, 8], [3, 10], [11, 12]]


def project(x):
    for point in vault:
        if approx_equal(x[0], point[0], 0.001):  # 阈值过小合法用户可能不能解锁，阈值过大安全性下降
            return [x[0], point[1]]

    return None


for p in template:
    print(project(p))

# Q = list(zip(*[project(p) for p in template if project(p) is not None]))
# print(Q)

# 理想输出的Q应该是:横纵坐标组成元组，Q是元组组成的列表。
# 当前返回值：[(1,), (2,)]
