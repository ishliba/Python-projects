import customtkinter as ctk



class Tax_Calculator:


    def __init__(self):

        #initialize our window
        self.window = ctk.CTk()
        self.window.title("Tax Calculator")
        self.window.geometry("280x200")
        self.window.resizable(False,False)


        #widget padding
        self.padding: dict = {'padx': 20, 'pady': 10}

        #income lable and entry

        self.income_label = ctk.CTkLabel(self.window, text="Income: ")
        self.income_label.grid(row =0, column=0)
        self.income_entry = ctk.CTkEntry(self.window)
        self.income_entry.grid(row =0, column=1, **self.padding)


        #Tax lable
        self.tax_lable = ctk.CTkLabel(self.window, text="Percent: ")
        self.tax_lable.grid(row =1, column=0)
        self.tax_entry = ctk.CTkEntry(self.window)
        self.tax_entry.grid(row =1, column=1, **self.padding)


        #Result lable and entry
        self.result_label= ctk.CTkLabel(self.window, text="Result: ")
        self.result_label.grid(row =2, column=0)
        self.result_entry = ctk.CTkEntry(self.window)
        self.result_entry.insert(0, '0')
        self.result_entry.grid(row=2, column=1, **self.padding)

        #calculate button
        self.calculate_button = ctk.CTkButton(self.window, text="Calculate", command = self.calculate_tax)
        self.calculate_button.grid(row=3, column=1, **self.padding)


    def update_result(self, text:str):
        self.result_entry.delete(0, ctk.END)
        self.result_entry.insert(0, text)

    def calculate_tax(self):
        try:
            income: float = float(self.income_entry.get())
            tax: float = float(self.tax_entry.get())
            self.update_result(f"Rs {income * (tax/100):,.2f}")
        except ValueError:
            self.update_result('Invalid input')


    def run(self):
        """Runs tkinter app"""

        self.window.mainloop()




if __name__ == "__main__":
    tc = Tax_Calculator()
    tc.run()


