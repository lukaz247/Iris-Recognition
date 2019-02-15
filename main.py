import matplotlib.pyplot as plt

plt.grid()

prim = list(map(float, input('Input accordingly, seperated by comas:\nsepal length in cm, sepal width in cm, petal length in cm, petal width in cm \n').split(',')))
#prim = User inputted flower iris
iris = {"Iris-setosa" : [],"Iris-versicolor" : [],"Iris-virginica" : []}
#Initializing a dictionary with these three types
iris_types = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
#Added to avoid multiple elifs
data = open('iris.data', 'r').read().split('\n')

for row in data:
    row = row.split(',')
    try: iris[row[4]].append(list(map(float, [row[0],row[1],row[2],row[3]])))
    except IndexError : ''

setosa = iris["Iris-setosa"]
versi = iris["Iris-versicolor"]
virg = iris["Iris-virginica"]

def distance(x):
    plt.scatter(x[0] + x[1], x[2] + x[3], color=c)
    r1 = abs(x[0] - prim[0])
    r2 = abs(x[1] - prim[1])
    r3 = abs(x[2] - prim[2])
    r4 = abs(x[3] - prim[3])
    return abs(sum([r1,r2,r3,r4])) 

c = 'red'
setosa_close = min(list(map(distance, setosa)))

c = 'green'
versi_close = min(list(map(distance, versi)))

c = 'blue'
virg_close = min(list(map(distance, virg)))

closest = [setosa_close, versi_close, virg_close]
numofclose = closest.index(min(closest))

plt.scatter(prim[0] + prim[1], prim[2] + prim[3], color='purple')

plt.ylabel('Blue = Iris Virginica \nGreen = Iris Versicolor \nRed = Iris Setosa')
plt.xlabel('Your flower belongs in ' + iris_types[numofclose])

plt.show()
