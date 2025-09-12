#   WeightConvert.py
WeightStr = input("请输入带有符号的重量值:")
if  WeightStr[-1]in ["kg"]:
    pd = (eval (Weight[0:-1]))*2.20462
    print("转化后的重量是{：.3f}pd".format(pd))
elif  WeightStr[-1] in ["pd"]:
    kg = (eval (weight[0:-1]))*0.453592
    print("转化后的重量是{:.3f}kg".format(kg))
else 
print("输入格式错误")
                  

