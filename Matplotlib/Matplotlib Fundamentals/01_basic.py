# Matplotlib Basics

from matplotlib import pyplot as plt
x = ["C","C++","JAVA","PYTHON"]
y = [50,60,70,90]
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Bar Graph",fontsize=14)
plt.bar(x,y,width=0.5,color="skyblue",edgecolor="blue",label="Popularity")
plt.legend()
plt.show()