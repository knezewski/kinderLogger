import glob
from datetime import datetime


pattern = "audios//*.ogg"
ogg_files = glob.glob(pattern)


def extract_datetime_from_filename(filename):
    path, file_name = filename.split("/")
    parts = file_name.split("at")
    date_part = parts[0].split(" ")[0]  # Get the date part
    time_part = parts[1].split(".ogg")[
        0
    ]  # Get the time part, excluding the '.ogg' extension
    time_part = time_part.replace(".", ":")  # Replacing dots with colons
    datetime_str = f"{date_part} {time_part}"
    return datetime.strptime(datetime_str, "%Y-%m-%d %I:%M:%S %p")
