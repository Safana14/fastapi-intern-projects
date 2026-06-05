age=int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


for i in range(1,6):
    print(i) 


count=1
while count<=5:
    print(count)
    count+=1


fruits=["apple","banana","orange"]
print(fruits)
fruits.append("grape")
print(fruits)


colors=("red","blue","green")
print(colors)
print(colors[0])


student={
    "name":"Safana",
    "age":21,
    "course":"MCA"
}
print(student)
print(student["name"])



squares=[]
for i in range(1,6):
    squares.append(i * i)

print(squares)


square_dict={i: i*i for i in range(1, 6)}
print(square_dict)