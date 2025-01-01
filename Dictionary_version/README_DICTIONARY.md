# **AI Article Generator**

## **Table of Contents**
1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Code Overview](#code-overview)
7. [Troubleshooting](#troubleshooting)
8. [Future Enhancements](#future-enhancements)
9. [License](#license)

---

## **Introduction**

The **AI Article Generator** is a user-friendly desktop application designed to generate professional LinkedIn-style articles using OpenAI's GPT-3.5 model. This application allows users to register and log in, enter a topic, and generate AI-driven articles, which can be saved to a local directory.

---

## **Features**

- **User Authentication**: Register and log in with secure password hashing.
- **AI-Powered Article Generation**: Generate detailed LinkedIn articles based on user-provided topics.
- **Modern GUI**: Built using `ttkbootstrap` for a sleek and responsive interface.
- **File Management**: Save articles to a designated folder with a timestamped filename.
- **In-Memory User Management**: Eliminates the need for a database by storing users in memory.

---

## **Technologies Used**

- **Programming Language**: Python 3.11+
- **Libraries**:
  - `openai`: For GPT-3.5 API integration.
  - `ttkbootstrap`: For modern GUI design.
  - `hashlib`: For secure password hashing.
  - `os`: For file management.
  - `datetime`: For timestamping saved articles.

---

## **Installation**

### **Prerequisites**
1. Python 3.11 or later
2. OpenAI API Key

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ai-article-generator.git
   cd ai-article-generator
   ```

2. Install required dependencies:
   ```bash
   pip install openai ttkbootstrap
   ```

3. Set up the directory for saving articles:
   - By default, articles are saved to `LinkedIn/articles`. You can change this by modifying the `SAVE_DIR` variable in the code.

4. Set your OpenAI API key:
   - Replace the placeholder in the code:
     ```python
     openai.api_key = "YOUR_API_KEY"
     ```

5. Run the application:
   ```bash
   python3 ai_article_gui.py
   ```

---

## **Usage**

1. **Launch the Application**:
   - Run the script to open the GUI.
   - Enter your credentials to log in or register as a new user.

2. **Generate Articles**:
   - Enter a topic in the input field and click "Generate Article."
   - The article will appear in the text area.

3. **Save Articles**:
   - Click "Save Article" to save the generated article to the designated folder.

4. **Clear Output**:
   - Click "Clear Output" to reset the text area for a new article.

5. **Logout**:
   - Click "Logout" to return to the login screen.

---

## **Code Overview**

### **User Management**
- **Registration**:
  - Users are stored in an in-memory dictionary with hashed passwords.
  ```python
  users[username] = hashed_password
  ```
- **Login**:
  - Validates credentials against the in-memory dictionary.
  ```python
  if username in users and users[username] == hashed_password:
  ```

### **Article Generation**
- Powered by OpenAI's GPT-3.5 API.
- The `generate_article` function generates articles based on user-provided topics:
  ```python
  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
          {"role": "system", "content": "You are a professional LinkedIn article writer."},
          {"role": "user", "content": f"Write an article about {topic.strip()}."}
      ],
      max_tokens=3000,
      temperature=1.3
  )
  ```

### **File Saving**
- Articles are saved with sanitized filenames and timestamps:
  ```python
  file_name = f"{timestamp}_{sanitized_topic}.txt"
  ```

---

## **Troubleshooting**

### **Common Issues**
1. **OpenAI API Key Error**:
   - Ensure you have replaced the placeholder API key with a valid key:
     ```python
     openai.api_key = "YOUR_API_KEY"
     ```

2. **Dependencies Not Installed**:
   - Install required libraries:
     ```bash
     pip install openai ttkbootstrap
     ```

3. **Save Directory Error**:
   - Ensure the save directory exists or modify the `SAVE_DIR` path.

4. **Invalid Login Credentials**:
   - Check if the username and password are correctly registered in memory.

---

## **Future Enhancements**

- Add persistent storage for user management using a database.
- Include a feature to edit or delete saved articles.
- Support for generating articles in multiple languages.

---

## **License**

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).