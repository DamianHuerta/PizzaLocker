# Imports
from traceback import print_tb
from gui import *



# main function
def main() :
    # print("Hello world\n")
    print("Creating Objects")
    # root = Root()
    # root.mainloop()
    # canvas = Canvas()
    PizzaLockerGui = tk.Tk()
    PizzaLockerGui.geometry("500x500")
    user = tk.Button(PizzaLockerGui, state='normal', text="User",command= userButtonClick())
    # employee = tk.Button(PizzaLockerGui, state='normal', text="Client",command = employeeButtonClick())
    user.location(x=25, y=100)
    # employee.location(x=25, y=300)
    user.pack()
    # employee.pack()
    print("Finished")
    PizzaLockerGui.mainloop()
    return



if __name__ == "__main__":
    main()