from Utils import SCORES_FILE_NAME
import os
import fileinput
import sys

scores_file = SCORES_FILE_NAME


def validate_score_file():
    if os.path.isfile(scores_file) is True:
        print(scores_file)
        return True
    else:
        open(scores_file, "a").close()
        return False


def get_user_score(username):
    sc = open(scores_file, "r").readlines()
    user_exists = False
    for line in sc:
        spl_line = line.split("=")
        name = spl_line[0]
        score = spl_line[1]
        if name.strip().lower() == username.lower():
            user_exists = True
            break
    if user_exists is True:
        return int(score)
    else:
        return 0


def add_score(username, difficulty):
    score_to_add = (int(difficulty) * 3) + 5
    file_exists = validate_score_file()
    if file_exists is True:
        current_score = get_user_score(username=username)
    else:
        current_score = 0

    if current_score == 0:
        sc = open(scores_file, "a")
        line_to_write = username.lower() + "=" + str(score_to_add) + "\n"
        sc.write(line_to_write)
    else:
        for line in fileinput.input(scores_file, inplace=1):
            if username.lower() in line.lower():
                total_score = score_to_add+current_score
                line_to_write = username.lower() + "=" + str(total_score) + "\n"
                line = line.replace(line, line_to_write)
                sys.stdout.write(line)
            else:
                sys.stdout.write(line)



add_score("DviR", 6)
