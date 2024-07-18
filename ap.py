from flask import Flask,render_template
import subprocess

app = Flask(__name__, static_folder='pic')

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/execute', methods=['POST'])
def execute():
    subprocess.Popen(["python", r"C:\Users\babbu\OneDrive\Desktop\major\Reusable captcha security engine\generatecaptcha.py"])
    return 'Python file executed!'


if __name__ == '__main__':
    app.run()

