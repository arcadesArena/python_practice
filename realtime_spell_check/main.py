import re
import nltk
from nltk.corpus import words
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

nltk.download("words")

class SpellCheck():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry("600x500")

        self.old_spaces = 0

        self.text=ScrolledText(self.root,font=("Arial",14))
        self.text.bind("<KeyRelease>",self.check)
        self.text.pack()

        self.root.mainloop()
    
    def check(self,event):
        content = self.text.get("1.0",tk.END)
        spaces = content.count(" ")


        if spaces != self.old_spaces:
            self.old_spaces = spaces
            for tag in self.text.tag_names():
                self.text.tag_delete(tag)
            for word in content.split():
                if re.sub("[^\w]","",word.lower()) not in words.words():
                    position = content.find(word)
                    self.text.tag_add(word,f'1.{position}',f'1.{position+len(word)}')
                    self.text.tag_config(word,foreground="blue")
        pass

SpellCheck()
