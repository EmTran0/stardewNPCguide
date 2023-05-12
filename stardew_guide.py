from tkinter import *
from PIL import Image, ImageTk
from npc_data import *


window = Tk()
window.title('Stardew Valley NPC Guide')
window.geometry('550x511')
window.resizable(width=False, height=False)
window.configure(bg='#feffff')
main_frame = Frame(window, width=545, height=309, bg='#feffff')
main_frame.grid(padx=2, pady=1)


def character_choice(i) -> None:
    """
    Function to set up initial character info page and allow user to choose character profiles
    :param i: index of information from npc_data file
    """
    global portrait_1
    global character_image
    main_frame['bg'] = characters[i]['extra'][1]
    character_name['text'] = i
    character_name['bg'] = characters[i]['extra'][1]
    character_birthday['text'] = characters[i]['birthday'][0]
    character_birthday['bg'] = characters[i]['extra'][1]

    image = characters[i]['extra'][0]
    character_image = Image.open(image)
    character_image = character_image.resize((260, 260))
    character_image = ImageTk.PhotoImage(character_image)
    portrait_1 = Label(window, image=character_image, bg=characters[i]['extra'][1])
    portrait_1.place(x=130, y=45)

    char_loves['text'] = characters[i]['gifts'][0]
    char_likes['text'] = characters[i]['gifts'][1]
    char_hates['text'] = characters[i]['gifts'][2]
    char_interests_text['text'] = characters[i]['interests'][0]
    marriage_text['text'] = characters[i]['marriage'][0]

    character_birthday.lift()


# GUI text setup

character_name = Label(main_frame, text='Character name', anchor='center', font='Arial 20 bold', fg='#37374a')
character_name.place(x=175, y=5)

character_birthday = Label(main_frame, text='Birthday', anchor='center', font='Arial 11 bold', fg='#37374a')
character_birthday.place(x=10, y=5)
character_birthday.lift()

character_gifts = Label(window, text='Gifts', font='Arial 20', bg='#feffff', fg='#37374a')
character_gifts.place(x=125, y=315)

char_loves = Label(window, text='Loves:', font='Arial 11', bg='#feffff', fg='#37374a')
char_loves.place(x=125, y=360)

char_likes = Label(window, text='Likes:', font='Arial 11', bg='#feffff', fg='#37374a')
char_likes.place(x=125, y=395)

char_hates = Label(window, text='Hates:', font='Arial 11', bg='#feffff', fg='#37374a')
char_hates.place(x=125, y=430)

char_interests = Label(window, text='Interests', font='Arial 20', bg='#feffff', fg='#37374a')
char_interests.place(x=270, y=315)

char_interests_text = Label(window, text='enter stuff here', font='Arial 11', bg='#feffff', fg='#37374a')
char_interests_text.place(x=270, y=360)

marriage_text = Label(window, text='Marriage? ', font='Arial 11', bg='#feffff', fg='#37374a')
marriage_text.place(x=185, y=475)

# all character Icons/images were obtained from sticknpg.com

character_image_1 = Image.open('Images/leah.png')
character_image_1 = character_image_1.resize((40, 40))
character_image_1 = ImageTk.PhotoImage(character_image_1)

character_icon_1 = Button(window, text='Leah', command=lambda: character_choice('Leah'), width=90,
                          image=character_image_1,
                          padx=5, compound=LEFT,
                          font='Arial, 12', bg='#feffff', fg='#37374a')
character_icon_1.place(x=15, y=70)

character_image_2 = Image.open('Images/haley.png')
character_image_2 = character_image_2.resize((40, 40))
character_image_2 = ImageTk.PhotoImage(character_image_2)

character_icon_2 = Button(window, text='Haley', command=lambda: character_choice('Haley'), width=90,
                          image=character_image_2,
                          padx=5, compound=LEFT,
                          font='Arial, 12', bg='#feffff', fg='#37374a')
character_icon_2.place(x=15, y=130)

character_image_3 = Image.open('Images/evelyn.png')
character_image_3 = character_image_3.resize((40, 40))
character_image_3 = ImageTk.PhotoImage(character_image_3)

character_icon_3 = Button(window, text='Evelyn', command=lambda: character_choice('Evelyn'), width=90,
                          image=character_image_3,
                          padx=5, compound=LEFT,
                          font='Arial, 12', bg='#feffff', fg='#37374a')
character_icon_3.place(x=15, y=200)

character_image_4 = Image.open('Images/pam.png')
character_image_4 = character_image_4.resize((40, 40))
character_image_4 = ImageTk.PhotoImage(character_image_4)

character_icon_4 = Button(window, text='Pam', command=lambda: character_choice('Pam'), width=90,
                          image=character_image_4, padx=5,
                          compound=LEFT,
                          font='Arial, 12', bg='#feffff', fg='#37374a')
character_icon_4.place(x=15, y=260)

character_image_5 = Image.open('Images/elliot.png')
character_image_5 = character_image_5.resize((40, 40))
character_image_5 = ImageTk.PhotoImage(character_image_5)

character_icon_5 = Button(window, text='Elliott', command=lambda: character_choice('Elliott'), width=90,
                          image=character_image_5,
                          padx=5, compound=LEFT,
                          font='Arial, 12', bg='#feffff', fg='#37374a')
character_icon_5.place(x=400, y=70)

character_image_6 = Image.open('Images/sebastian.png')
character_image_6 = character_image_6.resize((40, 40))
character_image_6 = ImageTk.PhotoImage(character_image_6)

character_icon_6 = Button(window, text='Seb', command=lambda: character_choice('Sebastian'), width=90,
                          image=character_image_6,
                          padx=5, compound=LEFT,
                          font='Arial, 12', bg='#feffff', fg='#37374a')
character_icon_6.place(x=400, y=130)

character_image_7 = Image.open('Images/harvey.png')
character_image_7 = character_image_7.resize((40, 40))
character_image_7 = ImageTk.PhotoImage(character_image_7)

character_icon_7 = Button(window, text='Harvey', command=lambda: character_choice('Harvey'), width=90,
                          image=character_image_7,
                          padx=5, compound=LEFT,
                          font='Arial, 12', bg='#feffff', fg='#37374a')
character_icon_7.place(x=400, y=200)

character_image_8 = Image.open('Images/lewis.png')
character_image_8 = character_image_8.resize((40, 40))
character_image_8 = ImageTk.PhotoImage(character_image_8)

character_icon_8 = Button(window, text='Lewis', command=lambda: character_choice('Lewis'), width=90,
                          image=character_image_8,
                          padx=5, compound=LEFT,
                          font='Arial, 12', bg='#feffff', fg='#37374a')
character_icon_8.place(x=400, y=260)

# Initial character profile page

character_choice('Leah')
window.mainloop()
