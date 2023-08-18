from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def runapp():
    file = open('output.txt','r')
    lines = file.readlines()
    lines = "\n".join(lines)
    return render_template('index.html',str = lines)


if __name__=="__main__":
    app.run(debug=True)
