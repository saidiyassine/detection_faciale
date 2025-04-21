from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class ChatBot:
 def __init__(self,root):
  self.root=root
  self.root.title("ChatBot")
  self.root.geometry("730x620+0+0")
  self.root.bind('<Return>',self.enter_func)

  main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
  main_frame.pack()

  img_chat=Image.open('friendly-chatbot.jpg')
  img_chat = img_chat.resize((200, 70))
  self.photoimg=ImageTk.PhotoImage(img_chat)

  Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text="CHAT ME",font=('arial',30,'bold'),fg='green',bg='white')
  Title_label.pack(side=TOP)

  self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
  self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
  self.scroll_y.pack(side=RIGHT,fill=Y)
  self.text.pack()

  btn_frame=Frame(self.root,bd=4,bg='white',width=730)
  btn_frame.pack()

  label_1=Label(btn_frame,text="Type Something",font=('arial',14,'bold'),fg='green',bg='white')
  label_1.grid(row=0,column=0,padx=5,sticky=W)

  self.entry=StringVar()

  self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('times new roman',16,'bold'))
  self.entry1.grid(row=0,column=1,padx=5,sticky=W)

  self.send=Button(btn_frame,text="Send>>",command=self.send,font=('arial',15,'bold'),width=8,bg='green')
  self.send.grid(row=0,column=2,padx=5,sticky=W)

  self.clare=Button(btn_frame,text="Clear Data",command=self.clear,font=('arial',15,'bold'),width=8,bg='red',fg='white')
  self.clare.grid(row=1,column=0,padx=5,sticky=W)

  self.msg=''
  self.label_11=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='red',bg='white')
  self.label_11.grid(row=1,column=1,padx=5,sticky=W)



#-----------------function declaration-------------
  
 def enter_func(self):
  self.send.invoke()
  self.entry.set('')

 def clear(self):
  self.text.delete('1.0',END)
  self.entry.set('')


 def send(self):
  send='\t\t\t'+'You: '+self.entry.get()
  self.text.insert(END,'\n'+send)

  self.text.yview(END)

  if(self.entry.get()==''):
   self.msg='Please enter some input'
   self.label_11.config(text=self.msg,fg='red')
  else:
   self.msg=''
   self.label_11.config(text=self.msg,fg='red')
  
  if(self.entry.get()=='hello'):
   self.text.insert(END,'\n\n'+'Bot: Hi')
  
  elif(self.entry.get()=='hi'):
   self.text.insert(END,'\n\n'+'Bot: Hello')
  
  elif(self.entry.get()=='How are you?'):
   self.text.insert(END,'\n\n'+'Bot: fine and you?')
  
  elif(self.entry.get()=='Fantastic'):
   self.text.insert(END,'\n\n'+'Bot: Nice to hear')
  
  elif(self.entry.get()=='Who created you?'):
   self.text.insert(END,'\n\n'+'Bot: Yassine Es-saidi and Ismail Brihmat')
  
  elif(self.entry.get()=='What is your name?'):
   self.text.insert(END,'\n\n'+'Bot: My name is Mr Hacker')

  elif(self.entry.get()=='Can you speak another language?'):
   self.text.insert(END,'\n\n'+'Bot: I only speak english')
  
  elif(self.entry.get()=='What is machine learning?'):
   self.text.insert(END,'\n\n'+'Bot: Machine learning is a field of artificial intelligence where algorithms enable systems to learn patterns from data and make predictions or decisions without explicit programming. It involves creating models that can improve their performance over time as they are exposed to more data.')

  elif(self.entry.get()=='How does Facial recognition work step by step?'):
   self.text.insert(END,'\n\n'+'Bot: Facial recognition captures and analyzes facial features from an image or video, converting them into a unique numerical representation. This representation is then compared to stored templates to identify or verify an individual\'s identity.')

  elif(self.entry.get()=='What is python programming?'):
   self.text.insert(END,'\n\n'+'Bot: Python is a high-level, versatile programming language known for its readability and simplicity. It supports multiple paradigms and is widely used for web development, data analysis, artificial intelligence, and more.')

  elif(self.entry.get()=='What is chatbot?'):
   self.text.insert(END,'\n\n'+'Bot: A chatbot is a computer program designed to simulate conversation with human users, especially over the internet. Chatbots use natural language processing and machine learning to understand and respond to user queries, providing automated assistance or information.')

  elif(self.entry.get()=='bye'):
   self.text.insert(END,'\n\n'+'Bot: Thank You For Chatting')
  
  else:
   self.text.insert(END,'\n\n'+'Bot: Sorry I didn\'t get it')
  





if __name__ == '__main__':
 root=Tk()
 obj=ChatBot(root)
 root.mainloop()