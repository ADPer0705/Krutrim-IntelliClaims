# Project Title

## Overview
This project includes a chatbot for claims submission, a wireframe website, and an audio analysis service.

## Chatbot
The chatbot is built using Rasa and assists users with claims submission and general inquiries.

### Features:
- **Intents**: 
  - `greet`: Initiates a conversation.
  - `goodbye`: Ends the conversation.
  - `submit_claim`: Submits a claim.
- **Responses**: 
  - "Hey! How are you?"
  - "Your claim has been submitted successfully!"
- **Custom Actions**: Includes a custom action for submitting claims.
- **Testing**: Can be tested locally using Rasa commands.

### Installation:
To set up the environment and dependencies, ensure you have:
- Python 3.6 or higher
- Rasa framework

Install the required packages using:
```bash
pip install -r requirements.txt
```

### Configuration:
The chatbot's configuration is defined in:
- **config.yml**: Rasa NLU and Core components configuration.
- **domain.yml**: Defines intents, entities, responses, and actions.
- **endpoints.yml**: Configures endpoints for model storage and action handling.

## Frontend
The frontend is a wireframe website that starts on the `login.html` page.

### Features:
- **Login Page**: Users can log in with a username and password.
- **Form Validation**: Validates user inputs and provides feedback.
- **Navigation**: Links to create an account and reset passwords.

To see the wireframe, open the `login.html` page in a web browser. All pages are interlinked and included in the same directory, ensuring the website is navigable.

## Audio Analysis Service
The audio analysis service processes audio files to extract insights.

### Features:
- **Audio Processing**: Loads and processes audio files.
- **Transcription**: Transcribes audio using the Whisper model.
- **Sentiment Analysis**: Analyzes sentiment of the transcribed text.
- **Speech Detection**: Detects speech activity in audio.
- **Keyword Spotting**: Identifies specific keywords in the transcription.
- **Visualization**: Plots audio waveforms and sentiment analysis results.
- **Dashboard**: Generates a web dashboard to display results.
- **Report Generation**: Saves analysis results to a CSV file.

## Usage
To run the chatbot, navigate to the chatbot directory and use the following commands:
```bash
rasa run actions
```
Then, in another terminal:
```bash
rasa shell
```

To run the audio analysis service, execute the `sentiment_ananlysis.py` script.

## Conclusion
This project showcases a functional chatbot, a wireframe frontend, and an audio analysis service, all designed to assist users in managing claims and analyzing audio data.
