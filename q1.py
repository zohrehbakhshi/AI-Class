import numpy as np
import matplotlib.pyplot as plt

X_train = np.array([
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 4],
    [6, 7],
    [7, 8],
    [3, 6],
    [4, 7],
    [6, 5],
    [7, 6]
])


plt.scatter(X_train[:, 0], X_train[:, 1])
plt.xlabel("Length")
plt.ylabel("Width")
plt.title("Fruits Dataset")

new_fruit = [5, 6]

plt.scatter(new_fruit[0], new_fruit[1],
            color="red", s=100)

plt.show()


distances = np.sqrt(
    np.sum((X_train - new_fruit) ** 2, axis=1)
)

print("Distances:")
print(distances)