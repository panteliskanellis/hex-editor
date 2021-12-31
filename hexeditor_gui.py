import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self,root):
        self.root = root
       
        
        self.menubar = tk.Menu(self.root)

        self.show_menu = tk.Menu(self.menubar, tearoff = "off")
        self.analyse_menu = tk.Menu(self.menubar, tearoff = "off")
        self.more_menu = tk.Menu(self.menubar, tearoff = "off")

        self.menubar.add_cascade(label = "Προβολή", menu = self.show_menu)
        self.menubar.add_cascade(label = "Ανάλυση", menu = self.analyse_menu)
        self.menubar.add_cascade(label = "Επιπρόσθετα", menu = self.more_menu)

        ###Προβολή(menu)
        self.adjust_image = tk.PhotoImage(file = "adjust_image.png" ).subsample(50)
        self.show_menu.add_command(label = "Προσαρμογή στο μήκος του παραθύρου", image=self.adjust_image, compound=tk.LEFT)
        self.show_menu.add_command(label = "Bytes ανα σειρά...")

        self.show_menu.add_separator()

        self.show_menu.add_command(label="Επιθεωρητής δεδομένων",accelerator="Ctrl+Alt+D")
        #root.bind
        self.show_menu.add_command(label="Checksums",accelerator="Ctrl+Alt+C")
        #root.bind
        self.show_menu.add_command(label="Αποτέλεσμα αναζήτησης", accelerator="Ctrl+Alt+S")
        #root.bind

        self.show_menu.add_separator()

        self.show_menu.add_command(label ="Επόμενο παράθυρο εργαλείων",accelerator="Alt+F7")
        self.show_menu.add_command(label="Προηγούμενο παράθυρο εργαλείων",accelerator="Shift + Alt +F7")

        self.show_menu.add_separator()

        self.refresh_image = tk.PhotoImage(file="refresh_image.png").subsample(20)
        self.show_menu.add_command(label="Ανανέωση",image=self.refresh_image,compound=tk.LEFT)

        ###Ανάλυση(menu)

        self.statistics_image = tk.PhotoImage(file= "statistics_image.png").subsample(40)
        self.analyse_menu.add_command(label = "Στατιστικές",image = self.statistics_image,compound = tk.LEFT)

        self.analyse_menu.add_command(label = " Αθροίσματα ελέγχου...")

        self.analyse_menu.add_command(label = " Σύγκριση δεδομένων",accelerator="Ctrl+K")
        #root.bind

        ###Επιπρόσθετα(menu)

        self.open_first_memory_image = tk.PhotoImage(file = "open_first_memory_image.png").subsample(10)
        self.more_menu.add_command(label="Άνοιγμα πρωτεύουσας μνήμης...", image = self.open_first_memory_image, compound= tk.LEFT, accelerator="Shift+Ctrl+M")
        #root.bind
        self.more_menu.add_command(label="Άνοιγμα δίσκου...")

        self.more_menu.add_separator()

        self.more_menu.add_command(label = "Επιλογές...")


        self.root.config(menu = self.menubar)

        ###κουμπιά

        self.save = tk.PhotoImage(file = "save_image.png").subsample(15)
        self.save_button = tk.Button(root, image=self.save, borderwidth= 0).grid(padx = 5, column=0, row = 0 )

        self.open_first_memory_button = tk.Button(root, image=self.open_first_memory_image, borderwidth= 0).grid(padx = 5, column=1, row = 0)

        ###combobox

        self.box_value = tk.StringVar()
        self.combobox1 = ttk.Combobox(root,textvariable= self.box_value)
        self.combobox1.bind("<<ComboboxSelected>>",lambda event : self.box_value==self.combobox1.get())
        self.combobox1['values']=('8','16','24','32')    
        self.combobox1.current(0)
        self.combobox1.grid(row = 0,column = 3)
        ### .box_value -> σε συνάρτηση 


        self.root.mainloop()

def main():
        root=tk.Tk()
        root.iconbitmap("hexeditor_icon.ico")
        root.title("hexeditor")
        root.state('zoomed')
        app=App(root)
        root.mainloop()
        
main()        