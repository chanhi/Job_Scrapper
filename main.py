from flask import Flask, render_template, request

app = Flask("SupperScrapper")

# '@' -> 데코레이트 : 아래에 있는 함수를 실행(*함수만)
@app.route("/")
def home():
  return render_template("potato.html")

# query argument : url에서 &, ? 뒤쪽에 있는 내용
@app.route("/report")
def report():
  word = request.args.get('word')
  return render_template("report.html", searchingBy=word)

app.run(host="0.0.0.0")