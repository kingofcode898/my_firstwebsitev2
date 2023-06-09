from flask import Flask, render_template, jsonify 

app = Flask(__name__)

JOBS = [
{
  "id": 1,
  'title': 'Data Analyst',
  'location': 'San Diego, California',
  'salary': 'U.S 100,000',
},
{
  "id": 2 ,
  'title': 'Data Scientist',
  'location': 'San Francisco, California',
  'salary': 'U.S 120,000'
},
{
  "id": 3,
  'title': 'Lead Data Analyst',
  'location': 'San Diego, California',
}
]

@app.route("/")
def Homepage():
    return render_template('home.html',       
              jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS) 

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)