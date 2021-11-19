import os

SCORES_FILE_NAME = "db/Scores.txt"
BAD_RETURN_CODE = 6


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
