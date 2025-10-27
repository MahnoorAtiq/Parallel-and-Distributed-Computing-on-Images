import cv2
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

input_dir = r"E:\sem6\PDC\MidLabExam\data_set"
output_dir = r"E:\sem6\PDC\MidLabExam\output_parallel"

watermark_text = "© Mahnoor"

os.makedirs(output_dir, exist_ok=True)


def process_image(args):
    """Function to resize and watermark a single image."""
    input_path, output_path = args
    try:
        img = cv2.imread(input_path)
        if img is None:
            print(f"Skipping {input_path} (not an image)")
            return False

        resized_img = cv2.resize(img, (128, 128))

        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.4
        color = (255, 255, 255)
        thickness = 1
        text_size = cv2.getTextSize(watermark_text, font, font_scale, thickness)[0]
        text_x = resized_img.shape[1] - text_size[0] - 5
        text_y = resized_img.shape[0] - 5
        cv2.putText(resized_img, watermark_text, (text_x, text_y),
                    font, font_scale, color, thickness)

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        cv2.imwrite(output_path, resized_img)
        return True
    except Exception as e:
        print(f"Error processing {input_path}: {e}")
        return False


def collect_all_images():
    """Collect all image file paths with their output destinations."""
    tasks = []
    for root, _, files in os.walk(input_dir):
        relative_path = os.path.relpath(root, input_dir)
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_dir, relative_path, file)
                tasks.append((input_path, output_path))
    return tasks


def parallel_processing(worker_count):
    """Run processing in parallel using specified number of workers."""
    tasks = collect_all_images()
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=worker_count) as executor:
        futures = [executor.submit(process_image, task) for task in tasks]
        for _ in as_completed(futures):
            pass  

    end_time = time.time()
    total_time = end_time - start_time
    return total_time


if __name__ == "__main__":

    workers = [1, 2, 4, 8]
    results = {}

    print("Workers | Time (s) | Speedup")
    print("--------|----------|--------")

    base_time = None
    for w in workers:
        t = parallel_processing(w)
        if base_time is None:
            base_time = t
        speedup = base_time / t
        results[w] = (t, speedup)
        print(f"{w:<7d} | {t:8.2f} | {speedup:6.2f}x")
