# Eye-Blink-Detection
Real-Time Eye Blink Detection using MediaPipe and OpenCV

This project detects eye blinks in real time using a webcam feed. It uses MediaPipe Face Mesh to identify facial landmarks and determine whether both eyes are closed (i.e., a blink) by calculating the vertical distances between specific eye landmarks.

✨ Features
👁️ Detects eye closure by measuring vertical distances between eyelid landmarks.

🧠 Uses MediaPipe Face Mesh for facial landmark detection (478 landmarks).

📌 Supports up to two faces simultaneously.

⚡ Displays "Blinking" on screen when both eyes are closed.

📈 Shows FPS to monitor performance.

🟢 Draws facial mesh with optional landmark points.

🧠 How It Works
Uses specific upper and lower eyelid landmark pairs:

Right eye pairs: (386, 374), (385, 380), (387, 373)

Left eye pairs: (159, 145), (158, 153), (160, 144)

Computes Euclidean distance for each pair.

Calculates the average eye height.

If the average vertical distance is below a threshold (default = 5 pixels), the eye is considered closed.

If both eyes are closed, displays "Blinking" on screen.

 🚀 How to Run
Clone or download the repository.

Save the script as eye_blink_detection.py.

Run the script:

python eye_blink_detection.py

📊 Output
Live webcam feed with:

Green dots showing landmarks

Mesh overlay on face

"Blinking" text when both eyes are closed

FPS in top-left corner
