from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("SupperScrapper")

db = {}

# '@' -> 데코레이트 : 아래에 있는 함수를 실행(*함수만)
@app.route("/")
def home():
  return render_template("potato.html")

# query argument : url에서 &, ? 뒤쪽에 있는 내용
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

app.run(host="0.0.0.0")


#https://studiomeal.com/archives/533 -> 그리드 잘 정리된 듯