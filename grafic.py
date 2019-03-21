import matplotlib.pyplot as plt
n = list(range(1, 6))
m = [x**2 for x in n]
#plt.scatter(n, m, c = m, cmap=plt.cm.Reds, edgecolor='none', s=40)
plt.plot(n,m,c='red', linewidth=5)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([1, 5, 0, 25])
plt.show()
#plt.savefig('grafic.png', bbox_inches='tight')