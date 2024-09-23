import string
import random
import tkinter as tk

running = False

def generate_random_password():
    uppercase_letters = list(string.ascii_uppercase)
    lowercase_letters = list(string.ascii_lowercase)
    digits = list(string.digits)
    punctuation = list("!@#$%^&*()")

    # Ensure fixed length of 8
    length = 8

    # Fixed counts for each character type
    uppercase_count = 2
    lowercase_count = 2
    digits_count = 2
    punctuation_count = 2

    # Ensure no repeat characters
    password = []
    for _ in range(uppercase_count):
        password.append(random.choice(uppercase_letters))
        uppercase_letters.remove(password[-1])
    for _ in range(lowercase_count):
        password.append(random.choice(lowercase_letters))
        lowercase_letters.remove(password[-1])
    for _ in range(digits_count):
        password.append(random.choice(digits))
        digits.remove(password[-1])
    for _ in range(punctuation_count):
        password.append(random.choice(punctuation))
        punctuation.remove(password[-1])

    # Shuffle the password
    random.shuffle(password)
    #print(password)
    generated_password.set("".join(password))

def generate_password_every_second():
    if running:
        generate_random_password()
        root.after(1000, generate_password_every_second)

def start_generation():
    global running
    running = True
    generate_password_every_second()

def stop_generation():
    global running
    running = False

# Create Tkinter window
root = tk.Tk()
root.title("Random Password Generator")

# Load background image
background_image = tk.PhotoImage(file=r"E:\python_project\ppassword_generator.png")

# Resize the image to fit the window size
root.geometry(f"{background_image.width()}x{background_image.height()}")

# Create a label with the background image
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Heading
heading_label = tk.Label(root, text="Random Password Generator", width=25, height=2, borderwidth=3, relief="ridge", font=("Arial", 24), bg="#A2CD5A")
heading_label.place(x=410, y=60)

# Password Box
password_label = tk.Label(root, text=" Password : ", font=("Arial", 16), width=9, bg="#8EE5EE")
password_label.place(x=510, y=200)

generated_password = tk.StringVar()

password_entry = tk.Entry(root, textvariable=generated_password, bg="#8EE5EE", font=("Arial", 16), width=9, state="disable")
password_entry.place(x=700, y=200)

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_random_password, bg="#ffcc80", font=("Arial", 14))
generate_button.place(x=565, y=280)

# Start button to begin automatic generation
start_button = tk.Button(root, text="Start", command=start_generation, bg="#A2CD5A", width=9, font=("Arial", 14))
start_button.place(x=510, y=380)

# Stop button to halt automatic generation
stop_button = tk.Button(root, text="Stop", command=stop_generation, bg="#A2CD5A", width=9, font=("Arial", 14))
stop_button.place(x=620, y=380)

# Quit button
quit_button = tk.Button(root, text="Quit", command=root.destroy, bg="#A2CD5A", width=9, font=("Arial", 14))
quit_button.place(x=730, y=380)

# Start the Tkinter event loop
root.mainloop()

