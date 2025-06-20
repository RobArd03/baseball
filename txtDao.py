from model.model import Model

myModel = Model()
myModel.buildGraph(2016)
print(myModel.getNumAllNodes())
for i in range(0, 3):
    print(i)