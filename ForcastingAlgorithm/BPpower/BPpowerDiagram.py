import matplotlib as mpl
#mpl.use('Agg')

import matplotlib.pyplot as plt
#plt.style.use('bmh')

fig, ax = plt.subplots(1, 1)
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.show()