# Chatbot Documentation

## Introduction
This chatbot is built using Rasa and is designed to assist users with claims submission and general inquiries.

## Installation
To set up the environment and dependencies, ensure you have the following installed:
- Python 3.6 or higher
- Rasa framework

You can install the required packages using:
```bash
pip install -r requirements.txt
```

## Configuration
The chatbot's configuration is defined in the following files:

- **config.yml**: Contains the configuration for Rasa NLU and Core components. You may customize the pipeline and policies as needed.
- **domain.yml**: Defines the intents, entities, responses, and actions for the chatbot.
- **endpoints.yml**: Configures the endpoints for model storage, action handling, and tracker stores. Ensure to uncomment and customize these settings based on your deployment needs.

## Usage
To interact with the chatbot, you can use the following intents:
- `greet`: Initiates a conversation.
- `goodbye`: Ends the conversation.
- `submit_claim`: Submits a claim.

Responses include:
- "Hey! How are you?"
- "Your claim has been submitted successfully!"

## Custom Actions
The chatbot includes a custom action for submitting claims, defined in `actions/actions.py`. Ensure that the action server is running to handle these requests.

## Testing
You can test the chatbot locally by running the following command:
```bash
rasa run actions
```
Then, in another terminal, run:
```bash
rasa shell
```
This will allow you to interact with the chatbot in the command line.
