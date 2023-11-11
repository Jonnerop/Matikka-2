from matplotlib import pyplot as plt, patches
import numpy as np
from fractions import Fraction as fr

fig = plt.figure()
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')

plt.xticks([-1, 0, 1], minor=True)
plt.yticks([-1, 0, 1])

pist_xy = np.array([np.pi/6, np.pi/4])
varit = np.array(['red', 'green'])
x = np.cos(pist_xy)
y = np.sin(pist_xy)
plt.scatter(x, y, color=varit, marker='X')

plt.annotate(r'$(\frac{\pi}{6})$',
             xy=(np.cos(np.pi/6), np.sin(np.pi/6)), xycoords='data',
             xytext=(+30, +0), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))

additional_angles = np.radians([30, 45, 60, 90, 120, 150, 180, 270])
x_additional = np.cos(additional_angles)
y_additional = np.sin(additional_angles)

plt.scatter(x_additional, y_additional, color='blue', marker='o')

for angle in additional_angles:
    angle_degrees = np.round(np.degrees(angle), decimals=2)
    plt.annotate(fr'{angle_degrees}$^\circ$',
                 xy=(np.cos(angle), np.sin(angle)), xycoords='data',
                 xytext=(+30, 25), textcoords='offset points', fontsize=10, color='blue',
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))

plt.show()
