from Stack import BasicStack
from Queue import BasicQueue

#Stack useing two queue
Q1 = BasicQueue()
Q2 = BasicQueue()

# input value to a stack
Q1.enqueue("Q")
Q1.enqueue("U")
Q1.enqueue("E")
Q1.enqueue("U")
Q1.enqueue("E")

print(Q1.data)

for i in range(Q1.size()-1):
    Q2.enqueue(Q1.dequeue())

print("Removed content from Stack: ",Q1.dequeue())

print(Q1.data)
Q1=Q2
print(Q1.data)
print(Q2.data)
Q2=BasicQueue()
print(Q2.data)