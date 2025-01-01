# AI-Article-Writer

Below is the README.md file for your project, tailored for GitHub:

AI Article Generator

Table of Contents
	1.	Introduction
	2.	Features
	3.	Technologies Used
	4.	Hardware and Setup
	5.	Installation
	6.	Usage
	7.	Code Overview
	8.	Troubleshooting
	9.	Future Enhancements
	10.	License

Introduction

The AI Article Generator is a robust application designed to generate professional LinkedIn-style articles using OpenAI’s GPT-3.5. It features secure user authentication with PostgreSQL, password hashing with SHA-256, and a modern GUI built with ttkbootstrap. Designed for use on a Raspberry Pi 5 with an Argon M.2 V3 case, it efficiently integrates AI with scalable hardware.

Features
	•	AI-Powered Article Generation: Create LinkedIn-style articles using OpenAI GPT-3.5.
	•	Secure User Management: Handle registration and login with hashed passwords.
	•	Modern GUI: Built using ttkbootstrap for a responsive and polished user interface.
	•	File Management: Save generated articles with sanitized filenames and timestamps.
	•	Error Handling: Comprehensive feedback for input validation, database queries, and API interactions.

Technologies Used

Programming Languages
	•	Python 3.11+

Frameworks and Libraries
	•	openai: For GPT-3.5 API integration.
	•	ttkbootstrap: Modern styling for the GUI.
	•	Pillow: Image rendering support (required by ttkbootstrap).
	•	psycopg2-binary: PostgreSQL interaction.

Database
	•	PostgreSQL: User management and authentication.

Hardware
	•	Raspberry Pi 5
	•	Argon M.2 V3 Case (1TB M.2 SSD)

Hardware and Setup

Required Hardware
	•	Raspberry Pi 5
	•	Argon M.2 V3 Case with a 1TB M.2 SSD
	•	Power supply, monitor, keyboard, mouse

Formatting the SSD
	1.	Install gparted:

sudo apt update
sudo apt install gparted -y


	2.	Format the SSD as ext4:
	•	Open gparted: sudo gparted
	•	Select the SSD, create a partition table (GPT), and format it as ext4.
	3.	Mount the SSD:

sudo mkdir /mnt/ssd
sudo mount /dev/sda1 /mnt/ssd

Installation
	1.	Clone the repository:

git clone https://github.com/your-repo/ai-article-generator.git
cd ai-article-generator


	2.	Install Python dependencies:

pip3 install -r requirements.txt


	3.	Set up PostgreSQL:

sudo -i -u postgres
psql
CREATE DATABASE user_management;
CREATE USER myuser WITH PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE user_management TO myuser;


	4.	Create the users table:

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);


	5.	Update the database settings in ai_article_gui.py:

DB_SETTINGS = {
    "dbname": "user_management",
    "user": "myuser",
    "password": "mypassword",
    "host": "localhost"
}


	6.	Run the application:

python3 ai_article_gui.py

Usage
	1.	Launch the application:

python3 ai_article_gui.py


	2.	Register or Login:
	•	Register a new account or log in with existing credentials.
	3.	Generate Articles:
	•	Enter a topic and click “Generate Article” to create professional LinkedIn content.
	4.	Save Articles:
	•	Save the generated article to a timestamped file.

Code Overview

User Authentication
	•	Registration: Saves new users to the PostgreSQL database with hashed passwords.
	•	Login: Authenticates users by verifying hashed passwords.

Article Generation
	•	Uses OpenAI GPT-3.5 API to generate articles based on user-provided topics:

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a professional LinkedIn article writer."},
        {"role": "user", "content": f"Write a professional LinkedIn article about {topic}."}
    ]
)



File Saving
	•	Articles are saved with sanitized filenames:

file_name = f"{timestamp}_{sanitized_topic}.txt"

Troubleshooting

Common Issues and Fixes
	1.	Cannot Import ImageTK from PIL:
	•	Reinstall Pillow:

pip3 uninstall Pillow
pip3 install Pillow


	2.	Database Error: relation "users" does not exist:
	•	Ensure the users table is created:

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);


	3.	Permission Denied for Table users:
	•	Grant permissions:

GRANT ALL PRIVILEGES ON TABLE users TO myuser;


	4.	No Feedback After Login or Register:
	•	Debug by adding print() statements in the login() and register() functions.

Future Enhancements
	•	Implement email-based account recovery.
	•	Add multilingual support for generated articles.
	•	Introduce role-based user management (e.g., admin vs. standard users).
