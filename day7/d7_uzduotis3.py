import os
import datetime

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
new_directory_path = os.path.join(desktop_path, "IdomusNaujas")

os.makedirs(new_directory_path, exist_ok=True)

now = datetime.datetime.now()
filename = now.strftime("%y-%M-%d_%H:%M:S.txt")
file_path = os.path.join(new_directory_path, filename)

with open(file_path, "w") as file:
    file.write(str(now))

file_stats = os.stat(file_path)
created_timestamp = file_stats.st_ctime
file_size = file_stats.st_size

created_datetime = datetime.datetime.fromtimestamp(created_timestamp)
print(f"Sukūrimo data: {created_datetime}")
print(f"Dydis baitais: {file_size}")