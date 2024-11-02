from tkinter import*
import webbrowser 

janela=Tk()
janela.configure(bg="red")
label=Label(janela, text="Ver todos os dados\nde Diamantino Massaqui", width=20, font=("Ivy 8 bold"), bg="red")
label.pack(padx=0, pady=30)
#Encontar a conta do Facebook
def facebook():
    webbrowser.open_new(r"https://www.facebook.com/diamantinomassaquoi.fam")
  
 #Encontar a conta do Instagram...  
def instagram():
     webbrowser.open_new(r"https://www.instagram.com/diamantino_massaqui?igsh=YzljYTk1ODg3Zg==")
 #Encontar a conta do whatzaap....
def whatzap():
     webbrowser.open_new(r"https://wa.me/qr/K7UPQZOO7AKRP1")
     
 #Encontar a conta do github
def github():
    webbrowser.open_new(r"https://github.com/settings/profile")
    
def ver():
    label.place(x=5000000, y=0)
    b.place(x=5000000, y=0)
    l1=Label(janela, text="Aceda as contas  a baixo para, mas informações....\n E não se esqueça de mim seguir.", bg="red", fg="white", font=("Ivy 7 bold"))
    l1.pack(pady=20)    
    
    #Botao para Facebook.....
    b0=Button (janela,text="https:facebook.com",width=20,bg="red", fg="blue" ,command=facebook, font=("Gloria 10 bold"))
    b0.pack(pady=70)
    
    #Botao para o Instagram.....
    bi=Button (janela,text="https:Instagram.com",width=20,bg="red", fg="blue" ,command=instagram, font=("Gloria 10 bold"))
    bi.pack(pady=80)

#botao whatzaap......
    bw=Button (janela,text="https:whatzaap.com",width=20,bg="red", fg="blue" ,command=whatzap, font=("Gloria 10 bold"))
    bw.pack(pady=90)
 #botao github....
    bg=Button (janela,text="https:github.com",width=20,bg="red", fg="blue" ,command=github, font=("Gloria 10 bold"))
    bg.pack(pady=100)
    
    

#Boato para aceder as minnhas contas....
b=Button(janela, width=8, text="Ver", bg="green", fg="white", font=("Ivy 8 bold"), command=ver)
b.pack(padx=0, pady=50)



janela.mainloop()