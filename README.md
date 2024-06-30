[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT license.

# AI Medical Assistant

![chatbot_blog-1](https://github.com/Dennis-Maigua/ai-medical-assistant/assets/32156551/37f7de8b-e13c-42fd-a711-09d6122677cb)

This project implements a conversational ai chatbot using RASA Open Source Framework, Flask, and Python.

### Design

1. **Intents:** represent the goal or purpose behind a user's input. They capture what the user wants to do or achieve through their message.
2. **Responses:** are the messages or actions that the chatbot produces to interact with the user. These are predefined based on the identified intent.
3. **Actions:** refer to the tasks or operations that the chatbot can perform in response to a user's input. They are designed to provide relevant information.

# Setup

### 1. Clone the repository

Download and open the project in your local machine:

  ```bash
    $ cd Desktop
    $ git clone https://github.com/Dennis-Maigua/ai-medical-assistant.git
    $ cd ai-medical-assistant-main/ai-medical-assistant-main
  ```

### 2. Create a virtual environment

Build a venv and activate it inside the project:

   ```bash
     $ python -m venv venv
     $ ./venv/Scripts/activate
   ```
   
### 3. Install packages and dependencies

Install `rasa` and python `requirements`:
  
   ```bash
     $ pip install rasa
     $ pip install -r requirements.txt
   ```

# Testing and Performance

### 1. Train the model

Map all the datasets, intents, responses, and actions for the chatbot:
  
   ```bash
     $ rasa train
   ```

2. Interact with the Chatbot

- Open Terminal 1 and run:

```bash
    # rasa run actions
```

- Open Terminal 2 and run:

```bash
    # rasa shell
```

# Contributing:

We welcome contributions from developers, legal experts, and blockchain enthusiasts. Feel free to fork the repository, make improvements, and submit pull requests.
