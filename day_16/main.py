# from turtle import Turtle, Screen
#
# timmy = Turtle()  # new object called timmy
# timmy.shape("turtle")  # change the shape to turtle
# timmy.color("medium purple")  # change color to medium purple
# timmy.forward(100)  # move forward by 100
#
#
# window = Screen()  # create new screen object
# window.title("Timmy the Turtle")  # set title to screen
# print(window.canvwidth)  # print screen height
# print(window.canvheight)  # print screen width
# window.exitonclick()  # widow exits only when clicked

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squitle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table.align)
print(table)
