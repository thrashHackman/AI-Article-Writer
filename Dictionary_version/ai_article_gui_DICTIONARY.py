import openai # Import the OpenAI module
import os # Import the OS module
import datetime # Import the datetime module
import hashlib # Import the hashlib module
import ttkbootstrap as ttk # Import the ttkbootstrap module
from ttkbootstrap.constants import * # Import the constants from ttkbootstrap
from ttkbootstrap.dialogs import Messagebox # Import the Messagebox dialog from ttkbootstrap
import sqlite3 # Import the SQLite3 module
from plantuml import PlantUML # Import the PlantUML module
from dotenv import load_dotenv # Import the load_dotenv function from the dotenv module

# Constants
PLANTUML_JAR = "/home/tahraun/plantuml/plantuml.jar" # Path to the PlantUML JAR file
DB_FILE = "users.db" # Path to the SQLite database file
load_dotenv() # Load environment variables from the .env file
SAVE_DIR = "LinkedIn/articles" # Directory to save articles
users = {}# User dictionary for storing users in memory
openai.api_key = os.getenv("OPENAI_API_KEY") # Access the API key from the environment variable
os.makedirs(SAVE_DIR, exist_ok=True) # Ensure the save directory exists

# Generate a PlantUML diagram
def generate_diagram(diagram_code, output_file):
    """Generate a PlantUML diagram."""
    with open("temp_diagram.puml", "w") as file:
        file.write(diagram_code)

    try:
        # Run PlantUML locally to generate the diagram
        import subprocess
        subprocess.run(["java", "-jar", PLANTUML_JAR, "temp_diagram.puml", "-o", output_file], check=True)
        print(f"Diagram generated: {output_file}")
    except Exception as e:
        print(f"Error generating diagram: {e}")

# Create a workflow diagram
def create_workflow_diagram():
    diagram_code = """
    @startuml
    actor User
    participant "GUI" as GUI
    participant "Authentication Module" as Auth
    participant "AI API (OpenAI)" as API
    participant "File Storage" as Storage
    participant "Email System" as Email

    User -> GUI: Logs in
    GUI -> Auth: Authenticate
    Auth --> GUI: Success/Failure
    User -> GUI: Enter Topic
    GUI -> API: Request Article
    API --> GUI: Return Article
    User -> GUI: Save Article
    GUI -> Storage: Save File
    User -> GUI: Email Article
    GUI -> Email: Send Email
    Email --> GUI: Confirmation
    @enduml
    """
    generate_diagram(diagram_code, "/home/tahraun/Documents/AI_Article/AI-Article-Writer/01. PlantUML/workflow.png")

# Create an architecture diagram
def create_architecture_diagram():
    diagram_code = """
    @startuml
    rectangle GUI {
        component "Login" as Login
        component "Article Generator" as Generator
        component "File Manager" as FileManager
    }

    rectangle Backend {
        component "Authentication Service" as Auth
        component "Database" as DB
        component "Email Service" as Email
        component "AI API (OpenAI)" as OpenAI
    }

    Login --> Auth
    Generator --> OpenAI
    FileManager --> DB
    Generator --> Email
    @enduml
    """
    generate_diagram(diagram_code, "/home/tahraun/Documents/AI_Article/AI-Article-Writer/01. PlantUML/architecture.png")

# Initialize the SQLite database
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

# Hash a password using SHA256
def hash_password(password):
    """Hash a password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest()

# Save a new user to the in-memory dictionary
def save_user(username, password):
    """Save a new user to the in-memory dictionary."""
    hashed_password = hash_password(password)
    if username in users:
        Messagebox.show_error("Username already exists. Please choose a different username.", "Registration Error")
        return False
    users[username] = hashed_password
    Messagebox.show_info("User registered successfully!", "Registration Success")
    return True

# Authenticate a user by checking their credentials
def authenticate_user(username, password):
    """Authenticate a user by checking their credentials."""
    hashed_password = hash_password(password)
    if username in users and users[username] == hashed_password:
        return True
    else:
        Messagebox.show_error("Invalid username or password.", "Login Error")
        return False

# Generate an article using OpenAI
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

# Save the article to a file
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

# Clear the output area
def clear_output(output_area):
    """Clear the output area."""
    output_area.delete(1.0, END)

# Create the GUI
def login_screen(app):
    """Display the login screen."""
    for widget in app.winfo_children():
        widget.destroy()

    app.title("Tahraun's AI Article Generator")

    ttk.Label(app, text="Login", font=("Helvetica", 20, "bold")).pack(pady=20)
    ttk.Label(app, text="LinkedIn Article Generator", font=("Helvetica", 16)).pack(pady=20)
    username_entry = ttk.Entry(app, font=("Helvetica", 14), width=30)
    username_entry.pack(pady=10)
    username_entry.insert(0, "Username")
    password_entry = ttk.Entry(app, font=("Helvetica", 14), show="*", width=30)
    password_entry.pack(pady=10)
    password_entry.insert(0, "Password")

    # Authenticate the user
    def login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()
        if not username or not password:
            Messagebox.show_error("Username and password cannot be empty.", "Login Error")
            return
        if authenticate_user_from_db(username, hash_password(password)):
            article_creator_screen(app)
        else:
            Messagebox.show_error("Invalid username or password.", "Login Error")

    ttk.Button(app, text="Login", bootstyle=PRIMARY, command=login).pack(pady=10)
    ttk.Button(app, text="Register", bootstyle=SUCCESS, command=lambda: register_screen(app)).pack(pady=10)
    
# Register the user
def register_screen(app):
    """Display the registration screen."""
    for widget in app.winfo_children():
        widget.destroy()

    app.title("Tahraun's AI Article Generator")

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
        if not username or not password:
            Messagebox.show_error("Username and password cannot be empty.", "Registration Error")
            return
        save_user_to_db(username, hash_password(password))
        login_screen(app)

    ttk.Button(app, text="Register", bootstyle=SUCCESS, command=register).pack(pady=10)
    ttk.Button(app, text="Back to Login", bootstyle=INFO, command=lambda: login_screen(app)).pack(pady=10)

# Display Article Generator Screen
def article_creator_screen(app):
    """Display the article creator screen."""
    for widget in app.winfo_children():
        widget.destroy()

    app.title("Tahraun's AI Article Generator")

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

# Initializes the program
if __name__ == "__main__":
    initialize_db()
    create_gui()
    create_workflow_diagram()
    create_architecture_diagram()
