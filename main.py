from . import db, app, Data
from flask import render_template, request, redirect

@app.route('/')
def home ():
    return render_template('home.html')

@app.route('/submit', methods=['POST', 'GET'])
def post_submit ():
    try:
        if request.method == 'POST':
            data = Data(request.form['name'], request.form['college'])
            db.session.add(data)
            db.session.commit()
            return redirect('/')
    except :
        return "If you are entering data which is already in the database then you will encounter an error. Name must be unique."
    
    
    if request.method == 'GET':
        content = Data.query.all()
        return render_template('result.html', cont = content)
        

if __name__ == '__main__':
    app.run(debug=True)
    
    #export FLASK_APP=main.py