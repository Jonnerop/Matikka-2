import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6.4 * 3, 4.8))

X = np.linspace(-3 * np.pi, 3 * np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C, label='Cosine', color='blue', linestyle='--')
plt.plot(X, S, label='Sine', color='red', linestyle='-.')

plt.legend()
plt.show()
