import matplotlib.pyplot as plt

f = open("fitness/output1.txt", "r")
lines = f.readlines()

x = [1 + i for i in range(len(lines))]
best_fitness = []
worst_fitness = []
mean_fitness = []
for line in lines:
    numbers = line.split(" ")
    best_fitness.append(int(numbers[0]))
    worst_fitness.append(int(numbers[1]))
    mean_fitness.append(float(numbers[2]))

plt.plot(x, mean_fitness, 'b', alpha=0.7, label='average')
plt.plot(x, worst_fitness, 'g', alpha=0.7, label='worst')
plt.plot(x, best_fitness, 'r', alpha=0.4, label='best')

plt.xlabel("generation number")
plt.ylabel("fitness")
plt.legend(loc="upper left")
plt.show()