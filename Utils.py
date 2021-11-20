import os

SCORES_FILE_NAME = "db/Scores.txt"
BAD_RETURN_CODE = 6


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def my_sort(line):
    line_fields = line.strip().split('=')
    amount = float(line_fields[1])
    return amount


def sort_file_scores():
    fp = open(SCORES_FILE_NAME)
    contents = fp.readlines()
    contents.sort(key=my_sort, reverse=True)
    fp.close()
    with open(SCORES_FILE_NAME, "w") as new:
        for line in contents:
            new.write(line)
    new.close()
