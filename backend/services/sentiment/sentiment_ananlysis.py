import librosa
import whisper
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import numpy as np
from dash import Dash, html, dcc
import pandas as pd
import webrtcvad
import wave
import nltk

# Download vader_lexicon if not already downloaded
nltk.download('vader_lexicon')

# Load and process audio file
def load_audio(audio_path):
    audio, sr = librosa.load(audio_path, sr=None)
    duration = librosa.get_duration(y=audio, sr=sr)
    return audio, sr, duration

# Transcribe audio using Whisper
def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]

# Perform sentiment analysis
def analyze_sentiment(transcription):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(transcription)


# Detect speech activity using WebRTC VAD (using librosa)
def detect_speech(audio_path):
    audio, sr = librosa.load(audio_path, sr=16000)  # Resample to 16000 Hz
    audio = librosa.to_mono(audio)  # Convert to mono
    vad = webrtcvad.Vad()
    vad.set_mode(3)
    frame_duration = 30  # milliseconds
    frame_size = int(sr * frame_duration / 1000)  # Duration in samples per frame
    num_frames = len(audio) // frame_size  # Calculate number of frames
    segments = [audio[i*frame_size:(i+1)*frame_size] for i in range(num_frames)]
    
    # Convert each segment to raw 16-bit PCM and check for speech
    results = []
    for segment in segments:
        # Ensure the segment is not empty and has enough samples for processing
        if len(segment) == frame_size:
            pcm_segment = (segment * 32767).astype(np.int16).tobytes()
            results.append(vad.is_speech(pcm_segment, sr))
        else:
            results.append(False)  # Mark as non-speech if the segment is too short
    return sum(results), len(results)


# Keyword spotting
def keyword_spotting(transcription, keywords):
    return [word for word in keywords if word in transcription.lower()]

# Visualization
def plot_audio_waveform(audio, sr):
    plt.figure(figsize=(10, 4))
    plt.plot(np.linspace(0, len(audio) / sr, len(audio)), audio)
    plt.title("Audio Waveform")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.show()

def plot_sentiment(sentiment):
    plt.bar(sentiment.keys(), sentiment.values(), color="skyblue")
    plt.title("Sentiment Analysis")
    plt.xlabel("Sentiment Type")
    plt.ylabel("Score")
    plt.show()

# Generate dashboard
def create_dashboard(transcription, sentiment):
    app = Dash(__name__)
    app.layout = html.Div([
        html.H1("Voice Call Analysis"),
        dcc.Markdown(f"**Transcription:** {transcription}"),
        dcc.Graph(
            figure={
                "data": [{"x": list(sentiment.keys()), "y": list(sentiment.values()), "type": "bar"}],
                "layout": {"title": "Sentiment Analysis"}
            }
        )
    ])
    return app

# Save report
def save_report(transcription, sentiment, keywords, duration, output_path):
    report = {
        "Transcription": transcription,
        "Sentiment": sentiment,
        "Keywords Detected": keywords,
        "Audio Duration": duration
    }
    df = pd.DataFrame([report])
    df.to_csv(output_path, index=False)
    print(f"Report saved as {output_path}")

# Main function
def main():
    audio_path = "InboundSampleRecording.wav"
    keywords = ["alert", "payment", "password", "shipping address", "discount", " subscription"]

    print("Loading audio...")
    audio, sr, duration = load_audio(audio_path)

    print("Transcribing audio...")
    transcription = transcribe_audio(audio_path)

    print("Analyzing sentiment...")
    sentiment = analyze_sentiment(transcription)

    print("Detecting speech activity...")
    speech_detected, total_segments = detect_speech(audio_path)
    print(f"Speech detected in {speech_detected}/{total_segments} segments.")

    print("Performing keyword spotting...")
    detected_keywords = keyword_spotting(transcription, keywords)
    print(f"Detected Keywords: {detected_keywords}")

    print("Visualizing results...")
    plot_audio_waveform(audio, sr)
    plot_sentiment(sentiment)

    print("Saving report...")
    save_report(transcription, sentiment, detected_keywords, duration, "voice_call_analysis_report.csv")

    print("Launching dashboard...")
    app = create_dashboard(transcription, sentiment)
    app.run_server(debug=True)

if __name__ == "__main__":
    main()
