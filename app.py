
from flask import Flask,render_template,request

app = Flask(__name__)
 

@app.route('/')
def index():
    if request.method == 'GET':
        print("Its in get")
        print("1")
        return render_template("index.html")
    else:
        print("2")
        return render_template('Dashboard.html')
    
@app.route("/index")
def ind():

   return render_template("index.html")

@app.route('/about', methods = ['GET', 'POST'])
def about():
    print("page open")
    return render_template('about.html')

@app.route('/courses', methods = ['GET', 'POST'])
def courses():
    print("page open")
    return render_template('Courses.html')


@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    print("page open")
    return render_template('Contact.html')

@app.route('/signup',methods=['GET','POST'])
def signup(): 
    
        
        return render_template('signup.html')



