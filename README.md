# File Organizer CLI

A lightweight Python command-line utility that automatically scans a directory and organizes files into category folders based on their extensions.

## Problem Solved
Download directories and desktop folders frequently accumulate loose files with mixed extensions. Manually creating folders and moving each item is repetitive and inefficient. This script scans the target directory and relocates recognized file formats into organized folders automatically.

## Supported Categories
- **Images:** `.jpg`, `.jpeg`, `.png`
- **Documents:** `.pdf`, `.docx`, `.txt`, `.xlsx`
- **Videos:** `.mp4`, `.mov`, `.avi`
- **Archives:** `.zip`, `.rar`, `.tar`

## How It Works
1. Prompts for a folder path, stripping accidental quotes or trailing whitespace.
2. Validates that the directory exists before executing operations.
3. Scans entries via `os.listdir()` and processes files using `os.path.isfile()`.
4. Extracts extensions using `os.path.splitext()`.
5. Matches extensions against predefined category mappings.
6. Dynamically creates destination folders with `os.makedirs(..., exist_ok=True)`.
7. Relocates files using `shutil.move()`.
8. Prints a summary of moved versus skipped files.

## Requirements
- Python 3.8+
- Uses standard library modules only (`os`, `shutil`, `sys`) — no third-party installations required.

## Usage
1. Clone the repository:
   ```bash
   git clone [https://github.com/](https://github.com/)<your-username>/file-organizer-cli.git
   cd file-organizer-cli
   Run the script:

python organizer.py
