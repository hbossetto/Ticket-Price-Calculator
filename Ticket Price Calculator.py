#Hunter Bossetto
#12/14/2021
import tkinter

class TipGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.subtotal_frame = tkinter.Frame(self.main_window)
        self.percent_frame = tkinter.Frame(self.main_window)
        self.tip_frame = tkinter.Frame(self.main_window)
        self.total_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        
        self.subtotal_label = tkinter.Label (self.subtotal_frame, text = 'Enter the amount of the ticket:')
        self.subtotal_entry = tkinter.Entry(self.subtotal_frame, width = 15)
        
        self.subtotal_label.pack(side = 'left')
        self.subtotal_entry.pack(side = 'left')
        
        self.percent_label = tkinter.Label (self.percent_frame, text = 'Enter the tip as a percent:')
        self.percent_entry = tkinter.Entry(self.percent_frame, width = 15)
        
        self.percent_label.pack(side = 'left')
        self.percent_entry.pack(side = 'left')
        
        self.tip_label = tkinter.Label (self.tip_frame, text = 'Tip Amount: $')
        
        self.tip = tkinter.StringVar()
        self.tip_display_label = tkinter.Label (self.tip_frame, textvariable = self.tip)
        
        self.tip_label.pack(side = 'left')
        self.tip_display_label.pack(side = 'left')
        
        self.total_label = tkinter.Label (self.total_frame, text = 'Total Amount: $')
        
        self.total = tkinter.StringVar()
        self.total_display_label = tkinter.Label (self.total_frame, textvariable = self.total)
        
        self.total_label.pack(side = 'left')
        self.total_display_label.pack(side = 'left')
        
        self.calculate_button = tkinter.Button (self.button_frame, text = 'Calculate', command = self.calculate_tip)
        self.exit_button = tkinter.Button (self.button_frame, text = 'Exit', command = self.main_window.destroy)
        
        self.calculate_button.pack(side = 'left')
        self.exit_button.pack(side = 'left')
        
        self.subtotal_frame.pack()
        self.percent_frame.pack()
        self.tip_frame.pack()
        self.total_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()

    def calculate_tip(self):
        self.subtotal = float(self.subtotal_entry.get())
        self.percent = float(self.percent_entry.get())

        if self.percent > 0:
            self.tip_ammount = float(self.subtotal) * (self.percent / 100)
            self.total_ammount = float(self.subtotal) + self.tip_ammount
            self.tip.set(format(self.tip_ammount, ',.2f'))
            self.total.set(format(self.total_ammount, ',.2f'))

TipGUI()
