import sys

try:
    import cv2
    import numpy as np
except ImportError:
    print("ERROR: Missing required libraries.")
    print(
        "Open Command Prompt / Terminal and run: pip install opencv-python numpy"
    )
    input("\nPress Enter to exit...")
    sys.exit()

# 1080p Resolution
WIDTH = 1920
HEIGHT = 1080
FPS = 60  # 1 pixel changed per frame at 60fps = 60 pixels/sec

TOTAL_PIXELS = WIDTH * HEIGHT
TOTAL_FRAMES = TOTAL_PIXELS  # 1 pixel per frame
TOTAL_SECONDS = TOTAL_FRAMES / FPS

hours = int(TOTAL_SECONDS // 3600)
minutes = int((TOTAL_SECONDS % 3600) // 60)

OUTPUT_FILENAME = "all_pixels_white_1080p_60fps.mp4"

print(f"--- 1080p Video Generation Parameters ---")
print(f"Resolution: {WIDTH}x{HEIGHT} ({TOTAL_PIXELS:,} pixels)")
print(f"Framerate: {FPS} FPS")
print(
    f"Calculated Duration: {hours} hours, {minutes} minutes ({TOTAL_SECONDS:.1f} seconds)"
)
print(
    f"Generating '{OUTPUT_FILENAME}'... (This will take a few minutes to encode)"
)

# Use mp4v codec
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(OUTPUT_FILENAME, fourcc, FPS, (WIDTH, HEIGHT))

# Initialize canvas with a single black frame array
frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

# Render frames by updating 1 pixel in-place per frame
for frame_idx in range(TOTAL_FRAMES):
    y = frame_idx // WIDTH
    x = frame_idx % WIDTH
    frame[y, x] = [255, 255, 255]  # BGR white

    out.write(frame)

    # Print render progress every 10%
    if frame_idx % (TOTAL_FRAMES // 10) == 0 and frame_idx > 0:
        percent = (frame_idx / TOTAL_FRAMES) * 100
        print(f"Rendering progress: {percent:.0f}%...")

out.release()
print(f"\nSUCCESS! Video saved as '{OUTPUT_FILENAME}'.")
input("Press Enter to exit...")