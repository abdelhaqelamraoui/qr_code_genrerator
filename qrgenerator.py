


from pyqrcode import create
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import Label, filedialog, mainloop
import pyperclip as ppc
from PIL import ImageTk, Image



class QRGen(tk.Frame):
   def __init__(self, root):
      tk.Frame.__init__(self, root)
      self.root = root

   entry_link = None
   btn_generate = None
   btn_paste = None
   btn_export = None
   entry_scale = None
   format = None
   path = None
   label_scale = None
   label_auth = None
    
   def show(self):
      self.root.geometry("400x500")
      self.root.resizable(0,0)
      self.root.title("QR code Generator")

      self.entry_link = tk.Entry(self.root, width=44, border=1, fg='blue')
      self.btn_generate = tk.Button(self.root, text="Generate", command=self.generate, bg='#27743c', fg='#ffffff', font='Ubuntu 10', activeforeground='white', activebackground='#004156')
      self.btn_paste = tk.Button(self.root, text="Paste", command=self.paste, bg='#27743c', fg='#ffffff', font='Ubuntu 10', activeforeground='white', activebackground='#004156')
      self.btn_export = tk.Button(self.root, text="Export", command=self.export, bg='#27743c', fg='#ffffff', font='Ubuntu 10', activeforeground='white', activebackground='#004156')
      self.entry_scale = tk.Entry(self.root, textvariable=self.path, width=4)
      self.label_scale = tk.Label(self.root, text="Scale of the image", font='Ubuntu 10')
      auth = "By: Abdelhaq El Amraoui  2021  |   www.elam-2020.blogspot.com"
      self.label_auth = tk.Label(self.root, text=auth, font="Ubuntu-Mono 8", bg="#c3c4c4", width=400)


      self.entry_link.place(x=200, y=410, anchor="center")
      self.btn_paste.place(x=100, y=450, anchor="center")
      self.btn_generate.place(x=200, y=450, anchor="center")
      self.btn_export.place(x=300, y=450, anchor="center")
      self.label_auth.place(x=200, y=500, anchor="s")

   def generate(self):
      data = self.entry_link.get()
      if len(data) > 0:
         self.generate_qrcode(data=data, fname='.tmp.png', scale=10)
      else:
         self.generate_qrcode(fname='.tmp.png', scale=10)

      canvas = tk.Canvas(self.root, width = 400, height = 386)     
      canvas.place(x=200, y=0, anchor='n')

      image = Image.open('.tmp.png')
      image = image.resize((372, 372), Image.ANTIALIAS)
      img = ImageTk.PhotoImage(image)
      canvas.create_image(200,200, anchor='center', image=img)
      canvas.create_rectangle(12, 12, 388, 385,outline="black", width=1)

      mainloop()
            

   def generate_qrcode(self, data="www.elam-2020.blogspot.com", fname='qr_code.png', scale=40):

      fname = str(fname)
      url = create(str(data))
      if(fname.endswith('.png')):
         url.png(fname, scale = scale)
      elif(fname.endswith('.svg')):
         url.svg(fname, scale = scale)
      else:
         raise Exception("Invalid extension!")

   def export(self):
      self.btn_paste.destroy()
      self.btn_generate.destroy()

      self.entry_scale.place(x=230, y=450, anchor="center")
      self.label_scale.place(x=140, y=450, anchor="center")
      self.entry_scale.insert(0, '40')
      self.btn_export.configure(text="OK", command=self.ok)
      

   def ok(self):
      d = self.entry_link.get()
      fn = filedialog.asksaveasfilename(title='qr_code', initialfile='qr_code',
      confirmoverwrite=True,initialdir='/home/Desktop/' ,filetypes=[('PNG', '.png'), ('SVG', '.svg')])
      try:
         sc = int(self.entry_scale.get())
      except:
         raise Exception("Invalide scale")
      self.generate_qrcode(data=d, fname=fn, scale=sc)
      self.entry_scale.destroy()
      self.label_scale.destroy()
      self.show()



   def paste(self):
      self.entry_link.delete(0, 'end')
      self.entry_link.insert(0,ppc.paste())

   def chose_path_and_save(self):
      f = filedialog.asksaveasfile(title='qr_code', defaultextension='.png',
      confirmoverwrite=True,initialdir='/home/' ,filetypes=[('PNG', '.png'), ('SVG', '.svg')])
  

if __name__ == '__main__':
   window = tk.Tk()
   rggen = QRGen(window)
   rggen.show()
   window.mainloop()