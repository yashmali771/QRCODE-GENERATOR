import qrcode
from tkinter import Tk, Label, Entry, Button, filedialog
from tkinter import StringVar
from PIL import Image, ImageTk

def generate_qr():
    text = entry_text.get()
    if text:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("generated_qr.png")

        # Load the generated image and display it in the GUI
        image = Image.open("generated_qr.png")
        photo = ImageTk.PhotoImage(image)
        qr_label.config(image=photo)
        qr_label.image = photo

def save_qr():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path:
        img = Image.open("generated_qr.png")
        img.save(file_path)

# Create the main window
root = Tk()
root.title("QR Code Generator")
root.configure(bg="#1e1e1e")
root.geometry("400x550")
root.resizable(False, False)

# Style configurations
font_style = ("Helvetica", 14, "bold")
entry_text = StringVar()

# Create and place the input field
Label(root, text="Enter text for QR Code:", font=font_style, fg="#800080", bg="#1e1e1e").pack(pady=20)
entry = Entry(root, textvariable=entry_text, width=30, font=font_style, bg="#333333", fg="#FFFFFF", insertbackground="#FFFFFF", bd=2, relief="groove")
entry.pack(pady=10)

# Create and place the generate button
Button(root, text="Generate QR Code", command=generate_qr, font=font_style, fg="#FFFFFF", bg="#800080", activebackground="#800080", activeforeground="#1e1e1e", bd=0, padx=10, pady=5, relief="raised").pack(pady=10)

# Create and place the save button
Button(root, text="Save QR Code", command=save_qr, font=font_style, fg="#FFFFFF", bg="#800080", activebackground="#800080", activeforeground="#1e1e1e", bd=0, padx=10, pady=5, relief="raised").pack(pady=10)

# Create and place the label to display the QR code
qr_label = Label(root, bg="#1e1e1e")
qr_label.pack(pady=20)

# Run the application
root.mainloop()
