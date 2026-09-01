#bmi : weight(kg) / height(m)^2
height = float(input("請輸入身高"))
weight = float(input("請輸入體重"))
bmi = weight/(height/100)**2
print(f"你的身高是{height}cm")
print(f"你的體重是{height}kg")
print(f"你的bmi是{bmi}")
if bmi > 25:
    print(f"太重了")
else:
    print(f"正常體重")