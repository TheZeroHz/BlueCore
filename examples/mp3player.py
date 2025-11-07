import board
import audiomp3
import audiobusio
import time

# === Pin setup ===
# BCLK=GPIO5, LRC/WS=GPIO4, DOUT/DIN=GPIO6
i2s = audiobusio.I2SOut(
    bit_clock=board.GPIO5,    # BCLK
    word_select=board.GPIO4,  # LRC (Word Select)
    data=board.GPIO6          # DOUT (Data)
)

try:
    # === Load the MP3 file ===
    mp3_file = open("Ehssas.mp3", "rb")
    decoder = audiomp3.MP3Decoder(mp3_file)
    
    # Print audio file info
    print("=" * 40)
    print(f"Playing: Ehssas.mp3")
    print(f"Sample rate: {decoder.sample_rate} Hz")
    print(f"Bits per sample: {decoder.bits_per_sample}")
    print(f"Channels: {decoder.channel_count}")
    print("=" * 40)
    
    # === Play the audio ===
    i2s.play(decoder)
    
    # Wait for playback to finish
    while i2s.playing:
        time.sleep(0.1)
    
    print("Playback complete!")
    
except OSError as e:
    print(f"Error: Could not open file - {e}")
    print("Check that 'Ehssas.mp3' exists in the root directory")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    # Clean up
    i2s.deinit()
    if 'mp3_file' in locals():
        mp3_file.close()
    print("Audio system released.")
