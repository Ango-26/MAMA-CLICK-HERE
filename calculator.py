
# this program makes a calculator, I mean ofc this isnt like top tier casio calulcators we have at home
# however it is GUI enabled therefore its like interactable.


# import all packages and necessary methods from the tkinter module
from tkinter import *

#  declare the expression variable, in this case as you can see I have made the
#  content in between the speech marks, zilch, as this will be "appended" later per se
expression = ""


# Function to update expression
# in the text entry box
def press(num):
	# making the variable expression global enables me to tap into/access it anywhere throughout the code
	# it is more useful as this prevents me from referencing this again and again, which is a waste of time,
	global expression

	# concatenation of string allows the flow of equation to be continued
	# for example, if the expression box is empty, I press a '3' and then a '+' , it will still be continued,
	# and not run in a new equation, basically, after I press '=' , does it only stop concatenating.
	# if you don't know what concatenating is, it's basically linking things together in chains/series.
	expression = expression + str(num)

	# updates the expression, because as the expression concatenayes, the equation must keep pace and hence we use:
	equation.set(expression)  #passing through expression as one of the kwargs.


# Function to make the equal button give the answer to said expression or equation in question
def equalpress():
	# Try and except statement is used for handling the errors like zero or division error (7/0 or smth)

	# Put that code inside the try block
	# which may generate the error
	try:

		global expression

		# the eval function evaluates the expression
		# and str function convert the data type into string. String is basically the stuff in ""

		total = str(eval(expression))

		equation.set(total)

		# initialize the expression variable
		# by empty string
		expression = ""

	# if error is generate then handle
	# by the except block
	except:

		equation.set(" error ")
		expression = ""


# Function to clear the contents

def clear():
	global expression
	expression = ""
	equation.set("")
	# as the function name, suggests, this code enables the program to clear the expression field and wipe out
	# traces of previous expression, therefore enabling user to type in new


# All code under this driver is the main code and this is where the program will be run
if __name__ == "__main__":
	# create a tkinter window
	window = Tk()

	# background colour of the pop-up window is now light green
	window.configure(background="light green")

	# makes the title of the window pop-up called Calculator
	window.title("Calculator")

	# this line of code sets the djmensions if the display window.
	window.geometry("290x150")


	# this code creates an instance of the StringVar class
	equation = StringVar()

	# create the text entry box for
	# showing the expression .
	expression_field = Entry(window, textvariable=equation)

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	expression_field.grid(columnspan=4, ipadx=70)

	# create a Buttons and place at a particular
	# location inside the root window .
	# when user press the button, the command or
	# function affiliated to that button is executed .


	# I decided to use the grid method rather than pack as it was more useful and it was more easy to position
	# the needed requirements, entry fields, and etc.
	button1 = Button(window, text=' 1 ', fg='black', bg='red',
					 command=lambda: press(1), height=1, width=7)
	button1.grid(row=2, column=0)

	button2 = Button(window, text=' 2 ', fg='black', bg='red',
					 command=lambda: press(2), height=1, width=7)
	button2.grid(row=2, column=1)

	button3 = Button(window, text=' 3 ', fg='black', bg='red',
					 command=lambda: press(3), height=1, width=7)
	button3.grid(row=2, column=2)

	button4 = Button(window, text=' 4 ', fg='black', bg='red',
					 command=lambda: press(4), height=1, width=7)
	button4.grid(row=3, column=0)

	button5 = Button(window, text=' 5 ', fg='black', bg='red',
					 command=lambda: press(5), height=1, width=7)
	button5.grid(row=3, column=1)

	button6 = Button(window, text=' 6 ', fg='black', bg='red',
					 command=lambda: press(6), height=1, width=7)
	button6.grid(row=3, column=2)

	button7 = Button(window, text=' 7 ', fg='black', bg='red',
					 command=lambda: press(7), height=1, width=7)
	button7.grid(row=4, column=0)

	button8 = Button(window, text=' 8 ', fg='black', bg='red',
					 command=lambda: press(8), height=1, width=7)
	button8.grid(row=4, column=1)

	button9 = Button(window, text=' 9 ', fg='black', bg='red',
					 command=lambda: press(9), height=1, width=7)
	button9.grid(row=4, column=2)

	button0 = Button(window, text=' 0 ', fg='black', bg='red',
					 command=lambda: press(0), height=1, width=7)
	button0.grid(row=5, column=0)

	plus = Button(window, text=' + ', fg='black', bg='red',
				  command=lambda: press("+"), height=1, width=7)
	plus.grid(row=2, column=3)

	minus = Button(window, text=' - ', fg='black', bg='red',
				   command=lambda: press("-"), height=1, width=7)
	minus.grid(row=3, column=3)

	multiply = Button(window, text=' * ', fg='black', bg='red',
					  command=lambda: press("*"), height=1, width=7)
	multiply.grid(row=4, column=3)

	divide = Button(window, text=' / ', fg='black', bg='red',
					command=lambda: press("/"), height=1, width=7)
	divide.grid(row=5, column=3)

	equal = Button(window, text=' = ', fg='black', bg='red',
				   command=equalpress, height=1, width=7)
	equal.grid(row=5, column=2)

	clear = Button(window, text='Clear', fg='black', bg='red',
				   command=clear, height=1, width=7)
	clear.grid(row=5, column='1')

	Decimal= Button(window, text='.', fg='white', bg='black',
					command=lambda: press('.'), height=1, width=7)
	Decimal.grid(row=6, column=0)
	# start the GUI
	window.mainloop()
