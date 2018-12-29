
#Review of List Comprehensions
#Date 12.28.18

squares = [x for x in range(10)]
print(squares)

squares = [x**2+x for x in range(10)]
print(squares)

Rectangledom = [x+y for x in [10,30,300] for y in [10,20,30,50]]
print(Rectangledom)
print(Rectangledom.sort())
