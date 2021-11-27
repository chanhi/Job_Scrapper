from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file

app = Flask("SupperScrapper")

db = {}

# '@' -> 데코레이트 : 아래에 있는 함수를 실행(*함수만)
@app.route("/")
def home():
  return render_template("home.html")

# query argument : url에서 ? 뒤쪽에 있는 내용 ex> /report?arg1&arg2 -> arg1, arg2 둘 전달
@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()
    existingJobs = db.get(word)
    if existingJobs:
      jobs = existingJobs
    else:
      jobs = get_jobs(word)
      db[word] = jobs
  else:
    return redirect("/")
  return render_template(
    "report.html",
    searchingBy=word,
    resultNumber=len(jobs),
    jobs=jobs
  )

@app.route("/export")
def export():
  try:
    word = request.args.get('word')
    if not word:
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    save_to_file(jobs)
    return send_file("jobs.csv", attachment_filename="jobs.csv", as_attachment=True)
  except:
    return redirect("/")

app.run(host="0.0.0.0")


#https://studiomeal.com/archives/533 -> 그리드 잘 정리된 듯