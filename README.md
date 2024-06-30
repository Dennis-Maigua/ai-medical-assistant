[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT license.

# Medoc - AI Medical Assistant

![chatbot_blog-1](https://github.com/Dennis-Maigua/ai-medical-assistant/assets/32156551/37f7de8b-e13c-42fd-a711-09d6122677cb)

This project implements a Conversational AI using RASA Open Source Framework. The Chatbot requests the user's symptoms, identifies the disease (diagnosis), recommends medication or doctor consultation, and provides information about any disease (if asked by a user) through the WikipediaApi.

# Design features

### Natural Language Understanding (NLU)
- **Intent Classification**: Identifies the intent or purpose behind user messages (e.g., requesting information, asking a question).
- **Entity Recognition**: Extracts specific pieces of information (entities) from user messages (e.g., names, diseases, symptoms).

### Dialogue Management
- **State Management**: Tracks the context of the conversation to maintain coherence and relevance in responses over multiple turns.
- **Policy-Based Decision Making**: Determines the next action or response based on the current dialogue state, past interactions, and predefined rules.

### Responses and Actions
- **Response Generation**: Crafts appropriate replies or actions based on identified intents, entities, and current dialogue context.
- **Action Execution**: Performs backend operations (e.g., database queries, API calls) to fulfill user requests or provide information.
  
### Training Pipeline
- **Data Annotation**: Involves labeling datasets with intents and entities to train the NLU model effectively.
- **Model Training**: Uses machine learning algorithms (often neural networks) to train NLU and dialogue management models on annotated datasets.
- **Evaluation and Iteration**: Tests and refines the chatbot's performance based on real or simulated interactions to improve accuracy and user satisfaction.

### Integration and Deployment
- **Platform Integration**: Allows deployment on various platforms (e.g., web, apps, messaging platforms) to interact with users where they are.
- **Continuous Learning**: Supports ongoing updates and improvements based on user feedback and evolving needs.

# Setup Installation

>**Note**: Make sure you have installed the latest version of [Git](https://git-scm.com/downloads) and [Python](https://www.python.org/downloads/release/python-31011/) before proceeding. By default, `pip` comes pre-installed with Python. If missing, you can download it [here](https://bootstrap.pypa.io/get-pip.py) and open to install it automatically.

### Step 1. Confirm Installation

Open a new terminal and run the following commands:

  ```bash
    $ git --version
    $ python --version
    $ pip --version
  ```

### Step 2. Clone the Repository

Download and extract the project into a folder:

  ```bash
    $ cd Desktop
    $ git clone https://github.com/Dennis-Maigua/ai-medical-assistant.git
  ```

### Step 3. Open the Project

Open the inner folder of the project:

  ```bash
    $ cd ai-medical-assistant-main/ai-medical-assistant-main
  ```

### Step 4. Create a Virtual Environment

Build a venv inside the inner folder and activate it:

  ```bash
   $ python -m venv venv
   $ venv/Scripts/activate
  ```
   
### Step 5. Install Packages and Dependencies

Install `rasa` and other python `requirements` (in the venv):
  
  ```bash
   $ pip install rasa
   $ rasa --version 
   $ pip install -r requirements.txt
  ```

# Testing and Performance

### Step 6. (Optional) Train the Model

Train NLU and dialogue management models on annotated datasets for the chatbot:
  
  ```bash
   $ rasa train
  ```

### Step 7. Run the Chatbot

On the terminal, run the Actions:

  ```bash
    $ rasa run actions
  ```

Open another terminal, and run the Sanic server:

  ```bash
    $ rasa shell
  ```

# Contributing:

We welcome contributions from developers, IT experts, and technology enthusiasts. Feel free to fork the repository, make improvements, and submit pull requests. Happy coding!