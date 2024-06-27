# Meta Date Change Bot With Python
This Python script updates the access and modification dates of files in a directory based on the dates extracted from their filenames. This is especially useful when dates are embedded within filenames.

# Requirements
- Python 3.x

# Usage
- Create a directory named 'images' in your project folder and place files with date information in their filenames in this directory. For example: 'img_20240318.jpg'
- When the script runs, it will update the access and modification dates of all files in the images directory, and print an update message for each file.

# Explanation
- The os.listdir("images") command gets a list of all files in the images directory.
- The datestr variable extracts the date portion from the filename. In this example, it assumes the filename format is img_20240318.jpg.
- The datetime.datetime.strptime(datestr, "%Y-%m-%d") expression converts the date string into a datetime object.
- The os.utime(file_path, (new_access_time_epoch, new_modification_time_epoch)) command updates the access and modification times of the file.

# Notes
- The filenames must follow a specific format (e.g., img_YYYYMMDD.ext).
If the filenames have a different format, you may need to adjust the portion where the datestr variable is derived accordingly.