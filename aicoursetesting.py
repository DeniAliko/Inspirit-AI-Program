import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

gdp = pd.Series([264.50, 250.07, 248.84, 242.83], ["Czechia", "Iraq", "Oh no my car is gone", "Portugal"])
# print(gdp)

animal_dict = {
     'Animal' : ["Hamster", "Alligator", "Hamster","Cat", "Snake", "Cat","Hamster", "Cat", "Cat", "Snake", "Hamster", "Hamster", "Cat", "Alligator"],
     'Age' : [1,9,4,13,14,10,2,4,14,7,14,2,1,7],
     'Weight': [7,13,8,12,11,8,10,14,9,11,10,10,9,14],
     'Length' : [8,6,9,1,8,9,5,6,6,6,5,3,4,5]
}

animal = pd.DataFrame(animal_dict)
# print(animal)
# print(pd.unique(animal["Animal"]))
# print(animal.describe(include=[np.number]))
# print(animal[animal["Weight"] > 10])

animal_groups = animal.groupby("Animal")
# print(animal_groups['Weight'].mean())

plt.plot([1,2,3,4],[1,4,9,16]) # plt.plot([x-coordinates], [y-coordinates])
# plt.show()

plt.plot([1,2,3,4],[1,4,9,16]) # plt.plot([x-coordinates], [y-coordinates])
plt.title("First Plot")
plt.xlabel("X Label")
plt.ylabel("Y Label")
# plt.show()

height = np.array([167, 170, 149, 165, 155, 180, 166, 146, 159, 185, 145, 168, 172, 181, 169])
weight = np.array([86,74,66,78,68,79,90,73,70,88,66,84, 67, 84, 77])

#We can set the limit (lower, upper) for the x-axis and the y-axis using xlim and ylim, respectively.
plt.xlim(140, 200)
plt.ylim(60,100)
#A scatterplot can be generated through .scatter(x,y)
plt.scatter(height,weight)
plt.title("Comparing Height vs. Weight")
plt.xlabel("Height")
plt.ylabel("Weight")
# plt.show()

animal_length = [8,6,9,1,8,9,5,6,6,6,5,3,4,5]
animal_weight = [7,13,8,12,11,8,10,14,9,11,10,10,9,14]
plt.scatter(animal_length, animal_weight)
plt.title("Animal length vs weight")
plt.xlabel("length")
plt.ylabel("weight")
# plt.show()