from tkinter import *
from PIL import ImageTk, Image
import time

root = Tk()
root.title("Slideshow")
root.geometry("600x400")
root.resizable(False, False)
image_size = (597, 300)
global current_image_index

welcome_image = ImageTk.PhotoImage(
    Image.open("image_viewer/assets/welcome.jpg").resize(image_size)
)
frame = Frame(root)
frame.grid(row=0, column=0)

welcome_label = Label(frame, image=welcome_image)
welcome_label.grid(row=0, column=0, columnspan=5)





def selected(type):
    global image_list
    global frame,current_image_index
    image_list = []
    image_size = (597, 300)
    for i in range(1, 6):
        if type == "nature":
            exec(
                f'image_list.append(ImageTk.PhotoImage(Image.open("image_viewer/assets/nature/img{i}.jpg").resize({image_size})))'
            )
        if type == "animal":
            exec(
                f'image_list.append(ImageTk.PhotoImage(Image.open("image_viewer/assets/animal/img{i}.jpg").resize({image_size})))'
            )
        if type == "city":
            exec(
                f'image_list.append(ImageTk.PhotoImage(Image.open("image_viewer/assets/city/img{i}.jpg").resize({image_size})))'
            )
        if type == "abstract":
            exec(
                f'image_list.append(ImageTk.PhotoImage(Image.open("image_viewer/assets/abstract/img{i}.jpg").resize({image_size})))'
            )
        if type == "food":
            exec(
                f'image_list.append(ImageTk.PhotoImage(Image.open("image_viewer/assets/food/img{i}.jpg").resize({image_size})))'
            )
        else:
            pass
    def next(number):

        global frame
        global button_previous,button_next
        frame.grid_forget()
        frame.grid(row=0,column=0)

        image_window = Label(frame,image=image_list[number-1])
        image_window.grid(row=0,column=0,columnspan=5)

        button_previous = Button(frame, text="<<", command= lambda: previous(number-1))
        button_next = Button(frame, text=">>", command= lambda: next(number+1))
        button_sildeShow = Button(frame, text="Silde Show", state=DISABLED)
        button_exit = Button(frame, text="Exit", command=root.quit)

        if number == 5:
            button_next = Button(frame,text=">>", state=DISABLED)

        button_previous.grid(row=2, column=0)
        button_sildeShow.grid(row=2, column=1, columnspan=2, pady=10, ipadx=40)
        button_exit.grid(row=2, column=3)
        button_next.grid(row=2, column=4)
    


    def previous(number):
        global frame
        global button_previous,button_next
        frame.grid_forget()
        frame.grid(row=0,column=0)

        image_window = Label(frame,image=image_list[number-1])
        image_window.grid(row=0,column=0,columnspan=5)

        button_previous = Button(frame, text="<<", command= lambda: previous(number-1))
        button_next = Button(frame, text=">>", command= lambda: next(number+1))
        button_sildeShow = Button(frame, text="Silde Show", state=DISABLED)
        button_exit = Button(frame, text="Exit", command=root.quit)

        if number == 1:
            button_previous = Button(frame,text=">>", state=DISABLED)

        button_previous.grid(row=2, column=0)
        button_sildeShow.grid(row=2, column=1, columnspan=2, pady=10, ipadx=40)
        button_exit.grid(row=2, column=3)
        button_next.grid(row=2, column=4)
    def slideshow():
        global current_image_index
        global image_list

        
        if current_image_index == len(image_list):
            current_image_index = 0
        first_label.configure(image=image_list[current_image_index])
        current_image_index += 1
        

        button_previous = Button(frame, text="<<", state=DISABLED)
        button_next = Button(frame, text=">>", state=DISABLED)
        button_sildeShow = Button(frame, text="Silde Show", state=DISABLED)
        button_exit = Button(frame, text="Exit", command=root.quit)

        button_previous.grid(row=2, column=0)
        button_sildeShow.grid(row=2, column=1, columnspan=2, pady=10, ipadx=40)
        button_exit.grid(row=2, column=3)
        button_next.grid(row=2, column=4)
        
        root.after(2000, slideshow)
        
        

    current_image_index = 0

    frame.grid_forget()

    frame.grid(row=0, column=0)
    first_label = Label(frame, image=image_list[current_image_index])
    first_label.grid(row=0, column=0, columnspan=5)
    button_previous = Button(frame, text="<<", state=DISABLED)
    button_next = Button(frame, text=">>", command= lambda: next(2))
    button_sildeShow = Button(frame, text="Silde Show", command=slideshow)
    button_exit = Button(frame, text="Exit", command=root.quit)


    button_previous.grid(row=2, column=0)
    button_sildeShow.grid(row=2, column=1, columnspan=2, pady=10, ipadx=40)
    button_exit.grid(row=2, column=3)
    button_next.grid(row=2, column=4)



    



nature = Button(frame, text="Nature", command=lambda: selected("nature"))
animal = Button(frame, text="Animal", command=lambda: selected("animal"))
city = Button(frame, text="City", command=lambda: selected("city"))
abstract = Button(frame, text="Abstract", command=lambda: selected("abstract"))
food = Button(frame, text="Food", command=lambda: selected("food"))

nature.grid(row=1, column=0, pady=10, ipadx=25)
animal.grid(row=1, column=1, pady=10, ipadx=25)
city.grid(row=1, column=2, pady=10, ipadx=25)
abstract.grid(row=1, column=3, pady=10, ipadx=25)
food.grid(row=1, column=4, pady=10, ipadx=25)


button_previous = Button(frame, text="<<", state=DISABLED)
button_next = Button(frame, text=">>", state=DISABLED)
button_sildeShow = Button(frame, text="Silde Show", state=DISABLED)
button_exit = Button(frame, text="Exit", command=root.quit)

button_previous.grid(row=2, column=0)
button_sildeShow.grid(row=2, column=1, columnspan=2, pady=10, ipadx=40)
button_exit.grid(row=2, column=3)
button_next.grid(row=2, column=4)


root.mainloop()
