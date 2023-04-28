import tkinter as tk, os
from tkinter import filedialog, messagebox
from datetime import datetime
from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
# Create a Fernet object with the generated key
fernet = Fernet(key)

def browse_folder():
    # Open a file dialog to select a folder to encrypt
    folder_path = filedialog.askdirectory()
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(0, folder_path)

def encrypt_folder():
    timestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    encrypt_file = os.getcwd() + "/" + timestamp + ".txt"

    with open(os.getcwd() + "/" + timestamp + ".ran", 'wb') as thekeyE:
        thekeyE.write(key)

    # Get the folder path to encrypt
    folder_path = folder_path_entry.get()

    # Walk through the folder and encrypt each file
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Read the file to encrypt
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if file_size < 10485760:
                with open(file_path, 'rb') as file:
                    file_data = file.read()

                # Encrypt the file data
                encrypted_data = fernet.encrypt(file_data)

                # Write the encrypted data
                with open(file_path, 'wb') as f:
                    f.write(encrypted_data)

    # Write the encrypted key
    with open(encrypt_file, 'wb') as t:
        t.write(encrypted_data)

    # Show a message box with the encryption key
    messagebox.showinfo('Encryption Key', 'Files have been encrypted successfully')
    folder_path_entry.delete(0,'end')

def browse_files():
    # Open a file dialog to select multiple files to encrypt
    file_paths = filedialog.askopenfilenames()
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, ', '.join(file_paths))

def encrypt_files():
    # Get the file paths to encrypt
    file_paths = file_path_entry.get().split(', ')
    for file_path in file_paths:
        # Read the file to encrypt
        with open(file_path, 'rb') as file:
            file_data = file.read()

        # Encrypt the file data
        encrypted_data = fernet.encrypt(file_data)

        # Write the encrypted data to a new file
        with open(file_path + '.encrypted', 'wb') as file:
            file.write(encrypted_data)

    # Show a message box with the encryption key
    messagebox.showinfo('Encryption Key', f'The encryption key is: {key}')
    file_path_entry.delete(0,'end')

# Create the main window
window = tk.Tk()
window.title('File Encryptor')

# Create the folder path label and entry
folder_path_label = tk.Label(window, text='Folder path:')
folder_path_label.grid(row=0, column=0)
folder_path_entry = tk.Entry(window)
folder_path_entry.grid(row=0, column=1)
browse_folder_button = tk.Button(window, text='Browse', command=browse_folder)
browse_folder_button.grid(row=0, column=2)

# Create the encrypt folder button
encrypt_folder_button = tk.Button(window, text='Encrypt Folder', command=encrypt_folder)
encrypt_folder_button.grid(row=1, column=1)

# Create the file path label and entry
file_path_label = tk.Label(window, text='File paths:')
file_path_label.grid(row=2, column=0)
file_path_entry = tk.Entry(window)
file_path_entry.grid(row=2, column=1)
browse_files_button = tk.Button(window, text='Browse', command=browse_files)
browse_files_button.grid(row=2, column=2)

# Create the encrypt files button
encrypt_files_button = tk.Button(window, text='Encrypt Files', command=encrypt_files)
encrypt_files_button.grid(row=3, column=1)

# Start the main loop
window.mainloop()
