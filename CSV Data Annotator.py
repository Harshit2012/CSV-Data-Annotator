import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os

class CSVAnnotatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Data Annotator")
        self.root.geometry("800x600")

        self.csv_file_path = ""
        self.df = None

        self.upload_button = tk.Button(root, text="Upload CSV", command=self.upload_csv)
        self.upload_button.pack(pady=20)

        self.text_widget = tk.Text(root, height=20, width=100)
        self.text_widget.pack(pady=20)

        self.annotate_button = tk.Button(root, text="Add Annotation", command=self.add_annotation)
        self.annotate_button.pack(pady=10)

        self.save_button = tk.Button(root, text="Save Annotated CSV", command=self.save_csv)
        self.save_button.pack(pady=20)

    def upload_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.csv_file_path = file_path
            self.df = pd.read_csv(self.csv_file_path)
            self.display_csv_content()

    def display_csv_content(self):
        if self.df is not None:
            self.text_widget.delete(1.0, tk.END)
            self.text_widget.insert(tk.END, self.df.to_string())

    def add_annotation(self):
        if self.df is not None:
            row_idx = int(self.simpledialog("Enter Row Index to Annotate"))
            column_name = self.simpledialog("Enter Column Name to Annotate")
            annotation = self.simpledialog("Enter Annotation")
            if row_idx in self.df.index and column_name in self.df.columns:
                self.df.at[row_idx, column_name] = annotation
                self.display_csv_content()
            else:
                messagebox.showerror("Error", "Invalid row index or column name.")

    def simpledialog(self, prompt):
        return tk.simpledialog.askstring("Input", prompt)

    def save_csv(self):
        if self.df is not None:
            save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
            if save_path:
                self.df.to_csv(save_path, index=False)
                messagebox.showinfo("Success", f"Annotated CSV saved to {save_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVAnnotatorApp(root)
    root.mainloop()