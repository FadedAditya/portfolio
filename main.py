from flask import Flask,render_template,url_for,request
import csv
app=Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")

def write_to_txt(data):
    with open("database.txt",mode="a",newline="") as database:
        email=data["email"]
        subject = data["subject"]
        message = data["message"]
        file1=database.write(f"\n{email},{subject},{message}")

def write_to_csv(data):
    with open("database.csv",mode="a",newline="") as database:
        writer = csv.writer(database)
        writer.writerows(data)





@app.route('/thank', methods=['GET', 'POST'])
def submit_message():
    if request.method == 'POST':
        data=request.form.to_dict()
        write_to_txt(data)
        return render_template('thank.html')
    else:
        return render_template('index.html')
