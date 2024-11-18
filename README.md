Here’s a README file for the second project:

---

# Speech-to-Text Generator 🎙️➡️📝

This Python application converts speech to text using the **Google Web Speech API**. It supports transcription from both pre-recorded audio files and real-time microphone input. 

## Features
- **Audio File Transcription**: Upload a `.wav` audio file and get its transcription.
- **Real-Time Speech Recognition**: Speak directly into your microphone for instant transcription.
- **Error Handling**: Provides clear messages for invalid input, unrecognized speech, and API request issues.

## Requirements
To run this program, you'll need:
- Python 3.x installed on your system.
- The following Python libraries:
  - `speech_recognition`
  - `pydub`
  
You can install the required libraries using:
```bash
pip install SpeechRecognition pydub
```

## How to Run
1. Clone or download this repository:
   ```bash
   git clone https://github.com/Abhilashchary/speech-to-text.git
   cd speech-to-text-generator
   ```
2. Run the script:
   ```bash
   python speech_to_text.py
   ```

3. Follow the on-screen prompts:
   - Choose to transcribe from an audio file or use your microphone.
   - For audio file transcription, provide the file path to a `.wav` file.

## How It Works
1. **Audio File Transcription**:
   - The script uses the `speech_recognition` library to process `.wav` audio files.
   - Converts speech in the audio file into text using the Google Web Speech API.
   
2. **Real-Time Microphone Transcription**:
   - Captures audio using your device's microphone.
   - Processes the input in real-time to produce a text transcription.

## Audio Format
- For best results, ensure your audio files are in `.wav` format. If your file is in another format (e.g., `.mp3`), use tools like [Audacity](https://www.audacityteam.org/) or Python's `pydub` to convert the file.

## Error Handling
- If the script cannot understand the speech, it will notify you.
- API errors and missing file issues are handled gracefully with descriptive error messages.

## File Details
- `speech_to_text.py`: The main script containing functionality for both file-based and microphone-based speech recognition.

## Contribution
Feel free to fork the repository and submit pull requests for any improvements, such as adding support for additional audio formats or enhancing the user interface.
