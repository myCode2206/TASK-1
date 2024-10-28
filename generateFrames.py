import os
import subprocess

def generate_frames(video_file_name):
    print("Frame extraction started.")
    video_folder = 'recorded_videos'
    output_folder = 'frames'

    # Construct the full path to the video file
    video_file_path = os.path.join(video_folder, video_file_name)

    # Check if the specified video file exists
    if not os.path.isfile(video_file_path):
        print(f"Error: {video_file_name} does not exist in {video_folder}.")
        return

    # Get the base name of the video file without the extension
    base_name = os.path.splitext(video_file_name)[0]
    frames_folder = os.path.join(output_folder, base_name)
    os.makedirs(frames_folder, exist_ok=True)

    # Construct the ffmpeg command
    command = [
        'ffmpeg',
        '-i', video_file_path,  # Input video file
        '-vf', 'fps=1',  # Extract 1 frame per second
        os.path.join(frames_folder, 'frame_%04d.png')  # Output frame format
    ]

    # Execute the command
    subprocess.run(command)

    print("Frame extraction complete.")
