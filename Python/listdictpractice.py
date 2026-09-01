scores = [80, 60 ,90, 20, 100]
count = 0
for score in scores:
    if score >= 60:
        count += 1
print(f"有{count}個及格")