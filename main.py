# 获取用户输入
weight_input = input()
# 提取数字部分和单位部分
num = float(weight_input[:-2])
unit = weight_input[-2:]
# 定义转换系数
kg_to_pd = 2.2046
pd_to_kg = 1 / kg_to_pd
# 根据单位进行转换并输出结果
if unit == "kg":
    result = num * kg_to_pd
    print(f"对应的英制重量为{result:.3f}磅")
elif unit == "pd":
    result = num * pd_to_kg
    print(f"对应的公制重量为{result:.3f}公斤")

