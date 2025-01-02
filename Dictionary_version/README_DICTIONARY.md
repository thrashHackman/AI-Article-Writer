# Tahraun's AI Article Generator

Tahraun's AI Article Generator is a Python-based application that uses OpenAI's GPT-3.5 model to generate LinkedIn articles, allowing users to save and manage them efficiently. This project integrates SQLite for user authentication and PlantUML for visual documentation of workflows and architecture.

## Features

- **User Authentication**: Secure user registration and login using hashed passwords stored in an SQLite database.
- **Article Generation**: Generate professional LinkedIn articles using OpenAI's GPT-3.5-turbo model.
- **File Management**: Save generated articles with timestamped filenames in a structured directory.
- **Diagram Generation**: Automatically generate workflow and architecture diagrams using PlantUML.
- **Responsive GUI**: Built with `ttkbootstrap` for a modern and user-friendly interface.

## Project Structure

```
AI_Article_Generator/
├── LinkedIn/articles/        # Directory for saving articles
├── output/diagrams/          # Directory for storing generated diagrams
├── users.db                  # SQLite database for user authentication
├── temp_diagram.puml         # Temporary file for PlantUML diagrams
├── ai_article_generator.py   # Main Python application
└── README.md                 # Documentation
```

## Prerequisites

- Python 3.7 or higher
- OpenAI API key
- PlantUML (local installation with JAR file)
- SQLite3
- Required Python modules:
  - `openai`
  - `ttkbootstrap`
  - `sqlite3`
  - `hashlib`
  - `datetime`

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/AI_Article_Generator.git
   cd AI_Article_Generator
   ```

2. **Install Dependencies**:
   ```bash
   pip install openai ttkbootstrap plantuml
   ```

3. **Set Up PlantUML**:
   - Download the `plantuml.jar` file from the [PlantUML website](https://plantuml.com/download).
   - Update the `PLANTUML_JAR` variable in the script with the path to your `plantuml.jar`.

4. **Initialize Database**:
   Run the script to create the SQLite database:
   ```bash
   python ai_article_generator.py
   ```

## Usage

1. **Start the Application**:
   ```bash
   python ai_article_generator.py
   ```

2. **User Authentication**:
   - **Register**: Create a new user account.
   - **Login**: Access the article generator interface.

3. **Generate Articles**:
   - Enter a topic and click "Generate Article" to create an article using GPT-3.5.
   - Save articles with timestamped filenames.

4. **View and Manage Diagrams**:
   - Workflow and architecture diagrams are automatically generated and saved in `output/diagrams/`.

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
- **Login/Registration Screen**:
  - Username and password fields with placeholders.
  - "Show Password" toggle button (`👁️` to show, `🙈` to hide).
- **Article Generator Screen**:
  - Text field for entering topics.
  - Buttons for generating, saving, clearing, and logging out.

### PlantUML Integration
- **Workflow Diagram**: Shows user interactions with the system.
- **Architecture Diagram**: Visualizes system components and their interactions.

## Troubleshooting

1. **PlantUML Errors**:
   - Ensure `java` is installed and properly configured in your system PATH.
   - Verify the `PLANTUML_JAR` path is correct.

2. **OpenAI API Key Issues**:
   - Ensure you have a valid API key and it is correctly set in the `openai.api_key` variable.

3. **Module Import Errors**:
   - Install missing modules using `pip install <module-name>`.

## Future Enhancements

- Add email functionality for sharing articles directly from the application.
- Integrate more detailed reporting features.
- Enhance the GUI with themes and additional customization.

## Author

- **Tahraun** - [LinkedIn](https://www.linkedin.com/in/tahraun)
