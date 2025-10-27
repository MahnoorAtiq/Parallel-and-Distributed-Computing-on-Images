import os
import time
from multiprocessing import Process, Manager
from PIL import Image, ImageDraw, ImageFont

input_dir = r"E:\sem6\PDC\MidLabExam\data_set"
output_dir = r"E:\sem6\PDC\MidLabExam\output_distributed"
watermark_text = "© Mahnoor"

os.makedirs(output_dir, exist_ok=True)

def add_watermark(image_path, output_path, watermark_text):

    img = Image.open(image_path).convert("RGBA")
    img = img.resize((128, 128))
 
    txt = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt)
    font_size = 12
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    draw.text((5, 5), watermark_text, fill=(255, 255, 255, 128), font=font)
    
    watermarked = Image.alpha_composite(img, txt)
    watermarked = watermarked.convert("RGB")
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    watermarked.save(output_path)

def node_process(node_id, image_paths, result_dict):

    start_time = time.time()
    for img_path in image_paths:
        class_folder = os.path.relpath(os.path.dirname(img_path), input_dir)
        out_folder = os.path.join(output_dir, class_folder)
        os.makedirs(out_folder, exist_ok=True)
        out_path = os.path.join(out_folder, os.path.basename(img_path))
        add_watermark(img_path, out_path, watermark_text)
    end_time = time.time()
    result_dict[node_id] = end_time - start_time
    print(f"Node {node_id} processed {len(image_paths)} images in {result_dict[node_id]:.2f}s")

if __name__ == "__main__":

    all_images = []
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                all_images.append(os.path.join(root, file))

    mid = len(all_images) // 2
    node1_images = all_images[:mid]
    node2_images = all_images[mid:]

    manager = Manager()
    result_dict = manager.dict()

    p1 = Process(target=node_process, args=(1, node1_images, result_dict))
    p2 = Process(target=node_process, args=(2, node2_images, result_dict))

    total_start = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    total_end = time.time()

    total_distributed_time = total_end - total_start
    sequential_time_estimate = max(result_dict.values())  
    efficiency = sequential_time_estimate / total_distributed_time if total_distributed_time > 0 else 0

    print(f"Total distributed time: {total_distributed_time:.2f}s")
    print(f"Efficiency: {efficiency:.2f}x over sequential")
