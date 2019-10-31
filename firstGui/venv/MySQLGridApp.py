from operator import le
import mysql.connector
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Python MySQL GUI")
# -----------------Functions--------------
def clearEditRow():
    try:
        if len(editBoxArray) != 0:
            for j in range(len(editBoxArray)):
                for i, val in enumerate(editBoxArray):
                    val.delete(0, 'end')  # remove data of textbox
                    # editBoxArray.remove(val) #remove data of array
    except ValueError as err:
        print("Error: {0}".format(err))


def createButtons():
    buttonBoxArray.clear()

    obj = myArray[len(myArray) - 1]
    arr = ["Save", "Delete", "Clear"]
    for j in range(3):
        btn = Button(root, text=arr[j], textvariable=arr[j], fg="green")
        btn.bind("<Button-1>", onClick)
        btn.grid(row=obj.grid_info().get("row") + 1, column=j)
        buttonBoxArray.append(btn)

    buttonBoxArray.append(btn)


def createEditRow(record):
    clearEditRow()
    createButtons()

    length = myArray[len(myArray) - 1]

    for index in range(len(record)):
        txtvalue = StringVar()
        txtvalue.set(str(record[index]))

        editbox = Entry(root, textvariable=txtvalue)
        editbox.grid(row=length.winfo_x(), column=index)
        editBoxArray.append(editbox)
        # messagebox.showinfo("Info", str(value))


def doEntrySelected(e):
    row = e.widget.grid_info().get('row')
    col = e.widget.grid_info().get('column')
    record = data[row]
    # print(row, col)

    # e.widget.grid_remove() #remove column
    e.widget.configure(foreground="red")
    # e.widget.grid_info().__

    # for index in range(record):
    #     print(index)
    #     myArray[(index+row)].configure(background="gray", foreground="red")
    # print("location = "+str(index+col))
    # print(e.widget.get())
    # print("Text Length = " + str(e.widget.index(e.y)))
    deleteEditRow()
    createEditRow(record)


def doFocusIn(e):
    print(e.widget.get())
    # e.widget.configure(state=DISABLED)
    e.widget.configure(background="gray", foreground="red")


def loadDt():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="12345678",
        database="order_db"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM custdetail")
    return mycursor.fetchall()


def save():
    for arr in editBoxArray:
        if arr.get():  # The value is not empty then print out
            print(arr.get().strip())

        messagebox.showinfo("Info", ""+str(arr.get().strip()))


def deleteEditRow():
    try:
        if len(editBoxArray) != 0:
            for j in range(len(editBoxArray)):
                for i, val in enumerate(editBoxArray):
                    editBoxArray.remove(val)
                    val.grid_remove()
    except ValueError as err:
        print("Error: {0}".format(err))


def onClick(e):
    # sum = 0
    # for idx, val in enumerate(data): sum += int(val.__getitem__(0))
    # messagebox.showinfo("Information", "ผลลัพธ์ : " + str(sum))
    button_name = e.widget.config('text')[-1]
    if button_name == "Clear":
        clearEditRow()
    if button_name == "Save":
        save()
    if button_name == "Delete":
        deleteEditRow()


# ----------------------------------------
buttonBoxArray = []
editBoxArray = []
myArray = []
data = loadDt()
rows = len(data)
cols = len(data[0])

for i in range(rows):  # Rows
    for j in range(cols):  # Columns
        # set up the values to a textvar
        textvar = StringVar()
        textvar.set(str(data[i].__getitem__(j)))

        textbox = Entry(root, textvariable=textvar, state="readonly")  # , state="readonly"
        textbox.bind("<Button-1>", doEntrySelected)
        # textbox.bind("<KeyRelease>", doFocusIn)
        textbox.grid(row=i, column=j)
        textbox.focus()
        myArray.append(textbox)
# root.geometry(str(len(myArray) + 380) + "x" + str(len(myArray) + 250))

mainloop()
