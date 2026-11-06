# Frame Applier

A lightweight Python batch utility that resizes, center-crops, and overlays a custom transparent frame onto a folder of images. It supports standard formats (`.png`, `.jpg`, `.jpeg`) as well as Apple's `.heic` / `.heif` formats out of the box.

---

## Features

- **Batch Processing:** Automatically processes all supported images in the `input_images/` folder.
- **Smart Fit & Crop:** Uses high-quality Lanczos resampling (`ImageOps.fit`) to scale and center-crop photos to match the exact dimensions of your frame overlay without stretching or distorting aspect ratios.
- **HEIC / HEIF Support:** Seamlessly reads iPhone/Apple `.heic` and `.heif` photos and exports them as `.png` files.
- **Alpha Compositing:** Preserves transparency in your `overlay.png` frame and properly converts back to RGB when saving `.jpg` / `.jpeg` outputs.

---

## Project Structure

```text
frame-applier/
├── input_images/      # Place the photos you want to frame here
├── output_images/     # Framed images will be generated and saved here
├── main.py            # Main batch processing script
├── overlay.png        # The transparent frame overlay image
└── requirements.txt   # Python package dependencies
```

---

## Prerequisites

- **Python 3.10+** installed on your system.
- **Git** (optional, for cloning the repository).

### Installing Python (if not already installed)

- **Windows:** Download the installer from [python.org](https://www.python.org/downloads/windows/) (make sure to check **"Add Python to PATH"** during setup) or install via Winget:
  ```powershell
  winget install Python.Python.3.12
  ```
- **macOS:** Install via [Homebrew](https://brew.sh/) or download from [python.org](https://www.python.org/downloads/macos/):
  ```bash
  brew install python
  ```
- **Linux (Ubuntu/Debian):**
  ```bash
  sudo apt update && sudo apt install python3 python3-venv python3-pip libheif-dev -y
  ```
  *(For Fedora/RHEL: `sudo dnf install python3 python3-pip libheif-devel`)*

---

## Setup & Installation

### 1. Clone or Download the Repository

```bash
git clone https://github.com/marverickdev/frame-applier.git
cd frame-applier
```

### 2. Create a Virtual Environment & Install Dependencies

Select the instructions for your operating system below:

#### Windows (Command Prompt or PowerShell)

```powershell
# Create a virtual environment
python -m venv venv

# Activate the virtual environment (PowerShell)
.\venv\Scripts\Activate.ps1
# Or if using Command Prompt (cmd.exe):
# venv\Scripts\activate.bat

# Install dependencies
pip install -r requirements.txt
```

> **Note for Windows PowerShell users:** If you encounter an execution policy error when activating the virtual environment, run:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

#### macOS

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### Linux

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## How to Use

1. **Prepare Your Frame Overlay:**
   Place your transparent frame image in the root project directory and name it `overlay.png` (or replace the existing `overlay.png`).
   - *Tip:* Make sure `overlay.png` is a PNG with transparency (alpha channel) where the photo should show through. The output resolution of all framed photos will match the exact pixel dimensions of `overlay.png`.

2. **Add Input Photos:**
   Drop all the images you want to frame into the `input_images/` folder.
   - **Supported input formats:** `.png`, `.jpg`, `.jpeg`, `.heic`, `.heif` (case-insensitive).

3. **Run the Program:**
   With your virtual environment activated, run:

   **Windows:**
   ```powershell
   python main.py
   ```

   **macOS / Linux:**
   ```bash
   python3 main.py
   ```

4. **Collect Your Framed Images:**
   Once you see `Finished!` in the terminal, open the `output_images/` folder to find your processed images.
   - `.png`, `.jpg`, and `.jpeg` files keep their original file extensions.
   - `.heic` and `.heif` files are automatically converted and saved as `.png` files.

---

## Customization

If you want to use different folder names or a different overlay filename, you can edit the configuration constants at the bottom of `main.py`:

```python
# --- Configuration ---
INPUT_DIR = "input_images"
OUTPUT_DIR = "output_images"
OVERLAY_FILE = "overlay.png"
```

---

## Troubleshooting

- **`Error loading overlay: [Errno 2] No such file or directory: 'overlay.png'`**
  Ensure that `overlay.png` exists in the project root folder and that you are running the script from inside the `frame-applier` directory.
- **`ModuleNotFoundError: No module named 'PIL'` or `'pillow_heif'`**
  Make sure your virtual environment (`venv`) is activated before running `python main.py`, and that `pip install -r requirements.txt` completed without errors.
- **No images are being processed**
  Verify that your photos are placed directly inside `input_images/` (not nested in subfolders) and have one of the supported extensions (`.png`, `.jpg`, `.jpeg`, `.heic`, `.heif`).
- **Deactivating the Virtual Environment**
  When you are done using the tool, you can exit the virtual environment at any time by running:
  ```bash
  deactivate
  ```
