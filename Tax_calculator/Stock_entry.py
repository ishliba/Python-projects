import customtkinter
import customtkinter as ctk
import tkinter.messagebox
import csv

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class Stock_Entry(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Stock_entry")
        self.geometry("1100x580")
        self._set_appearance_mode("System")

        #widget_padding
        self.padding = {'padx':10, 'pady': 10}

    def auto_grid(self,r: int,c:int):
        return f"row={r}, column={c}"

    def main(self, Buy_S):
        self.Stock_lable = ctk.CTkLabel(self, text="Stock name")
        self.Stock_lable.grid(row=0, column=0,**self.padding)
        self.Stock_entry = ctk.CTkEntry(self)
        self.Stock_entry.grid(row=0, column=1, **self.padding)
        if Buy_S == "Buy":
            self.buy_label = ctk.CTkLabel(self, text="Buy Price")
            self.buy_label.grid(row=1, column=0, **self.padding)
            self.buy_entry = ctk.CTkEntry(self)
            self.buy_entry.grid(row=1, column=1, **self.padding)
        else:
            self.sell_label = ctk.CTkLabel(self, text="Sell Price")
            self.sell_label.grid(row=1, column=0, **self.padding)
            self.sell_entry = ctk.CTkEntry(self)
            self.sell_entry.grid(row=1, column=1, **self.padding)
        self.textbox = ctk.CTkTextbox(self, width=300,)
        self.textbox.grid(row=5, column=0, padx=10, pady=10)
        self.textbox.insert(index="0.0",text="Hi")




    # def query(self):
    #     Que

    def run(self):
        self.mainloop()



run = "n"
stk = Stock_Entry()
if run == "y":
    stk.main(Buy_S="Sell")
    stk.run()

file_name = "Data.csv"
fields = ["Date", "Company", "Buy Price", "Sell Price"]

with open(file_name, "w") as file:
    csvwriter = csv.writer(file)

    csvwriter.writerow(fields)
    csvwriter.writerows("Tesla")



