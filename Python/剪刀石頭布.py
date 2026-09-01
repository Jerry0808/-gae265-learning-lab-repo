import random

user_rock_paper_scissors = int(input("請出拳:0代表出剪刀，1代表出石頭，2代表出布"))
savelist = ["剪刀","石頭","布"]
pc_rock_paper_scissors = random.randint(0,2)
print(f"你出了{savelist[user_rock_paper_scissors]}")
print(f"電腦出{savelist[pc_rock_paper_scissors]}")
if user_rock_paper_scissors == (pc_rock_paper_scissors+1) % 3:
    print("你贏了")
elif pc_rock_paper_scissors == (user_rock_paper_scissors + 1) % 3:
    print("你輸了")
else:
    print("平手")