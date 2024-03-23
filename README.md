Sure, I'll update the README accordingly:

---

# Social Distancing Detector

## Description
This project implements a real-time Social Distancing Detector that can identify the distance between individuals in a crowd. It utilizes the YOLOv8 model for person detection and scipy for distance calculation. The detector aims to assist in ensuring adherence to social distancing guidelines in public spaces.

## Features
- Real-time detection of individuals in a crowd using YOLOv8.
- Calculation of distances between detected individuals using scipy.
- Visualization of social distancing violations.
- Customizable settings for detection thresholds and visualization options.

## Technologies Used
- Python
- YOLOv8
- OpenCV
- SciPy

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/your_username/social-distancing-detector.git
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the main script with the input video file:
   ```
   python main.py -i input_video.mp4
   ```
   Replace `path_to_input_video.mp4` with the path to your input video file.
2. Adjust settings as needed (e.g., detection threshold, visualization options).
3. View the output displaying individuals and social distancing violations.

## Final Video
![Social Distancing Detector Output](output_video.mp4)
