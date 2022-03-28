import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

# Functional method
plt.plot(x, y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('My graph')
#plt.show()

plt.subplot(1,2,1)
plt.plot(x,y,'r')
plt.subplot(1,2,2)
plt.plot(y,x,'b')
#plt.show()

# Object Oriented method
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x, y)
axes.set_xlabel('My new X label')
axes.set_ylabel('My new Y label')
axes.set_title('My new Title')
#fig.show()

fig1 = plt.figure()
axes1 = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig1.add_axes([0.2, 0.5, 0.4, 0.3])
axes1.plot(x,y)
axes2.plot(y,x)
axes2.set_title('SMALLER PLOT')
axes1.set_title('LARGER PLOT')
#fig1.show()

fig, axes = plt.subplots(nrows=1, ncols=2) # Tuple unpacking
plt.tight_layout()
print(type(axes))
#for current_axis in axes:
#    current_axis.plot(x, y)
axes[0].plot(x, y)
axes[0].set_title('First Plot')
axes[1].plot(x, y)
axes[1].set_title('Second Plot')
#fig.show()

# Figure size and DPI
fig = plt.figure(figsize=(8, 2))
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y)
#fig.show()

# With subplots
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8,2))
axes[0].plot(x, y)
axes[1].plot(y, x)
#fig.show()

# How to add legends
fig_new = plt.figure()
#ax1 = fig_new.add_axes([0, 0, 1, 1])
ax1 = fig_new.add_subplot(111) # 111 as the default value
ax1.plot(x, x**2, label='X Square', color='blue', linewidth=1, linestyle='--', marker='o', markerfacecolor='orange', markeredgecolor='yellow')
ax1.plot(x, x**3, label='X Cubed', color='green', alpha=0.5, linestyle='-.', marker='+', markersize=15, markeredgewidth=3)
ax1.set_title('My Graph')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.legend(loc=0)

# Control over axis appearance and Plot range
ax1.set_xlim([0, 1])
ax1.set_ylim([0, 1])

fig_new.show()
# Saving a figure
fig_new.savefig('my_picture.jpg', dpi=300)

# Special Plot Types


