import numpy as np  
import matplotlib.pyplot as plt 

X = np.array([[51, 55], [14, 19], [12, 13]])

# flatten
X1 = X.flatten()
print(X1)

# get elements where index..
X1[np.array([0, 2, 4])]

# filtering
print(X1 > 15)
print(X1[X1 > 15])

################################################

x = np.arange(0, 6, 0.1)

y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle = "--", label="cos")

plt.xlabel("x")
plt.ylabel("y")

plt.title('sin and cos')

plt.legend()
plt.show()