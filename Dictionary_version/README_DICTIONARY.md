# Tahraun's AI Article Generator

Tahraun's AI Article Generator is a Python-based application that uses OpenAI's GPT-3.5 model to generate LinkedIn articles. It offers secure user authentication, file management, and diagram generation, presented in a responsive GUI.


## Table of Contents
1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
   - [Step 1: Clone the Repository](#step-1-clone-the-repository)
   - [Step 2: Install Python Dependencies](#step-2-install-python-dependencies)
   - [Step 3: Set Up PlantUML](#step-3-set-up-plantuml)
   - [Step 4: Initialize the Database](#step-4-initialize-the-database)
5. [Usage](#usage)
6. [Key Components](#key-components)
   - [SQLite Database](#sqlite-database)
   - [GUI Features](#gui-features)
   - [PlantUML Integration](#plantuml-integration)
7. [Future Functionality](#future-functionality)
8. [Troubleshooting](#troubleshooting)
9. [Author](#author)

---

## Features

- **User Authentication**: Secure login and registration with hashed passwords stored in SQLite.
- **Article Generation**: Professional LinkedIn articles generated using OpenAI GPT-3.5.
- **File Management**: Articles are saved with timestamped filenames.
- **Diagram Generation**: PlantUML creates workflow and architecture diagrams.
- **Interactive GUI**: Built using `ttkbootstrap` for a sleek, modern design.

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

Ensure you have the following:
- Python 3.7 or higher
- OpenAI API Key
- Java installed for PlantUML
- SQLite3
- Required Python libraries:
  - `openai`
  - `ttkbootstrap`
  - `plantuml`

---

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-repo/AI_Article_Generator.git
cd AI_Article_Generator
```

### Step 2: Install Python Dependencies

Install the required Python libraries:
```bash
pip install openai ttkbootstrap plantuml
```

### Step 3: Set Up PlantUML

1. **Download PlantUML JAR**:
   - Visit [PlantUML Downloads](https://plantuml.com/download).
   - Save the `plantuml.jar` file to a directory, e.g., `/home/user/plantuml/`.

2. **Verify Java Installation**:
   ```bash
   java -version
   ```

3. **Update `PLANTUML_JAR` Path**:
   Open the script and ensure this line points to your `plantuml.jar` file:
   ```python
   PLANTUML_JAR = "/path/to/your/plantuml.jar"
   ```

### Step 4: Initialize the Database

Run the following script to create the SQLite database:
```bash
python ai_article_generator.py
```
This step ensures the `users.db` file is created and ready for user authentication.

---

## Usage

1. **Run the Application**:
   ```bash
   python ai_article_generator.py
   ```

2. **User Login/Registration**:
   - New users can register using the "Register" button.
   - Existing users can log in to access the article generator.

3. **Generate Articles**:
   - Enter a topic in the text field and click "Generate Article."
   - Save the article or clear the output using the respective buttons.

4. **View Diagrams**:
   - Workflow and architecture diagrams are generated in `output/diagrams/`.

---

## Key Components

### SQLite Database
- **Path**: `users.db`
- **Schema**:
  ```sql
  CREATE TABLE IF NOT EXISTS users (
      username TEXT PRIMARY KEY,
      password TEXT NOT NULL
  );
  ```

### GUI Features
- **Login Screen**:
  - Username and password fields.
  - "Show Password" toggle button (`👁️` to show, `🙈` to hide).
- **Article Generator**:
  - Input field for topics.
  - Buttons for generating, saving, and clearing articles.

### PlantUML Integration
- **Workflow Diagram**:
  Illustrates user interactions with the system.
- **Architecture Diagram**:
  Visualizes system components and their connections.

---

## Future Functionality

- **Email Integration**:
  - Send articles directly via email from the application.

- **Real-Time Collaboration**:
  - Allow multiple users to collaborate on articles in real time.

- **Enhanced Analytics**:
  - Provide detailed statistics on article generation and usage.

---

## Troubleshooting

### PlantUML Errors
- Ensure `java` is installed and accessible from your system PATH.
- Verify the `PLANTUML_JAR` variable points to the correct file.

### OpenAI API Issues
- Confirm your API key is valid and active.
- Check API usage limits on your OpenAI account.

### Missing Modules
- Install missing Python modules with:
  ```bash
  pip install <module-name>
  ```

---

## Author

- **Tahraun**  
  [LinkedIn](https://www.linkedin.com/in/tahraun)