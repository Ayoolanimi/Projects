# To create this Bank System GUI, I will be using tkinter. So let's import tkinter
from tkinter import *

# Creating a root window before creating any tkinter object is a must
root = Tk()
# In tkinter, taking the user input is done using "Entry" with the get() function and not the regular "Input" used for other python packages
entry = Entry()

# Here, we create a design for our GUI, setting the desired instruction in the text feature along with the formatting to choice
d_label = Label(text='Enter the amount you want to deposit or withdraw below\n and click the appropriate button.',
                font=('verdana', 16, 'bold'), fg='black')
# As the design for the GUI would be determined by a grid, rows and columns are used for the preferred placement of the above instruction and the columnspan indicates the length of the column to be used
d_label.grid(row=1, column=1, columnspan=5)

# Then, we go ahead to define our first function which will indicate the existing or available balance in the system. This is referred to as "self.balance" in this code
class BankSystemGUI():
    def __init__(self):
        self.balance = 10000
        self.user_input = Entry(font=('verdana', 16, 'bold'))
        self.user_input.grid(row=2, column=1, columnspan=5)

# Here, we define the deposit function and instruct the BankSystem to add the user input to the existing balance, as well as setting an instruction in the configuration value
    def deposit(self):
        d_input = eval(Entry.get(self.user_input))
        self.balance += d_input
        d_label.configure(text='Deposit Successful!! Your account balance is now ${}'.format(self.balance))

# This is similar to the previous function but the only difference is this is set for the withdrawal, thereby ibstructing tbe system to deduct the user input from the existing balance. Also, if the user inout is greater than the existing balance, the system would prompt the user to the overdraft section if the user decides to take an overdraft or not and following the defined set of instructions to either exit the operation or put the user on hold for the overdraft review
    def withdraw(self):
        d_input = eval(Entry.get(self.user_input))
        if (d_input > self.balance):
            d_label.configure(
                text='You do not have sufficient balance \nWould you like to request an overdraft? yes/no \n')
            d_input2 = Entry.get(self.user_input)
            if (d_input2 == 'yes'):
                d_label.configure(text='Your request is being reviewed')
            else:
                d_label.configure(text='Please try again later')
        else:
            self.balance -= d_input
            d_label.configure(text='Withdrawal Successful!! Your account balance is now ${}'.format(self.balance))

# Here, we call on the BankSystemGUI function to commence operation
bank = BankSystemGUI()

# We then set the button for each function, deposit and withdrawal, so as to be redirected to the line of code set for each when user clicks on the action of choice
deposit_btn = Button(text='Deposit', font=('verdana', 18, 'bold'), bg='green', command=bank.deposit, fg='black')
withdraw_btn = Button(text='Withdraw', font=('verdana', 18, 'bold'), bg='blue', command=bank.withdraw, fg='black')

# Placing the buttons takes place here, using the grid function to place the button as desired. The positions can be changed depending on how you want it to be
deposit_btn.grid(row=4, column=2)
withdraw_btn.grid(row=4, column=4)

# Mainloop() function instructs the GUI to keep running
mainloop()