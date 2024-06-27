import os
import datetime

for i in os.listdir("images"):
    # We select the date from the file name or "2024-03-18"
    datestr = f"{i[4:8]}-{i[8:10]}-{i[10:12]}"
    new_access_time = datetime.datetime.strptime(datestr, "%Y-%m-%d")
    new_modification_time = datetime.datetime.strptime(datestr, "%Y-%m-%d")

    new_access_time_epoch = new_access_time.timestamp()
    new_modification_time_epoch = new_modification_time.timestamp()
    # Let's specify the file path
    file_path = f"images/{i}"

    # Let's change file dates using the os.utime function
    os.utime(file_path, (new_access_time_epoch, new_modification_time_epoch))

    print(f"{file_path} file modification dates have been updated.")
