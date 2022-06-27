from flask import Flask, render_template, request, redirect, send_file
from indeed import get_indeed_jobs
from remoteok import get_remoteok_jobs
from stackoverflow import get_stackoverflow_companys
from weworkremotely import get_wwr_jobs
from exporter import save_to_file

app = Flask("SupperScrapper")

db = {}
indeed_db = {}
remoteok_db = {}
so_db = {}
wwr_db = {}

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
      indeed_jobs = get_indeed_jobs(word)
      remoteok_jobs = get_remoteok_jobs(word)
      so_jobs = get_stackoverflow_companys(word)
      wwr_jobs = get_wwr_jobs(word)
      jobs = indeed_jobs + remoteok_jobs + so_jobs + wwr_jobs
      db[word] = jobs
      indeed_db[word] = indeed_jobs
      remoteok_db[word] = remoteok_jobs
      so_db[word] = so_jobs
      wwr_db[word] = wwr_jobs
  else:
    return redirect("/")
  return render_template(
    "report.html",
    searchingBy=word,
    resultNumber=len(jobs),
    jobs=jobs
  )

@app.route("/indeed")
def report_indeed():
  word = request.args.get('word')
  jobs = indeed_db.get(word)
  return render_template(
    "indeed.html",
    searchingBy=word,
    resultNumber=len(jobs),
    jobs=jobs
  )

@app.route("/remoteok")
def report_remoteok():
  word = request.args.get('word')
  jobs = remoteok_db.get(word)
  return render_template(
    "remoteok.html",
    searchingBy=word,
    resultNumber=len(jobs),
    jobs=jobs
  )

@app.route("/stackoverflow")
def report_stackoverflow():
  word = request.args.get('word')
  jobs = so_db.get(word)
  return render_template(
    "stackoverflow.html",
    searchingBy=word,
    resultNumber=len(jobs),
    jobs=jobs
  )

@app.route("/wwr")
def report_wwr():
  word = request.args.get('word')
  jobs = wwr_db.get(word)
  return render_template(
    "wwr.html",
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