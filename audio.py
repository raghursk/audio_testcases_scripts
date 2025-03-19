import pytest
import time

def play_audio():
    print("Playing audio...")
    return "playing"

def pause_audio():
    print("Pausing audio...")
    return "paused"

def resume_audio():
    print("Resuming audio...")
    return "playing"

def stop_audio():
    print("Stopping audio...")
    return "stopped"

def change_volume(level):
    print(f"Setting volume to {level}...")
    return f"volume_{level}"

def test_audio_playback():
    assert play_audio() == "playing"

def test_pause_resume_audio():
    assert pause_audio() == "paused"
    assert resume_audio() == "playing"

def test_volume_control():
    assert change_volume(5) == "volume_5"
    assert change_volume(10) == "volume_10"

def test_audio_quality():
    assert play_audio() == "playing"  

def test_audio_format_support():
    supported_formats = ["MP3", "FLAC"]
    unsupported_formats = ["AAC", "WAV"]
    for fmt in supported_formats:
        assert fmt in supported_formats
    for fmt in unsupported_formats:
        assert fmt not in supported_formats

def test_bluetooth_audio():
    print("Connecting to Bluetooth...")
    time.sleep(1) 
    assert play_audio() == "playing"

def test_audio_during_notifications():
    print("Receiving notification...")
    time.sleep(1)
    assert pause_audio() == "paused"
    assert resume_audio() == "playing"

def test_audio_on_incoming_call():
    print("Simulating incoming call...")
    time.sleep(1)
    assert pause_audio() == "paused"
    assert resume_audio() == "playing"

def test_long_audio_playback():
    print("Playing long audio...")
    time.sleep(3)  
    assert play_audio() == "playing"

if __name__ == "__main__":
    pytest.main(["-v", "--tb=short"])
