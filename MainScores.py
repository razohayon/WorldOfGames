from Utils import SCORES_FILE_NAME
from flask import Flask, request

app = Flask("WorldOfGames")
score_file = SCORES_FILE_NAME


def generate_html_score_tbl():
    sc = open(score_file, "r").readlines()
    t_body = ""
    for line in sc:
        spl_line = line.split("=")
        name = spl_line[0]
        score = spl_line[1]
        t_body = t_body + "<tr>" + "<td>" + name + "</td>" + "<td>" + score + "</td>" + "</tr>"
    return t_body


@app.route('/scores', methods=['GET'])
def score_server():
    html_head = open("html/html_head.txt", "r").read()
    print(html_head)
    html_tail = open("html/html_tail.txt", "r").read()
    html_table = generate_html_score_tbl()
    return html_head + html_table + html_tail


app.run(host="0.0.0.0", port=5001, debug=True)