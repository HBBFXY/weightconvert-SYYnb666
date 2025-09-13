# 获取用户输入
weight = input()
# 定义转换系数
kg_to_pd = 2.2046
# 判断输入是千克还是磅
if weight.endswith('kg'):
    kg = float(weight[:-2])
    pd = kg * kg_to_pd
    print(f"对应的英制重量为{pd:.3f}磅")
elif weight.endswith('pd'):
    pd = float(weight[:-2])
    kg = pd / kg_to_pd
    print(f"对应的公制重量为{kg:.3f}公斤"
