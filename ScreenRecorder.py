import cv2
import numpy as np
import pyautogui
import time
import os


def RecordVideo():
    record_duration = 10
    fourcc = cv2.VideoWriter_fourcc(*"XVID") 
    fps = 20.0
    screen_size = pyautogui.size() 

    #Checking if Folder Already Exist
    output_folder = "recorded_videos"
    os.makedirs(output_folder, exist_ok=True)

    #finding the folder size
    temp=FolderSize()+1 
    output_file = os.path.join(output_folder, f"output_{temp}.avi")
    out = cv2.VideoWriter(output_file, fourcc, fps, screen_size)

    print("Recording...")

    start_time = time.time()
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = cv2.resize(frame, screen_size)
        out.write(frame)  
        cv2.imshow("Recording", frame)
        if time.time() - start_time > record_duration:
            break
        if cv2.waitKey(1) == ord('q'):
            break
    out.release()
    cv2.destroyAllWindows()
    print("Recording finished.")



def FolderSize():
    num_files = len([f for f in os.listdir("recorded_videos") if os.path.isfile(os.path.join("recorded_videos", f))])
    return num_files