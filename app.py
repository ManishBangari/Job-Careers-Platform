from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

jobs = [
  {
    'id':1,
    'title':'Data Scientist',
    'location':'Chennai, India',
    'salary':'12,00,000'
  },
  {
    'id':2,
    'title':'Data Engineer',
    'location':'Delhi, India',
    'salary':'8,00,000'
  },
  {
    'id':3,
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'salary':'10,00,000'
  }
]
@app.route("/")
def helloworld():
  return render_template('home.html', jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(jobs)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
