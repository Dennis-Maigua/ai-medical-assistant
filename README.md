[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT license.

# Medoc - AI Medical Assistant

![chatbot_blog-1](https://github.com/Dennis-Maigua/ai-medical-assistant/assets/32156551/37f7de8b-e13c-42fd-a711-09d6122677cb)

This project implements a Conversational AI using RASA Open Source Framework. The Chatbot requests the user's symptoms, identifies the disease (diagnosis), recommends medication or doctor consultation, and provides information about any disease (if asked by a user) through the WikipediaApi.

# Design Features

1. Natural Language Understanding (NLU).

2. Dialogue Management.
  
3. Training Pipeline.

4. Integration and Deployment.

# Environment (Windows, Mac, Linux)

>**Note**: Make sure you have installed the latest version of [Git](https://git-scm.com/downloads) and [Python](https://www.python.org/downloads/release/python-31011/) before proceeding. By default, `pip` comes pre-installed with Python. If missing, you can download it [here](https://bootstrap.pypa.io/get-pip.py) and open to install it automatically.

Open a new terminal and run the following commands (one-by-one):

  ```bash
    $ git --version
    $ python --version
    $ pip --version
  ```

# Setup Installation

### Step 1. Clone the Repository

Clone and open the project in your local machine `desktop`:

  ```bash
    $ cd Desktop
    $ git clone https://github.com/Dennis-Maigua/ai-medical-assistant.git
    $ cd ai-medical-assistant
  ```

### Step 2. Create a Virtual Environment

Build and activate a `venv` folder inside the project:

  ```bash
   $ python -m venv venv
   $ venv/Scripts/activate
  ```
   
### Step 3. Install Packages and Dependencies

Install `rasa` and `python requirements` for running the project:
  
  ```bash
   $ pip install rasa
   $ rasa --version 
   $ pip install -r requirements.txt
  ```

# Testing and Performance

>**Note**: Ignore all Deprecation Warnings in colors Red and Yellow! Errors or bugs that break the code functionality should be displayed in white, of which there are none currently. 😊

### Step 4. Train the Model

Always train the `NLU model` after making any code changes to `update` the chatbot:
  
  ```bash
   $ rasa train
  ```

### Step 5. Run the Chatbot

Open another `two` separate terminals and run the following commands:

- Terminal 1 (Actions):

  ```bash
    $ rasa run actions
  ```

- Terminal 2 (Rasa Server):

  ```bash
    # For frontend chatbot
    $ venv/Scripts/activate
    $ rasa run --model models --enable-api --cors "*"

    # For backend chatbot
    $ venv/Scripts/activate
    $ rasa shell
  ```

- Terminal 3 (Frontend Chatbot):

  ```bash
    $ venv/Scripts/activate
    $ python app.py
  ```

# Contributing:

We welcome contributions from developers, IT experts, and technology enthusiasts. Feel free to fork the repository, make improvements, and submit pull requests. Happy coding!