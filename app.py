from flask import Flask,request,redirect,render_template,session
from dbms import *
import pymysql as p

app=Flask(__name__)

app.secret_key="abc"

def getConnection():
    return p.connect(host='localhost',user='root',port=3306,database='portfolio')


#First Routing
@app.route("/")
def home_func():
    return redirect('/home')


@app.route('/home')
def home():
    datalist=fetchData()
    return render_template('home.html',data=datalist)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contactus():
    return render_template('contactus.html')


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/teams')
def teams():
    return render_template('teams.html')


@app.route("/savecreate",methods=["POST", "GET"])
def save_create():
    t=request.form['title']
    c=request.form['content']
    tc=(t,c)
    addDataCreate(tc)
    return redirect("/allpost")


@app.route("/show")
def allpost():
    return render_template('allpost.html')


@app.route('/allpost')
def show_func():
    datalist=fetchData()
    return render_template("allpost.html",data=datalist)


@app.route("/edit/<int:id>")
def displayforupdate(id):
    datalist=specificData(id)
    return render_template("edit.html",data=datalist)


@app.route("/update/<int:id>",methods=["POST"])
def updatefun(id):
    n=request.form['name']
    u=request.form['username']
    tu=(n,u,id)
    addDataUpdate(tu)
    return redirect("/allpost")


@app.route("/delete/<int:id>")
def deletefun(id):
    deleteData(id)
    return redirect("/allpost") 


# katrina start

@app.route("/sourabh")
def sourabh():
    datalist=fetchData()
    return render_template("sourabh.html",data=datalist)

# katrina end 

# kareena start

@app.route("/vivek")
def vivek():
    datalist=fetchData()
    return render_template("vivek.html",data=datalist)

# kareena end 

# madhuri start

@app.route("/abhi")
def abhi():
    datalist=fetchData()
    return render_template("abhi.html",data=datalist)

# madhuri end

# web start

@app.route('/web')
def web():
    return render_template('web.html')

# web end

# advt start

@app.route('/advt')
def advt():
    return render_template('advt.html')

# advt end

# app start

@app.route('/app')
def appd():
    return render_template('app.html')

# app end

# book start

@app.route('/book')
def book():
    return render_template('book.html')


@app.route("/savelink",methods=["POST", "GET"])
def save_func():
    n=request.form['name']
    u=request.form['email']
    p=request.form['number']
    b=request.form['bank']
    a=request.form['account']
    i=request.form['ifsc']
    t=(n,u,p,b,a,i)
    addData(t)
    return redirect("/bookdone")

# book end

# booking done start

@app.route('/bookdone')
def bookdone():
    return render_template('bookdone.html')

# booking done end


if __name__=='__main__':
     app.run(debug=True)
