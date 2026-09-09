import sys

try:
    import cv2
    import numpy as np
except ImportError:
    print("ERROR: Missing required libraries.")
    print("Open Command Prompt / Terminal and run: pip install opencv-python numpy")
    input("\nPress Enter to exit...")
    sys.exit()

# 144p resolution (16:9 widescreen)
WIDTH = 256
HEIGHT = 144
FPS = 30

TOTAL_PIXELS = WIDTH * HEIGHT
# 1 pixel every 0.1s = 10 pixels per second
TOTAL_SECONDS = TOTAL_PIXELS * 0.1  # 3,686.4 seconds (~61.4 minutes)
TOTAL_FRAMES = int(TOTAL_SECONDS * FPS)

OUTPUT_FILENAME = "all_pixels_white_144p.mp4"

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(OUTPUT_FILENAME, fourcc, FPS, (WIDTH, HEIGHT))

print(f"Total Pixels to turn white: {TOTAL_PIXELS:,}")
print(f"Calculated Duration: {TOTAL_SECONDS / 60:.1f} minutes")
print(f"Generating '{OUTPUT_FILENAME}'... (This will take a couple of minutes to render)")

# Initialize black frame
frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
pixels_turned_white = 0

for frame_idx in range(TOTAL_FRAMES):
    current_time_sec = frame_idx / FPS
    target_white_pixels = min(int(current_time_sec / 0.1) + 1, TOTAL_PIXELS)

    # Turn newly qualified pixels white sequentially
    while pixels_turned_white < target_white_pixels:
        y = pixels_turned_white // WIDTH
        x = pixels_turned_white % WIDTH
        frame[y, x] = [255, 255, 255]
        pixels_turned_white += 1

    out.write(frame)

    # Print render progress every 10%
    if frame_idx % max(1, (TOTAL_FRAMES // 10)) == 0:
        percent = (frame_idx / TOTAL_FRAMES) * 100
        print(f"Rendering: {percent:.0f}% complete...")

out.release()
print(f"\nSUCCESS! Fully white video generated: '{OUTPUT_FILENAME}'")
input("Press Enter to exit...")