import tkinter as tk
import zipfile
from func import create_zip, extract_archive
from tkinter import filedialog, messagebox

def create_archive(source_entry, target_entry, filters):
    source_folder = source_entry.get()
    target_zip = target_entry.get()
    filter_list = [ext for ext, var in filters.items() if var.get()]

    compression_level = {
        "ZIP_DEFLATED": zipfile.ZIP_DEFLATED,
        "ZIP_STORED": zipfile.ZIP_STORED,
        "ZIP_BZIP2": zipfile.ZIP_BZIP2,
        "ZIP_LZMA": zipfile.ZIP_LZMA,
    }[selected_comp.get()]

    try:
        create_zip(source_folder, target_zip, compression_level=compression_level, filter_list=filter_list)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

root = tk.Tk()
root.title("ZipApp")
root.geometry("420x380")  # Задаем размер окна 400x250
path_line_width = 20

# Первая строка
tk.Label(root, text="Исходная папка:").grid(row=0, column=1, padx=5, pady=5)

selected_path_1 = tk.Entry(root, width=path_line_width)
selected_path_1.grid(row=0, column=2, padx=5, pady=5)

tk.Button(root, text="Выбрать",
          command=lambda: selected_path_1.insert(tk.END, filedialog.askdirectory())).grid(
    row=0, column=3, padx=5, pady=5)

# Вторая строка
tk.Label(root, text="Целевой архив:").grid(row=1, column=1, padx=5, pady=5)

selected_path_2 = tk.Entry(root, width=path_line_width)
selected_path_2.grid(row=1, column=2, padx=5, pady=5)

tk.Button(root, text="Выбрать",
          command=lambda: selected_path_2.insert(tk.END, filedialog.asksaveasfilename(defaultextension=".zip"))).grid(
    row=1, column=3, padx=5, pady=5)

# Третья строка
tk.Label(root, text="Фильтрация файлов:").grid(row=2, column=1, padx=5, pady=5)
filter_zip = {
    '.txt': tk.BooleanVar(),
    '.docx': tk.BooleanVar(),
    '.pdf': tk.BooleanVar(),
    '.png': tk.BooleanVar(),
    '.jpg': tk.BooleanVar(),
    '.xlsx': tk.BooleanVar()
}

j = 0
for i, (ext, var) in enumerate(filter_zip.items()):
    cb = tk.Checkbutton(root, text=ext, variable=var)
    if i < 3:
        cb.grid(row=2, column=i+2, padx=5, pady=5)
    else:
        cb.grid(row=3, column=j+2, padx=5, pady=5)
        j += 1

# Четвертая строка
comp_label = tk.Label(root, text="Уровень сжатия:")  # часть выбора сжатия
comp_label.grid(row=4, column=1, padx=5, pady=5)

comp_options = ["ZIP_DEFLATED", "ZIP_STORED", "ZIP_BZIP2", "ZIP_LZMA"]
selected_comp = tk.StringVar()
selected_comp.set(comp_options[0])

compression_scale = tk.OptionMenu(root, selected_comp, *comp_options)
compression_scale.grid(row=4, column=2, padx=5, pady=5, columnspan=2)

# Пятая строка
tk.Button(root, text="Создать архив",
          command=lambda: create_archive(selected_path_1, selected_path_2, filter_zip)).grid(
    row=5, column=2, padx=5, pady=5)

open_zip_rows = 7
tk.Label(root).grid(row=open_zip_rows - 1, column=1, padx=5, pady=5)

# Создание виджетов для распаковки
tk.Label(root, text="Путь к архиву:").grid(row=open_zip_rows, column=1, padx=5, pady=5)
zip_entry = tk.Entry(root, width=path_line_width)
zip_entry.grid(row=open_zip_rows, column=2, padx=5, pady=5)
tk.Button(root, text="Выбрать", command=lambda: zip_entry.insert(tk.END, filedialog.askopenfilename())).grid(
    row=open_zip_rows,
column=3,
padx=5,
pady=5)

tk.Label(root, text="Путь для распаковки:").grid(row=open_zip_rows + 1, column=1, padx=5, pady=5)
extract_entry = tk.Entry(root, width=path_line_width)
extract_entry.grid(row=open_zip_rows + 1, column=2, padx=5, pady=5)
tk.Button(root, text="Выбрать", command=lambda: extract_entry.insert(tk.END, filedialog.askdirectory())).grid(
    row=open_zip_rows + 1,
column=3,
padx=5,
pady=5)

tk.Button(root, text="Распаковать архив", command=lambda: extract_archive(zip_entry, extract_entry)).grid(
    row=open_zip_rows + 2,
column=2,
padx=5,
pady=5)

root.mainloop()
