import matplotlib.pyplot as plt
import numpy as np

max_age = int(input("Enter the Maximum Age Of Survival Of The Species "))
class_length = int(input("Enter The Class Length "))
total_intervals = max_age//class_length

def list_multiplication(a1, a2):
    result = [0 for i in range(total_intervals)]
    result = np.dot(a1, a2)
    return result

No = []
for i in range(0, max_age, class_length):
    if i+class_length<=max_age:
        ele = int(input("Enter The total population in the age group {}-{} ".format(i,i+class_length)))
    No.append(ele)
current_population = sum(No)

Br = []
Dr = []
print("\n")
for i in range(0, max_age, class_length):
    ele = float(input("Enter the Birth Rate of age group {}-{} ".format(i,i+class_length)))
    Br.append(ele)
print("\n")
for i in range(0, max_age-class_length, class_length):
    ele = float(input("Enter the Death Rate of age group {}-{} ".format(i,i+class_length)))
    Dr.append(ele)
Dr.append(0)
L = [[None for i in range(total_intervals)] for j in range(total_intervals)]
count = 0
L[0] = Br
for i in range(1,total_intervals):
    for j in range(0,total_intervals):
        if i==j+1:
            L[i][j] = Dr[count]
            count += 1
        else:
            L[i][j] = 0

print("\n")
N = int(input("Enter the Number of Years"))
population = []
for i in range(N):
    year = list_multiplication(L,No)
    population.append(int(sum(year)))
    No = year

print("\n")
print("Total Population after {} Years = {}".format(N, int(sum(No))))


xpoints = np.array([i for i in range(N)])
ypoints = np.array(population)

plt.plot(xpoints, ypoints)
plt.show()








