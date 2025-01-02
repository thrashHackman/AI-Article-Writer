# Tahraun's AI Article Generator

Tahraun's AI Article Generator is a Python application designed to generate LinkedIn articles using OpenAI's GPT-3.5 model. It features secure user authentication, file management, and workflow/architecture diagram generation with PlantUML. This project is built with Python modules and libraries for a robust, interactive GUI experience.

---

## Table of Contents
1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Code Breakdown](#code-breakdown)
   - [Imports](#imports)
   - [Constants](#constants)
   - [Functions](#functions)
6. [Usage](#usage)
7. [Future Enhancements](#future-enhancements)
8. [Troubleshooting](#troubleshooting)
9. [Author](#author)

---

## Features

- Secure user authentication with SQLite and hashed passwords.
- AI-powered LinkedIn article generation using OpenAI's GPT-3.5.
- PlantUML integration for workflow and architecture diagrams.
- Modern GUI with responsive components and toggled password visibility.

---

## Project Structure

```
AI_Article_Generator/
├── LinkedIn/articles/        # Directory for saved articles
├── output/diagrams/          # Directory for diagrams
├── users.db                  # SQLite database
├── temp_diagram.puml         # Temporary PlantUML file
├── ai_article_generator.py   # Main Python script
└── README.md                 # Documentation
```

---

## Prerequisites

- Python 3.7 or higher
- OpenAI API Key
- Java installed for PlantUML
- SQLite3
- Required Python modules:
  - `openai`
  - `ttkbootstrap`
  - `sqlite3`
  - `hashlib`
  - `plantuml`

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/AI_Article_Generator.git
   cd AI_Article_Generator
   ```

2. **Install Python Dependencies**:
   ```bash
   pip install openai ttkbootstrap plantuml
   ```

3. **Set Up PlantUML**:
   - Download the `plantuml.jar` file from the [PlantUML website](https://plantuml.com/download).
   - Update the `PLANTUML_JAR` variable in the script with the correct path.

4. **Initialize the Database**:
   Run the script to set up the SQLite database:
   ```bash
   python ai_article_generator.py
   ```

---

## Code Breakdown

### Imports

1. **Core Imports**:
   - `os`: Manages file paths and directories.
   - `datetime`: For timestamps when saving articles.
   - `hashlib`: Used for SHA256 password hashing.
   - `sqlite3`: Enables SQLite database integration.

2. **External Libraries**:
   - `openai`: Interacts with the OpenAI API for article generation.
   - `plantuml`: Automates diagram generation with PlantUML.
   - `ttkbootstrap`: Provides modern GUI design.

3. **Constants**:
   - `PLANTUML_JAR`: Path to the PlantUML JAR file for diagram generation.
   - `DB_FILE`: SQLite database file path.
   - `SAVE_DIR`: Directory to save articles.

---

### Functions

#### **Database Initialization**
```python
def initialize_db():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        """)
        conn.commit()
```
This function creates a `users` table in the SQLite database for storing usernames and hashed passwords.

---

#### **Password Handling**
- **Hash Password**:
   ```python
   def hash_password(password):
       return hashlib.sha256(password.encode()).hexdigest()
   ```
   Hashes user passwords using SHA256 for secure storage.

---

#### **Authentication**
- **Save User**:
   ```python
   def save_user_to_db(username, hashed_password):
       # Adds a new user to the database.
   ```
- **Authenticate User**:
   ```python
   def authenticate_user_from_db(username, hashed_password):
       # Checks if a username and hashed password match an entry in the database.
   ```

---

#### **Article Management**
- **Generate Article**:
   ```python
   def generate_article(topic, output_area):
       response = openai.ChatCompletion.create(
           model="gpt-3.5-turbo",
           messages=[
               {"role": "system", "content": "You are a professional LinkedIn article writer."},
               {"role": "user", "content": f"Write an article about {topic.strip()}."}
           ],
           max_tokens=3000,
           temperature=1.3
       )
       output_area.insert(END, response.choices[0].message.content.strip())
   ```
   Uses OpenAI's GPT-3.5 model to generate a professional article based on the given topic.

- **Save Article**:
   ```python
   def save_article(output_area, topic):
       file_name = f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_{sanitized_topic}.txt"
       file_path = os.path.join(SAVE_DIR, file_name)
       with open(file_path, "w") as file:
           file.write(article)
   ```

---

#### **Diagram Generation**
- **Workflow Diagram**:
   ```python
   def create_workflow_diagram():
       diagram_code = """
       @startuml
       actor User
       participant "GUI" as GUI
       ...
       """
       generate_diagram(diagram_code, "output/diagrams/workflow.png")
   ```
   Generates a UML workflow diagram illustrating user interactions.

- **Architecture Diagram**:
   ```python
   def create_architecture_diagram():
       diagram_code = """
       @startuml
       rectangle GUI {
           component "Login" as Login
           ...
       }
       """
       generate_diagram(diagram_code, "output/diagrams/architecture.png")
   ```

---

#### **GUI Components**
- **Login Screen**:
   Displays username/password fields with "Show Password" toggle functionality.
- **Article Generator Screen**:
   Provides input fields for topics and buttons for generating, saving, and clearing articles.

---

## Usage

1. **Run the Application**:
   ```bash
   python ai_article_generator.py
   ```

2. **Authenticate Users**:
   - Register as a new user.
   - Log in with your credentials.

3. **Generate Articles**:
   - Enter a topic and click "Generate Article."
   - Save or clear the article as needed.

4. **View Diagrams**:
   - Check `output/diagrams` for generated diagrams.

---

## Future Enhancements

- **Email Integration**: Allow users to send generated articles via email.
- **Collaboration Features**: Real-time article collaboration.
- **Detailed Analytics**: Provide article insights and statistics.

---

## Troubleshooting

### PlantUML Errors
- Ensure `java` is installed and accessible in your PATH.
- Verify the `PLANTUML_JAR` variable is set correctly.

### OpenAI API Issues
- Confirm your API key is valid and active.
- Check your API usage limits.

---

## Author

- **Tahraun**  
  [LinkedIn](https://www.linkedin.com/in/tahraun)

---

This `README.md` is designed to provide complete transparency and guidance for users and developers.
``` 