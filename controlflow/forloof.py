#first excercise
# item = [40, 80, 70, 50]
# total = 0
# for item in item:
#     total += item
#     print(f"the total cashout is {total}")
#some program
# for x in range(3):
#     for y in range(3):
#      print(f"({x})({y})")
#challeng of f sharf
numbers = [5, 2, 5, 2, 2,]
for x_count in numbers:
   output = ''
   for count in range(x_count):
      output += 'x'
      print(output)
for number in range(3):
   print("Attempting to show",  number, (number + 1) * "." )
#program to find the small word in a words
numbers = (2,3,5,78)
small_number = numbers[0]
for number in numbers:
   print(number)
eligible = True
is_student = False
banker = True
if eligible and is_student:
   print("you are Good to bro")
elif eligible and not is_student:
   print("sorry you can't have a loan because you are not a student")
elif (eligible or is_student) and not banker:
   print("hi there we can help you to have some cash")
else:
   print("good bye")
