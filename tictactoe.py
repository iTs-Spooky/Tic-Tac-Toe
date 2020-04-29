import tkinter.messagebox
from tkinter import*

root=Tk()
root.geometry("1350x750+0+0")
root.title("Tic Tac Toe")
root.configure(background='cadet blue')

Tops=Frame(root, bg='cadet blue', pady=2, width=1350, height=100,relief =RIDGE)
Tops.grid(row=0,column=0)

lblTitle=Label(Tops,font=('arial',50,'bold'), text="Tic Tac Toe Game",bd=21,bg='cadet blue',fg='cornsilk',justify=CENTER)
lblTitle.grid(row=0,column=0)

MainFrame= Frame(root, bg='powder blue', bd=10, width=1350, height=600, relief=RIDGE)
MainFrame.grid(row=1,column=0)

LeftFrame= Frame(MainFrame, bd=10, width=750, height=550, pady=2, padx=10, bg='cadet blue', relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame= Frame(MainFrame, bd=10, width=560, height=500, padx=10, pady=2, bg='cadet blue', relief=RIDGE)
RightFrame.pack(side=LEFT)

RightFrame1= Frame(RightFrame, bd=10, width=560, height=200, padx=10, pady=2, bg='cadet blue', relief=RIDGE)
RightFrame1.grid(row=0,column=0)

RightFrame2= Frame(RightFrame, bd=10, width=560, height=200, padx=10, pady=2, bg='cadet blue', relief=RIDGE)
RightFrame2.grid(row=1,column=0)

PlayerX=IntVar()
PlayerO=IntVar()

buttons=StringVar()
##Gobal variable####
click=TRUE

###checker function###
def checker(buttons):
    global click
    if buttons["text"] == " " and click==True: 
        buttons["text"]="X"
        click=False
        scorecalculator()
    elif buttons["text"] == " " and click==False:
        buttons["text"]="O"
        click=True
        scorecalculator()
####checker function ends####

#### Reset game####
def Reset_game():
    button1['text']=" "
    button2['text']=" "
    button3['text']=" "
    button4['text']=" "
    button5['text']=" "
    button6['text']=" "
    button7['text']=" "
    button8['text']=" "
    button9['text']=" " 
     
    button1.configure(background="gainsboro")
    button2.configure(background="gainsboro")
    button3.configure(background="gainsboro")
    button4.configure(background="gainsboro")
    button5.configure(background="gainsboro")
    button6.configure(background="gainsboro")
    button7.configure(background="gainsboro")
    button8.configure(background="gainsboro")
    button9.configure(background="gainsboro")
####Reset game ends####

###New game###
def New_game():
    Reset_game()
    PlayerX.set(0)
    PlayerO.set(0)
###New Game ends###

###check win####
def scorecalculator(): 
    ### Check win for x####
    if(button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X"):
        button1.configure(background="powder blue")
        button2.configure(background="powder blue")
        button3.configure(background="powder blue")
        a=int(PlayerX.get())
        score=(a + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","You have won a game")

    elif(button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X"):
        button4.configure(background="powder blue")
        button5.configure(background="powder blue")
        button6.configure(background="powder blue")
        a=int(PlayerX.get())
        score=(a + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","You have won a game")

    elif(button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X"):
        button7.configure(background="powder blue")
        button8.configure(background="powder blue")
        button9.configure(background="powder blue")
        a=int(PlayerX.get())
        score=(a + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","You have won a game")  

    elif(button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X"):
        button1.configure(background="purple")
        button5.configure(background="purple")
        button9.configure(background="purple")
        a=int(PlayerX.get())
        score=(a + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","You have won a game")

    elif(button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"):
        button3.configure(background="purple")
        button5.configure(background="purple")
        button7.configure(background="purple")
        a=int(PlayerX.get())
        score=(a + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","You have won a game")

    elif(button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X"):
        button1.configure(background="green")
        button4.configure(background="green")
        button7.configure(background="green")
        a=int(PlayerX.get())
        score=(a + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","You have won a game") 

    elif(button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X"):
        button2.configure(background="green")
        button5.configure(background="green")
        button8.configure(background="green")
        a=int(PlayerX.get())
        score=(a + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","You have won a game")

    elif(button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"):
        button3.configure(background="green")
        button6.configure(background="green")
        button9.configure(background="green")
        a=int(PlayerX.get())
        score=(a + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","You have won a game")  

         ### Check win for x ends####   

         ### Check win for O####
    if(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O"):
        button1.configure(background="green")
        button2.configure(background="green")
        button3.configure(background="green")
        a=int(PlayerO.get())
        score=(a + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O","You have won a game")
    elif(button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O"):
        button4.configure(background="green")
        button5.configure(background="green")
        button6.configure(background="green")
        a=int(PlayerO.get())
        score=(a + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O","You have won a game")
    elif(button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O"):
        button7.configure(background="green")
        button8.configure(background="green")
        button9.configure(background="green")
        a=int(PlayerO.get())
        score=(a + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O","You have won a game")    
    elif(button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O"):
        button1.configure(background="purple")
        button5.configure(background="purple")
        button9.configure(background="purple")
        a=int(PlayerO.get())
        score=(a + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O","You have won a game")
    elif(button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"):
        button3.configure(background="purple")
        button5.configure(background="purple")
        button7.configure(background="purple")
        a=int(PlayerO.get())
        score=(a + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O","You have won a game")
    elif(button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O"):
        button1.configure(background="grey")
        button4.configure(background="grey")
        button7.configure(background="grey")
        a=int(PlayerO.get())
        score=(a + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O","You have won a game")   
    elif(button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O"):
        button2.configure(background="grey")
        button5.configure(background="grey")
        button8.configure(background="grey")
        a=int(PlayerO.get())
        score=(a + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O","You have won a game")   
    elif(button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O"):
        button3.configure(background="grey")
        button6.configure(background="grey")
        button9.configure(background="grey")
        a=int(PlayerO.get())
        score=(a + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O","You have won a game")   
         ### Check win for x ends####   
##check win ends###

######Player scores#######
lblPlayerX=Label(RightFrame1, font=('arial',40,'bold'), text="PlayerX :", padx=2,pady=2,bg="cadet blue")
lblPlayerX.grid(row=0, column=0, sticky=W)

txtPlayerX=Entry(RightFrame1, font=('arial',40,'bold'),bd=2,fg="Black", textvariable= PlayerX, width=14,
                  justify=LEFT).grid(row=0,column=1)


lblPlayerO=Label(RightFrame1, font=('arial',40,'bold'), text="PlayerO :", padx=2,pady=2,bg="cadet blue")
lblPlayerO.grid(row=1, column=0, sticky=W)

txtPlayerO=Entry(RightFrame1, font=('arial',40,'bold'),bd=2,fg="Black", textvariable= PlayerO, width=14,
                  justify=LEFT).grid(row=1,column=1)
####Player score ends######

##### New Game and Reset Button####
btnReset = Button(RightFrame2, text="Reset",font=('arial',40,'bold'), height=1, width=20, command=Reset_game)
btnReset.grid(row=2,column=0, padx=6, pady=11)

btnNewgame= Button(RightFrame2, text="New Game",font=('arial',40,'bold'), height=1, width=20,command=New_game    )
btnNewgame.grid(row=3,column=0, padx=6, pady=10)
##### New Game and Reset Button ends####

#####Main game board######
button1= Button(LeftFrame, text=" ", font=("Times 26 bold"), height=3, width=8, bg='gainsboro', command=lambda:checker(button1))
button1.grid(row=1,column=0, sticky= S+N+E+W)

button2= Button(LeftFrame, text=" ", font=("Times 26 bold"), height=3, width=8, bg='gainsboro', command=lambda:checker(button2))
button2.grid(row=1,column=1, sticky= S+N+E+W)

button3= Button(LeftFrame, text=" ", font=("Times 26 bold"), height=3, width=8, bg='gainsboro', command=lambda:checker(button3))
button3.grid(row=1,column=2, sticky= S+N+E+W)

button4= Button(LeftFrame, text=" ", font=("Times 26 bold"), height=3, width=8, bg='gainsboro', command=lambda:checker(button4))
button4.grid(row=2,column=0, sticky= S+N+E+W) 

button5= Button(LeftFrame, text=" ", font=("Times 26 bold"), height=3, width=8, bg='gainsboro', command=lambda:checker(button5))
button5.grid(row=2,column=1, sticky= S+N+E+W)

button6= Button(LeftFrame, text=" ", font=("Times 26 bold"), height=3, width=8, bg='gainsboro', command=lambda:checker(button6))
button6.grid(row=2,column=2, sticky= S+N+E+W)

button7= Button(LeftFrame, text=" ", font=("Times 26 bold"), height=3, width=8, bg='gainsboro', command=lambda:checker(button7))
button7.grid(row=3,column=0, sticky= S+N+E+W)

button8= Button(LeftFrame, text=" ", font=("Times 26 bold"), height=3, width=8, bg='gainsboro', command=lambda:checker(button8))
button8.grid(row=3,column=1, sticky= S+N+E+W)

button9= Button(LeftFrame, text=" ", font=("Times 26 bold"), height=3, width=8, bg='gainsboro', command=lambda:checker(button9))
button9.grid(row=3,column=2, sticky= S+N+E+W)
#### Main Game board ends####


root.mainloop()