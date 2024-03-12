import itertools

# 定义两个集合
set1 = {1, 2, 3}
set2 = {'a', 'b', 'c'}

# 计算笛卡尔积
cartesian_product = list(itertools.product(set1, set2))

# 输出结果
print(cartesian_product)