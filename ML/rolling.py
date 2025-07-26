import random

total_rolls = 10000


count_sum_7 = 0
count_sum_2 = 0
count_sum_gt_10 = 0

for _ in range(total_rolls):
    die1 = random.randint(1, 6)  
    die2 = random.randint(1, 6)  
    total = die1 + die2         

    if total == 7:
        count_sum_7 += 1
    if total == 2:
        count_sum_2 += 1
    if total > 10:
        count_sum_gt_10 += 1


p_sum_7 = count_sum_7 / total_rolls
p_sum_2 = count_sum_2 / total_rolls
p_sum_gt_10 = count_sum_gt_10 / total_rolls

print(f"P(Sum = 7): {p_sum_7:.4f}")
print(f"P(Sum = 2): {p_sum_2:.4f}")
print(f"P(Sum > 10): {p_sum_gt_10:.4f}")
