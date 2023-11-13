import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6.4 * 3, 4.8))

X = np.linspace(-3 * np.pi, 3 * np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C, label='Cosine', color='blue', linestyle='--')
plt.plot(X, S, label='Sine', color='red', linestyle='-.')

plt.legend()

plt.xticks([-3*np.pi, -2*np.pi, -1*np.pi, 0, np.pi, 2*np.pi, 3*np.pi],
           ['-3π', '-2π', '-π', '0', 'π', '2π', '3π'])

plt.show()
