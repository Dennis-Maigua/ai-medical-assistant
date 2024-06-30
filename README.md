[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT license.

# Medoc - AI Medical Assistant

![chatbot_blog-1](https://github.com/Dennis-Maigua/ai-medical-assistant/assets/32156551/37f7de8b-e13c-42fd-a711-09d6122677cb)

This project implements a Conversational AI Chatbot using RASA Open Source Framework, Flask, and Python.

# Design Features

### 1. Natural Language Understanding (NLU)
- **Intent Classification**: Identifies the intent or purpose behind user messages (e.g., requesting information, asking a question).
- **Entity Recognition**: Extracts specific pieces of information (entities) from user messages (e.g., names, diseases, symptoms).

### 2. Dialogue Management
- **State Management**: Tracks the context of the conversation to maintain coherence and relevance in responses over multiple turns.
- **Policy-Based Decision Making**: Determines the next action or response based on the current dialogue state, past interactions, and predefined rules.

### 3. Responses and Actions
- **Response Generation**: Crafts appropriate replies or actions based on identified intents, entities, and current dialogue context.
- **Action Execution**: Performs backend operations (e.g., database queries, API calls) to fulfill user requests or provide information.
  
### 4. Training Pipeline:
- **Data Annotation**: Involves labeling datasets with intents and entities to train the NLU model effectively.
- **Model Training**: Uses machine learning algorithms (often neural networks) to train NLU and dialogue management models on annotated datasets.
- **Evaluation and Iteration**: Tests and refines the chatbot's performance based on real or simulated interactions to improve accuracy and user satisfaction.

### 5. Integration and Deployment:
- **Platform Integration**: Allows deployment on various platforms (e.g., web, apps, messaging platforms) to interact with users where they are.
- **Continuous Learning**: Supports ongoing updates and improvements based on user feedback and evolving needs.

# Setup Installation

>**Note**: Make sure you have installed the latest version of [Git](https://git-scm.com/downloads) and [Python](https://www.python.org/downloads/release/python-31011/) before proceeding. By default, `pip` comes pre-installed with Python. Otherwise if not, you can download it from [here](https://bootstrap.pypa.io/get-pip.py) and open it to install automatically.

Open a new terminal and run the following commands to confirm installation:
  ```bash
    $ git --version
    $ python --version
    $ pip --version
  ```

### Step 1. Clone the Repository

Download and extract the project into a folder:

  ```bash
    $ cd Desktop
    $ git clone https://github.com/Dennis-Maigua/ai-medical-assistant.git
  ```

### Step 2. Open the project

Open the root folder of the project:

  ```bash
    $ cd ai-medical-assistant-main
  ```

### Step 3. Create a virtual environment

Build a venv inside the root folder and activate it:

  ```bash
   $ python -m venv venv
   $ ./venv/Scripts/activate
  ```
   
### Step 4. Install packages and dependencies

Install `rasa` and other python `requirements` (in the venv):
  
  ```bash
   $ pip install rasa
   $ pip install -r requirements.txt
  ```

# Testing and Performance

### Step 5. Configure Rasa

Initialize Rasa configuration directly without prompts:
  
  ```bash
   $ rasa init --no-prompt
  ```

### Step 6. Move and Replace files

Inside the root folder `(ai-medical-assistant-main)`, there is another inner folder `(ai-medical-assistant-main)`.

  ```bash
    ### FOLLOW THE INSTRUCTIONS BELOW !!! ###
    # - Move all the files from the inner folder to the root folder
    # - Replace the existing replicas in the root folder
    # - Then delete the empty inner folder
  ```

### Step 7. Train the model

Train NLU and dialogue management models on annotated datasets for the chatbot:
  
  ```bash
   $ rasa train
  ```

### Step 8. Interact with the Chatbot

On the same terminal, run the Actions:

  ```bash
    $ rasa run actions
  ```

Open another terminal and run the Chatbot:

  ```bash
    $ rasa shell
  ```

# Contributing:

We welcome contributions from developers, legal experts, and blockchain enthusiasts. Feel free to fork the repository, make improvements, and submit pull requests.
