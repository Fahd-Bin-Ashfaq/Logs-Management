import os
import mimetypes
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from datetime import datetime
import csv
import stat

# File type check karne ke liye extension mapping
def get_file_type(file_path):
    ext = os.path.splitext(file_path)[1].lower()  # File ka extension nikalna
    ext_map = {
        '.doc': 'Word', '.docx': 'Word',
        '.xls': 'Excel', '.xlsx': 'Excel',
        '.ppt': 'PowerPoint', '.pptx': 'PowerPoint',
        '.pdf': 'PDF', '.txt': 'Text',
        '.csv': 'CSV', '.jpg': 'Image',
        '.jpeg': 'Image', '.png': 'Image',
        '.gif': 'Image', '.mp4': 'Video',
        '.mp3': 'Audio', '.py': 'Python Script',
        '.exe': 'Executable', '.zip': 'Archive',
        '.rar': 'Archive', '.html': 'HTML',
        '.js': 'JavaScript', '.json': 'JSON',
        '.xml': 'XML'
    }
    # Extension ke base par human-readable type return karo
    return ext_map.get(ext, ext.replace('.', '').upper() or 'Unknown')

# File ke permissions symbolically return karta hai (e.g. -rw-r--r--)
def get_permissions(file_path):
    try:
        mode = os.stat(file_path).st_mode  # File ka mode (permission info)
        return stat.filemode(mode)         # Human-readable permission string
    except:
        return 'N/A'

# Folder ke andar sabhi files ki metadata ikatthi karo
def get_metadata(folder_path):
    metadata = []
    for root, _, files in os.walk(folder_path):  # Folder ke andar recursively files nikalta hai
        for file in files:
            path = os.path.join(root, file)
            try:
                stats = os.stat(path)  # File ka size, date, permissions waghera
                metadata.append({
                    "Name": file,
                    "Type": get_file_type(path),
                    "Size (KB)": round(stats.st_size / 1024, 2),  # Bytes se KB main convert
                    "Permissions": get_permissions(path),
                    "Created": datetime.fromtimestamp(stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S'),
                    "Modified": datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                    "Accessed": datetime.fromtimestamp(stats.st_atime).strftime('%Y-%m-%d %H:%M:%S')
                })
            except Exception as e:
                print(f"Error reading {path}: {e}")
    return metadata

# CSV export karne ka function
def export_csv():
    if not tree.get_children():  # Agar data hi nahi hai table main
        messagebox.showwarning("Warning", "No data to export!")
        return

    # Save file dialog
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV File", "*.csv")])
    if file_path:
        with open(file_path, "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            headers = [tree.heading(col)["text"] for col in tree["columns"]]  # Column names
            writer.writerow(headers)
            for row in tree.get_children():
                writer.writerow(tree.item(row)['values'])  # Har row ki values likho
        messagebox.showinfo("Success", "CSV exported successfully!")

# Folder choose karne ka button function
def select_folder():
    folder_path = filedialog.askdirectory()  # Folder choose karna
    if folder_path:
        data = get_metadata(folder_path)  # Metadata collect karo
        for i in tree.get_children():  # Purana data clear karo
            tree.delete(i)
        for item in data:
            tree.insert('', 'end', values=list(item.values()))  # Naya data insert karo

# Columns par click kar ke sort karne ka logic
def sort_column(col, reverse):
    data = [(tree.set(k, col), k) for k in tree.get_children('')]
    try:
        # Numeric sorting if possible
        data.sort(key=lambda t: float(t[0]) if t[0].replace('.', '', 1).isdigit() else t[0], reverse=reverse)
    except:
        data.sort(reverse=reverse)
    for index, (val, k) in enumerate(data):
        tree.move(k, '', index)
    # Header par dobara click karne par reverse sorting ho
    tree.heading(col, command=lambda: sort_column(col, not reverse))

# GUI Window setup
root = tk.Tk()
root.title("Simple File Metadata Viewer")
root.geometry("900x500")

frame = tk.Frame(root)
frame.pack(pady=10)

# Buttons: Select Folder & Export CSV
btn_select = tk.Button(frame, text="Select Folder", command=select_folder)
btn_select.pack(side=tk.LEFT, padx=5)

btn_export = tk.Button(frame, text="Export CSV", command=export_csv)
btn_export.pack(side=tk.LEFT, padx=5)

# Table columns
columns = ["Name", "Type", "Size (KB)", "Permissions", "Created", "Modified", "Accessed"]
tree = ttk.Treeview(root, columns=columns, show='headings')  # Table create karo

for col in columns:
    tree.heading(col, text=col, command=lambda c=col: sort_column(c, False))  # Column headings
    tree.column(col, width=120)

tree.pack(expand=True, fill='both')

root.mainloop()  # GUI loop chalao
