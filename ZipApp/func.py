import zipfile
import os
from tkinter import messagebox

def create_zip(source_folder, target_zip, compression_level, filter_list):
    with zipfile.ZipFile(target_zip, 'w', compression=compression_level) as zipf:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                file_ext = os.path.splitext(file)[-1]

                # Если список фильтров пустой или расширение файла соответствует выбранным фильтрам
                if not filter_list or file_ext.lower() in filter_list:
                    zipf.write(file_path, os.path.relpath(file_path, source_folder))

def extract_zip(zip_file, extract_to):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def extract_archive(zip_entry, extract_entry):
    zip_file = zip_entry.get()
    extract_to = extract_entry.get()

    try:
        extract_zip(zip_file, extract_to)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")