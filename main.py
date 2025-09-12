#   WeightConvert.py
WeightStr = input()
if  WeightStr[-1]in ["kg"]:
    pd = (eval (Weight[0:-1]))*2.20462
    print("对应的英制重量为{：.3f}pd镑".format(pd))
elif  WeightStr[-1] in ["pd"]:
    kg = (eval (Weight[0:-1]))*0.453592
    print("对应的公制质量为{: .3f}kg公斤".format(kg))
 else  print（）
 
                  

