


from pyqrcode import create
import png
#from pyqrcode import QRCode
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import filedialog
import pyperclip as ppc



class QRGen(tk.Frame):
   def __init__(self, root):
      tk.Frame.__init__(self, root)
      self.root = root

   entry_link = None
   btn_generate = None
   btn_paste = None
   btn_export = None
   entry_scale = None
   # comboBox_format = None
   format = None
   path = None
   label_scale = None
   # label_format = None
   label_auth = None
    
   def show(self):
      self.root.geometry("400x480")
      self.root.resizable(0,0)
      self.root.title("QR code Generator")

      self.entry_link = tk.Entry(self.root, width=44, border=1, fg='blue')
      self.btn_generate = tk.Button(self.root, text="Generate", command=self.generate, bg='#27743c', fg='#ffffff', font='Ubuntu 10')
      self.btn_paste = tk.Button(self.root, text="Paste", command=self.paste, bg='#27743c', fg='#ffffff', font='Ubuntu 10')
      self.btn_export = tk.Button(self.root, text="Export", command=self.export, bg='#27743c', fg='#ffffff', font='Ubuntu 10')
      self.entry_scale = tk.Entry(self.root, textvariable=self.path, width=4)
      # self.comboBox_format = Combobox(self.root, values=['PNG', 'SVG'], textvariable=self.format, width=4)
      # self.label_format = tk.Label(self.root, text="Format")
      self.label_scale = tk.Label(self.root, text="Scale")
      auth = "By: Abdelhaq El Amraoui  2021  |   www.elam-2020.blogspot.com"
      self.label_auth = tk.Label(self.root, text=auth, font="Ubuntu-Mono 8", bg="#c3c4c4", width=400)


      self.entry_link.place(x=200, y=380, anchor="center")
      self.btn_paste.place(x=100, y=420, anchor="center")
      self.btn_generate.place(x=200, y=420, anchor="center")
      self.btn_export.place(x=300, y=420, anchor="center")
      self.label_auth.place(x=200, y=480, anchor="s")

   def generate(self):
      data = self.entry_link.get()
      self.generate_qrcode(self, data, fname='./.tmp/.tmp.png')
      # show the image in ui

   def generate_qrcode(self, data="www.elam-2020.blogspot.com", fname='qrcode.png', scale=40):
      # String which represents the QR code
      # s = "www.elam-2020.blogspot.com"
      # Generate QR code
      # url = create(s)
      # Create and save the svg file naming "myqr.svg"
      # url.svg("myqr.svg", scale = 8)
      # Create and save the png file naming "myqr.png"
      # url.png('myqr.png', scale = 40)
      ext = str(fname)[-1:-4:-1] # last 3 chars reversed
      ext = ext[::-1] # reverse them again to get right extension
      url = create(str(data))
      print("ext = ", ext)
      if(ext == 'png'):
         url.png(fname, scale = scale)
      elif(ext == 'svg'):
         url.png(fname, scale = scale)
      else:
         raise Exception("Invalid extension!")

   def export(self):
      self.btn_paste.destroy()
      self.btn_generate.destroy()

      self.entry_scale.place(x=230, y=420, anchor="center")
      # self.comboBox_format.place(x=140, y=420, anchor="center")
      # self.label_format.place(x=80, y=420, anchor="center")
      self.label_scale.place(x=190, y=420, anchor="center")
      self.entry_scale.insert(0, '40')
      self.btn_export.configure(text="OK", command=self.ok)

      # if(len(self.entry_scale.get()) < 1):
      #    return
      # data = self.entry_link.get()
      # fname = filedialog.asksaveasfilename(title='qr_code',mode='w+', defaultextension='.png', initialfile='qr_code',
      # confirmoverwrite=True,initialdir='/home/' ,filetypes=[('PNG', '.png'), ('SVG', '.svg')])
      # try:
      #    scale = self.int(self.entry_scale.get())
      #    if scale < 0:
      #       raise Exception
      # except:
      #    raise Exception("Invalide scale")
      # self.generate_qrcode(self, data=data, fname=fname, scale=scale)
      

   def ok(self):
      d = self.entry_link.get()
      fn = filedialog.asksaveasfilename(title='qr_code', defaultextension='.png', initialfile='qr_code',
      confirmoverwrite=True,initialdir='/home/' ,filetypes=[('PNG', '.png'), ('SVG', '.svg')])
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
   # rggen.generate_qrcode(fname="/home/shepherd/Desktop/ggen.png", scale=13)
   rggen.show()
   window.mainloop()