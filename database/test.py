import random

sim = []

def generate(count, complete):
    for i in range (0, count):
        temp = [0, 0, 0, 0, 0]
        add(complete, temp)
        sim.append(temp)

def add(count, temp):
    for i in range (0, count):
        num = random.randint(0, 4)
        temp[num] += 1
    return temp

def check(set):
    return set[0] > 6 and set[1] > 6 and set[2] > 6 and set[3] > 6 and set[4] > 6

def get_prob(sim):
    passed = 0
    failed = 0
    for item in sim:
        if check(item):
            passed += 1
        else:
            failed += 1
    return passed/(passed + failed)

days_prob = []
'''
for i in range (0, 70):
    generate(100000, i)
    days_prob.append(get_prob(sim))
    sim = []
print(days_prob)
'''
result = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00098, 0.00463, 0.01324, 0.02672, 0.04749, 0.0764, 0.10774, 0.14663, 0.19112, 0.23747, 0.28612, 0.33463, 0.38962, 0.43811, 0.48611, 0.53056, 0.57514, 0.61831, 0.65443, 0.69276, 0.72242, 0.75453, 0.78093, 0.80788, 0.82814, 0.84532, 0.86931, 0.88156, 0.89813, 0.90951, 0.92065, 0.93102, 0.94012, 0.94751, 0.95456, 0.96024]
by_task = []
day = 0
for item in result:
    by_task.append(f'Task completed = {day}: {item}')
    day += 1
print (by_task)