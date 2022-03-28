import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,100)
y = x*2
z = x**2

plt.tight_layout()
# Exercise 1
fig = plt.figure()
axes = fig.add_subplot(111)
axes.set_title('title')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.plot(x, y)
fig.show()

fig.savefig('exercise1.jpg', dpi=400)

# Exercise 2
fig1 = plt.figure()
axes1 = fig1.add_subplot(111)
axes2 = fig1.add_axes([0.2, 0.5, .2, .2])
axes1.plot(x, y)
axes2.plot(x, y)
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes2.set_xlabel('x')
axes2.set_ylabel('y')
fig1.show()

fig1.savefig('exercise2.jpg', dpi=400)

# Exercise 3
fig2 = plt.figure()
axes1 = fig2.add_subplot(111)
axes2 = fig2.add_axes([0.2, 0.5, .4, .4])

axes1.plot(x, z)
axes1.set_xlabel('X')
axes1.set_ylabel('Z')

axes2.plot(x, y)
axes2.set_xlabel('X')
axes2.set_ylabel('Y')

axes2.set_title('zoom')
axes2.set_xlim([20, 22])
axes2.set_ylim([30, 50])

fig2.show()

fig2.savefig('exercise3.jpg', dpi=400)

# Exercise 4

fig3, axes3 = plt.subplots(nrows=1, ncols=2, figsize=(12, 2))
axes3[0].plot(x, y, color='Blue', linestyle='--')
axes3[0].set_title('First Plot')
axes3[1].plot(x, z, color='red', linestyle='-.')
axes3[1].set_title('Second Plot')

fig3.show()


fig3.savefig('exercise4.jpg', dpi=400)
