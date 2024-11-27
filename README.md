# Instarche
# Instagram Posts Downloader

A Python tool for downloading posts from a public Instagram profile using Instaloader. The application provides a simple user interface to input the target profile and download posts.

## Features
- **User-Friendly Interface**: A GUI allows users to download posts by entering the target username.
- **Automatic Downloads**: Posts from a public profile are saved directly to the corresponding folder.
- **Cleanup Functionality**: Removes unnecessary files after downloading and optionally allows deletion of posts based on a specific date.

## Usage
1. Launch the application and enter the username of the public Instagram profile.
2. Click "Start Download" to download the posts.
3. After the downloads are complete, run the cleanup scripts to remove unnecessary files or older posts.

## Requirements
- Python 3.x
- Instaloader library
- Tkinter for the graphical user interface
```bash
pip install instaloader
``

## Cleanup Scripts
### `clean_up.py`
This script removes all unnecessary files generated during the download process (e.g., metadata files).

### `clean_up_date.py` (optional)
Deletes posts downloaded before a specified date. This can be used to manage and remove older posts from the folder.

## Notes
- This tool **only works for public Instagram profiles**.
- The script **does not support private profiles** or profiles requiring login access.

## License
This project is licensed under the MIT License. Ensure that you comply with Instagram's Terms of Service when using this tool.
