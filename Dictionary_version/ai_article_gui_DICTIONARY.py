import openai
import os
import datetime
import hashlib
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
import sqlite3

# Create a connection to the SQLite database
DB_FILE = "users.db"
def initialize_db():
    """Initialize the SQLite database."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
            """
        )
        conn.commit()
        conn.close

initialize_db()

#Save user to the SQLite database
def save_user_to_db(username, hashed_password):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
    except sqlite3.IntegrityError:
        Messagebox.show_error("Username already exists. Please choose a different username.", "Registration Error")
    finally:
        conn.close()

# Authenticate user from the SQLite database
def authenticate_user_from_db(username, hashed_password):
    hashed_password
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

# Set your OpenAI API key
openai.api_key = "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"  # Replace with your actual API key

# Directory to save articles
SAVE_DIR = "LinkedIn/articles"  # Replace with your desired save directory

# User dictionary for storing users in memory 
users = {}

# Ensure the save directory exists
os.makedirs(SAVE_DIR, exist_ok=True)

def hash_password(password):
    """Hash a password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest()

def save_user(username, password):
    """Save a new user to the in-memory dictionary."""
    hashed_password = hash_password(password)
    if username in users:
        Messagebox.show_error("Username already exists. Please choose a different username.", "Registration Error")
        return False
    users[username] = hashed_password
    Messagebox.show_info("User registered successfully!", "Registration Success")
    return True

def authenticate_user(username, password):
    """Authenticate a user by checking their credentials."""
    hashed_password = hash_password(password)
    if username in users and users[username] == hashed_password:
        return True
    else:
        Messagebox.show_error("Invalid username or password.", "Login Error")
        return False

def generate_article(topic, output_area):
    """Generate a LinkedIn article using OpenAI."""
    if not topic.strip():
        Messagebox.show_error("The topic field cannot be empty.", "Input Error")
        return

    try:
        output_area.delete(1.0, END)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional LinkedIn article writer that can code in any programming language."},
                {"role": "user", "content": f"Write an article about {topic.strip()}."}
            ],
            max_tokens=3000,
            temperature=1.3
        )
        article = response.choices[0].message.content.strip()
        output_area.insert(END, article)
    except Exception as e:
        Messagebox.show_error(f"Failed to generate the article: {str(e)}", "API Error")

def save_article(output_area, topic):
    """Save the article to a file."""
    article = output_area.get(1.0, END).strip()
    if not article:
        Messagebox.show_error("No article to save. Please generate an article first.", "Save Error")
        return

    try:
        sanitized_topic = "".join(c for c in topic if c.isalnum() or c in (" ", "-")).replace(" ", "_")
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{timestamp}_{sanitized_topic}.txt"
        file_path = os.path.join(SAVE_DIR, file_name)

        with open(file_path, "w") as file:
            file.write(article)
        Messagebox.show_info(f"Article saved to {file_path}", "Success")
    except Exception as e:
        Messagebox.show_error(f"Failed to save the article: {str(e)}", "Save Error")

def clear_output(output_area):
    """Clear the output area."""
    output_area.delete(1.0, END)

def login_screen(app):
    """Display the login screen."""
    for widget in app.winfo_children():
        widget.destroy()

    ttk.Label(app, text="Login", font=("Helvetica", 20, "bold")).pack(pady=20)
    username_entry = ttk.Entry(app, font=("Helvetica", 14), width=30)
    username_entry.pack(pady=10)
    username_entry.insert(0, "Username")
    password_entry = ttk.Entry(app, font=("Helvetica", 14), show="*", width=30)
    password_entry.pack(pady=10)
    password_entry.insert(0, "Password")

    def login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()
        if authenticate_user(username, password):
            article_creator_screen(app)

    ttk.Button(app, text="Login", bootstyle=PRIMARY, command=login).pack(pady=10)
    ttk.Button(app, text="Register", bootstyle=SUCCESS, command=lambda: register_screen(app)).pack(pady=10)

def register_screen(app):
    """Display the registration screen."""
    for widget in app.winfo_children():
        widget.destroy()

    ttk.Label(app, text="Register", font=("Helvetica", 20, "bold")).pack(pady=20)
    username_entry = ttk.Entry(app, font=("Helvetica", 14), width=30)
    username_entry.pack(pady=10)
    username_entry.insert(0, "Username")
    password_entry = ttk.Entry(app, font=("Helvetica", 14), show="*", width=30)
    password_entry.pack(pady=10)
    password_entry.insert(0, "Password")

    def register():
        username = username_entry.get().strip()
        password = password_entry.get().strip()
        if save_user(username, password):
            login_screen(app)

    ttk.Button(app, text="Register", bootstyle=SUCCESS, command=register).pack(pady=10)
    ttk.Button(app, text="Back to Login", bootstyle=INFO, command=lambda: login_screen(app)).pack(pady=10)

def article_creator_screen(app):
    """Display the article creator screen."""
    for widget in app.winfo_children():
        widget.destroy()

    app.title("AI Article Generator")

    ttk.Label(app, text="Enter a Topic:", font=("Helvetica", 16, "bold")).pack(pady=10)
    topic_entry = ttk.Entry(app, font=("Helvetica", 14), width=70)
    topic_entry.pack(pady=10)

    ttk.Label(app, text="Generated Article:", font=("Helvetica", 16, "bold")).pack(pady=10)
    output_area = ttk.Text(app, wrap=WORD, font=("Helvetica", 12), height=20, width=80)
    output_area.pack(pady=10, padx=10, fill=BOTH, expand=True)

    button_frame = ttk.Frame(app)
    button_frame.pack(pady=20)

    ttk.Button(
        button_frame, text="Generate Article", bootstyle=PRIMARY,
        command=lambda: generate_article(topic_entry.get(), output_area)
    ).grid(row=0, column=0, padx=10)

    ttk.Button(
        button_frame, text="Save Article", bootstyle=SUCCESS,
        command=lambda: save_article(output_area, topic_entry.get())
    ).grid(row=0, column=1, padx=10)

    ttk.Button(
        button_frame, text="Clear Output", bootstyle=WARNING,
        command=lambda: clear_output(output_area)
    ).grid(row=0, column=2, padx=10)

    ttk.Button(
        button_frame, text="Logout", bootstyle=DANGER, command=lambda: login_screen(app)
    ).grid(row=0, column=3, padx=10)

# Run the application
def create_gui():
    app = ttk.Window(themename="flatly")
    app.geometry("900x700")
    app.resizable(True, True)
    login_screen(app)
    app.mainloop()

if __name__ == "__main__":
    create_gui()
