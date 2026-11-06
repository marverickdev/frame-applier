import os
from PIL import Image, ImageOps
from pillow_heif import register_heif_opener

# Register HEIF support
register_heif_opener()

def apply_frame_batch(input_folder, output_folder, overlay_path):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        # Load the frame/overlay and grab its exact dimensions
        overlay = Image.open(overlay_path).convert("RGBA")
        frame_size = overlay.size 
    except Exception as e:
        print(f"Error loading overlay: {e}")
        return

    valid_extensions = ('.png', '.jpg', '.jpeg', '.heic', '.heif')

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(valid_extensions):
            base_image_path = os.path.join(input_folder, filename)
            
            # Swap the extension to .png if the original is a HEIC
            name_without_ext = os.path.splitext(filename)[0]
            if filename.lower().endswith(('.heic', '.heif')):
                output_filename = f"{name_without_ext}.png"
            else:
                output_filename = filename
                
            output_image_path = os.path.join(output_folder, output_filename)

            try:
                base_image = Image.open(base_image_path).convert("RGBA")

                # Core change: Resize and crop the photo to match the frame perfectly
                fitted_image = ImageOps.fit(base_image, frame_size, method=Image.Resampling.LANCZOS)

                # Paste the frame onto the newly sized photo
                fitted_image.alpha_composite(overlay)

                # Convert back to RGB only if saving as a JPG
                if output_filename.lower().endswith(('.jpg', '.jpeg')):
                    final_image = fitted_image.convert("RGB")
                else:
                    final_image = fitted_image

                final_image.save(output_image_path)
                print(f"Successfully framed: {filename} -> saved as {output_filename}")

            except Exception as e:
                print(f"Error processing {filename}: {e}")

# --- Configuration ---
INPUT_DIR = "input_images"
OUTPUT_DIR = "output_images"
OVERLAY_FILE = "overlay.png"

print("Starting batch framing process...")
apply_frame_batch(INPUT_DIR, OUTPUT_DIR, OVERLAY_FILE)
print("Finished!")