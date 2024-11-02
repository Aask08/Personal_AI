import pyautogui
from core_utils import speak
import time

def play_pause():
    """Toggle play/pause on YouTube video."""
    pyautogui.press("k")  # 'k' is the shortcut for play/pause on YouTube
    speak("Playback toggled.")

def forward():
    """Skip forward 10 seconds on YouTube video."""
    pyautogui.press("l")  # 'l' skips forward by 10 seconds
    speak("Skipped forward.")

def backward():
    """Skip backward 10 seconds on YouTube video."""
    pyautogui.press("j")  # 'j' skips backward by 10 seconds
    speak("Skipped backward.")

def set_volume(level):
    """Set volume to a specific level (0 to 100)."""
    if level < 0 or level > 100:
        speak("Volume level should be between 0 and 100.")
        return

    pyautogui.press("m")  # Mute the video first to start fresh
    time.sleep(0.1)

    # Raise volume to 100, then decrease to desired level
    for _ in range(50):  # Pressing 'up' key repeatedly to ensure max volume
        pyautogui.press("up")
    for _ in range(50 - level):
        pyautogui.press("down")
    speak(f"Volume set to {level} percent.")
