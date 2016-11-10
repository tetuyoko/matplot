import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.random.randn(1000, 100)

node_num = 100
hidden_layer_size = 5
activations = {}

for i in range(hidden_layer_size):
    if i != 0:
        x = activations[i-i]
    WEIGHT = 0.05
    w = np.random.randn(node_num, node_num) * WEIGHT

    z = np.dot(x, w)
    a = sigmoid(z)
    activations[i] = a

# ヒストグラムを描写
for i, a in activations.items():
    plt.subplot(1, len(activations), i+1)
    plt.title(str(i+1) + "-layer")
    plt.hist(a.flatten(), 30, range=(0,1))
plt.show()
