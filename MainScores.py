from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE
from flask import Flask, request

app = Flask("WorldOfGames")
score_file = SCORES_FILE_NAME
error_code = BAD_RETURN_CODE

def generate_html_score_tbl():
    try:
        sc = open(score_file, "r").readlines()
        t_body = ""
        for line in sc:
            spl_line = line.split("=")
            name = spl_line[0]
            score = spl_line[1]
            t_body = t_body + "<tr>" + "<td>" + name + "</td>" + "<td>" + score + "</td>" + "</tr>"
        status = 0
        return t_body, status
    except BaseException as b:
        t_body = """
        <html>
<head>
<title>Scores Game</title>
</head>
<body>
<body>
<h1><div id="score" style="color:red">""" +"Error Code: "  +  str(error_code) + """</div></h1>
</body>
</html>
        """
        status = error_code
        return t_body, status







@app.route('/scores', methods=['GET'])
def score_server():
    html_head = open("html/html_head.txt", "r").read()
    print(html_head)
    html_tail = open("html/html_tail.txt", "r").read()
    html_table, status = generate_html_score_tbl()
    if status == 0:
        return html_head + html_table + html_tail
    else:
        return html_table


app.run(host="0.0.0.0", port=5001, debug=True)