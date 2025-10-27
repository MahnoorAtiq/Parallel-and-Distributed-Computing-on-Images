import cv2
import os
import time


input_dir = r"E:\sem6\PDC\MidLabExam\data_set"
output_dir = r"E:\sem6\PDC\MidLabExam\output_seq"

watermark_text = "Specie?"

start_time = time.time()

os.makedirs(output_dir, exist_ok=True)

for root, dirs, files in os.walk(input_dir):
    
    relative_path = os.path.relpath(root, input_dir)
    output_folder = os.path.join(output_dir, relative_path)
    os.makedirs(output_folder, exist_ok=True)
    
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            input_path = os.path.join(root, file)
            output_path = os.path.join(output_folder, file)

            img = cv2.imread(input_path)

            if img is None:
                print(f"Skipping {input_path} (not an image)")
                continue

            resized_img = cv2.resize(img, (128, 128))

            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.4
            color = (255, 255, 255)
            thickness = 1
            text_size = cv2.getTextSize(watermark_text, font, font_scale, thickness)[0]
            text_x = resized_img.shape[1] - text_size[0] - 5
            text_y = resized_img.shape[0] - 5
            cv2.putText(resized_img, watermark_text, (text_x, text_y), font, font_scale, color, thickness)

            cv2.imwrite(output_path, resized_img)

end_time = time.time()
execution_time = end_time - start_time

print(f"Sequential Processing Time: {execution_time:.2f} seconds")
