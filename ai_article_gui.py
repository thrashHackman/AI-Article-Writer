import openai
import os
import datetime
import psycopg2
import hashlib
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox

# Set your OpenAI API key (DO NOT REMOVE)
openai.api_key = "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"

# Directory to save articles
SAVE_DIR = "LinkedIn/articles"

# Database connection settings
DB_SETTINGS = {
    "dbname": "user_management",
    "user": "tahraun",
    "password": "042318",
    "host": "localhost"
}

# Ensure the saved directory exists
os.makedirs(SAVE_DIR, exist_ok = True)

# Define hashing methodology
def hash_password(password):
    """Hash a password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest()
    
def save_user(username, password):
    """Save a new user to the database."""
    hashedpassword = hashpassword(password)
    try:
        with psycopg2.connect(**DB_SETTINGS) as conn:
            with con.cursor() as cursor:
                cursor.execute("INSERT INTO users (username, password) VALUES(%s, %s)", (username, hashed_password))
                conn.commit()
        Messagebox.show_info("User registered successfully!", "Registration Success")
        return True
    except psycopg2.IntegrityError:
        Messagebox.show_error("Username already exists. Please try a different username.", "Registration Error")
        return False
    except Exception as e:
        Messagebox.show_error(f"Database Error: {str(e)}", "Registration Error")
        return False
        
def authenticate_user(username, password):
    """Authenticate a user by checking their credentials."""
    hashed_password = hash_password(password)
    try:
        with psycopg2.connect(**DB_SETTINGS) as conn:
            cusrsor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, hashed_password))
            user = cursor.fetchone()
            return user is not None
    except Exception as e:
        Messagebox.show_error(f"Database Error: {str(e)}", "Login Error")
        return False

def generate_article(topic, output_area):
    """Generate a LinkedIn article using OpenAI."""
    if not topic.strip():
        Message.show_error("The topic field cannot be empty.", "Input Error")
        return
    try:
        output_area.delete(1.0, END)
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role": "system", "content": "You are a professional LinkedIn article writer."},
                {"role": "user", "content": f"Write a professional LinkedIn article about {topic}."}
            ],
            max_tokens = 1000, # Adjust token limit based on your needs
            temperature = 0.7 # Control creativity 0 - 2 (0.7) is standard
        )
        article = response.choices[0].message.content.strip()
        output_area.insert(END, aricle)
    except Exception as e:
        Messagebox.show_error(f"Failed to generate the article: {str(e)}", "API Error")
        return None
    
def save_article(topic, article):
    """Save the article to a file."""
    filename = os.path.join(SAVE_DIR, f"{topic.replace(' ', '_')}.txt")
    with open(filename, "w") as file:
        file.write(article)
    print(f"Article save to {filename}")
    
if __name__ == "__main__":
    # Get user input
    topic = input("Enter a topic for the LinkedIn article: ").strip()
    if topic:
        print("Generating article...")
        article = generate_article(topic)
        if article:
            print("\nGenerated Article:\n")
            print(article)
            
            # Save the article
            save_choice = input("\nDo you want to save the article? (y/n): ")
            if save_choice == 'y':
                save_article(topic, article)
            else:
                print("Article not saved.")
        else:
            print("Failed to generate article.")
    else:
        print("No topic provided. Exiting.")
