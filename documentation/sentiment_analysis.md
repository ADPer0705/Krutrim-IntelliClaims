# Sentiment Analysis for Audio Files

## Key Features
### *Audio Loading and Processing*
- The customer’s call is recorded using a standard telephony system and saved as an audio file.
- The load_audio function uses the Librosa library to load audio files while preserving their original sampling rate. It also calculates the duration of the audio, ensuring compatibility with downstream processing.
- The recorded file is processed to ensure it is in a format suitable for analysis, such as mono channel and resampled to 16 kHz for uniformity.

### *Automatic Speech Recognition (ASR)*
- Using OpenAI's Whisper model, the transcribe_audio function transcribes audio recordings into text.
- This transcription forms the foundation for further analysis, such as sentiment analysis and keyword spotting.

### *Sentiment Analysis*
- The transcription is processed by NLTK's SentimentIntensityAnalyzer to assess customer sentiment. 
- This step provides a polarity score (positive, neutral, negative, and compound), offering insights into customer satisfaction and emotional tone during the call.The transcription is analyzed for sentiment. 
- For example, if the customer says, “I am frustrated with the delay,” the system detects a negative sentiment.

### *Speech Activity Detection*
- The WebRTC Voice Activity Detection (VAD) module identifies segments of speech in the audio. 
- This ensures that only relevant speech segments are processed, filtering out silence or background noise.

### *Keyword Spotting*
- The system checks for the presence of predefined keywords (e.g., "alert," "payment," "password") in the transcription. T
- his feature identifies critical phrases that may require further attention, such as escalations or security concerns.
- Keywords like “refund” or “password” are identified in the transcription, signaling specific customer concerns.

### *Visualization*
Two types of visualizations are generated:

1. Audio Waveform:
- Displays the amplitude of the audio signal over time, providing a visual representation of the call's dynamics.
2. Sentiment Bar Chart: 
- Illustrates the sentiment scores, making it easier to interpret the emotional tone of the conversation.

### *Dashboard Interface*
- A user-friendly dashboard, built with Dash, presents the transcription and sentiment analysis results. The dashboard enables customer service managers to quickly review key insights from calls.

### *Report Generation*
The system saves a detailed report in CSV format, including transcription, sentiment scores, detected keywords, and audio duration. This report supports documentation and further analysis.

---

# Technical Stack
Libraries:
- Librosa: Audio processing.
- Whisper: Automatic Speech Recognition.
- NLTK: Sentiment analysis.
- WebRTC VAD: Speech activity detection.
- Dash: Dashboard creation.
- Matplotlib: Data visualization.
- Pandas: Data handling and report generation.
