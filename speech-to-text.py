import speech_recognition as sr
from pydub import AudioSegment

# Initialize the recognizer
recognizer = sr.Recognizer()

def recognize_speech_from_audio(audio_file_path):
    """
    Convert speech from an audio file to text using Google Web Speech API.
    """
    try:
        # Load the audio file (ensure it's in .wav format for best results)
        with sr.AudioFile(audio_file_path) as source:
            audio_data = recognizer.record(source)  # Read the entire audio file
            print("Transcribing audio file...")

            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            print("Transcription Result:", text)
            return text

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except FileNotFoundError:
        print("Audio file not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return None


def recognize_speech_from_microphone():
    """
    Convert speech from the microphone to text in real-time using Google Web Speech API.
    """
    try:
        # Use the microphone as the source for input
        with sr.Microphone() as source:
            print("Please speak into the microphone...")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
            audio_data = recognizer.listen(source)
            print("Transcribing your speech...")

            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            print("Transcription Result:", text)
            return text

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return None


def main():
    """
    Main function to choose between file-based and real-time microphone transcription.
    """
    print("Welcome to the Speech-to-Text Generator!")
    print("Choose an option:")
    print("1. Transcribe from an audio file")
    print("2. Transcribe in real-time from microphone")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        audio_file_path = input("Enter the path to your audio file (.wav): ")
        recognize_speech_from_audio(audio_file_path)
    elif choice == '2':
        recognize_speech_from_microphone()
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Run the main function
if __name__ == "__main__":
    main()
