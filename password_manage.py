import requests
from tkinter import Tk, Label, Entry, Button, StringVar, ttk, END, messagebox

API_URL = "https://api.exchangerate.host/latest"

CURRENCIES = [
    "USD","EUR","INR","GBP","JPY","AUD","CAD","CHF","CNY","SGD","NZD","AED","SAR","ZAR","HKD"
]

def fetch_rates(base):
    try:
        r = requests.get(API_URL, params={"base": base}, timeout=10)
        r.raise_for_status()
        data = r.json()
        return data.get("rates", {})
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch rates: {e}")
        return {}

class App:
    def _init_(self, root):
        root.title("Live Currency Converter")
        root.geometry("520x240")

        Label(root, text="From").grid(row=0, column=0, padx=8, pady=8, sticky="e")
        Label(root, text="To").grid(row=1, column=0, padx=8, pady=8, sticky="e")
        Label(root, text="Amount").grid(row=2, column=0, padx=8, pady=8, sticky="e")

        self.from_var = StringVar(value="USD")
        self.to_var = StringVar(value="INR")
        self.amount_var = StringVar(value="1")
        self.result_var = StringVar(value="Result will appear here")

        self.from_box = ttk.Combobox(root, textvariable=self.from_var, values=CURRENCIES, state="readonly")
        self.to_box = ttk.Combobox(root, textvariable=self.to_var, values=CURRENCIES, state="readonly")
        Entry(root, textvariable=self.amount_var, width=20).grid(row=2, column=1, padx=8, pady=8, sticky="w")

        self.from_box.grid(row=0, column=1, padx=8, pady=8, sticky="w")
        self.to_box.grid(row=1, column=1, padx=8, pady=8, sticky="w")

        Button(root, text="Convert", command=self.convert).grid(row=3, column=1, padx=8, pady=8, sticky="w")
        Label(root, textvariable=self.result_var).grid(row=4, column=0, columnspan=3, padx=8, pady=10)

    def convert(self):
        base = self.from_var.get()
        target = self.to_var.get()
        try:
            amount = float(self.amount_var.get())
        except ValueError:
            messagebox.showerror("Error", "Enter a valid amount.")
            return
        rates = fetch_rates(base)
        if not rates or target not in rates:
            messagebox.showerror("Error", "Rate not available.")
            return
        result = amount * rates[target]
        self.result_var.set(f"{amount:.4f} {base} = {result:.4f} {target}")

if __name__ == "__main__":
    root = Tk()
    App(root)
    root.mainloop()