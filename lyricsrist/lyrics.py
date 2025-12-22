import time
import sys
import pyttsx3

def typing_print_line(line: str, char_delay: float = 0.05):
    """Prints a single line with a typing effect."""
    for ch in line:
        print(ch, end="", flush=True)
        time.sleep(char_delay)
    print()  # move to next line

def speak_lyrics_ai(lyrics, rate: int = 150, volume: float = 1.0):
    """
    Uses text-to-speech to read the lyrics.
    Works offline with pyttsx3.
    """
    engine = pyttsx3.init()

    # Adjust speaking rate (words per minute)
    engine.setProperty("rate", rate)

    # Adjust volume (0.0 to 1.0)
    engine.setProperty("volume", volume)

    # (Optional) Try to pick a different voice if available
    voices = engine.getProperty("voices")
    if voices:
        # Just picking the first voice; you can experiment with indices
        engine.setProperty("voice", voices[0].id)

    # Speak each line with a tiny pause between them
    for line in lyrics:
        engine.say(line)
        engine.runAndWait()
        time.sleep(0.2)  # slight pause between lines

def print_lyrics_with_effect_and_voice():
    """
    Prints the song title and lyrics with a typing effect,
    and also plays an AI-like voice for the lyrics.
    """
    # --- Song Title ---
    song_title = "🎧 Konte Chooputho"
    print(song_title)
    print("-" * len(song_title))
    time.sleep(1.0)  # Short pause after printing the title

    # --- Lyrics ---
    lyrics = [
        "Kallu raase nee kallu raase",
        "Oka chinni kavita premenemoo",
        "Adi chadivinappudu",
        "Na pedavi chappudu",
        "Tolipaate naalo palikinadii,"
    ]

    # You can tweak this typing speed
    CHAR_DELAY = 0.05

    # Initial delay before lyrics start
    time.sleep(1.5)

    # 1) Print lyrics with typing effect
    for line in lyrics:
        typing_print_line(line, CHAR_DELAY)
        # No extra delay between lines – as per your requirement

    # 2) AI Voice for the lyrics
    print("\n🎤 Playing AI voice for the lyrics...")
    speak_lyrics_ai(lyrics, rate=155, volume=1.0)

if __name__ == "__main__":
    print_lyrics_with_effect_and_voice()
for i, v in enumerate(voices):
    print(i, v.name)


