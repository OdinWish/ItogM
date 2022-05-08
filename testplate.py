from flask import Flask, render_template, request
import os

import sqlite3


folder = os.getcwd()
print("=========================",folder)
app = Flask(__name__, template_folder=folder)



@app.route('/')
def index():

    return render_template('itogovoe/templates/page1.html')

@app.route('/p2', methods=['GET', 'POST'])
def index2():
    user = request.args.get('user')
    famil = request.args.get('famil')
    obomne = request.args.get('obomne')
    avatar = request.args.get("avatar")
    print(user)
    return render_template('itogovoe/templates/page2.html',user=user, famil=famil, obomne=obomne, avatar=avatar) 

if __name__ == "__main__":
    app.run()
