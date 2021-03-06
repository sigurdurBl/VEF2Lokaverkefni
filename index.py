from  bottle import run,route,redirect,request,post,template,app,response,static_file
from sys import argv
import pymysql
from beaker.middleware import SessionMiddleware
session_opts = {
    'session.type': 'file',
   # 'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(app(), session_opts)
#hear are products that are used on webstore
products = [{"pid": 1, "name": "AK-47 Bloodsport FN", "price": 55},
            {"pid": 2, "name": "USP-S killconfirmed FN", "price": 40},
            {"pid": 3, "name": "AWP Dragon lore FN", "price": 2000},
            {"pid": 4, "name": "M4A1- Hyper Beast FN", "price": 61},
            {"pid": 5, "name": "Desert Eagle Crimson Web FN", "price": 55},
            {"pid": 6, "name": "FAMAS Roll Cage FN", "price": 7},
            {"pid": 7, "name": "P250 Supernova FN ", "price": 1},
            {"pid": 8, "name": "Krambit gamma doppler FN", "price": 360},

            ]
@route("/")
def homepage():
    return template("home.tpl")
#this routes you to a from for new login to make a new user on the webside
@route('/nyskra')
def nyr():
    return template('newlogin.tpl')

@route('/donyskra', method='POST')
def nyr():
    #hear i request user from the froms
    user = request.forms.get('user')
    password = request.forms.get('pass')

    response.set_cookie("account", user, secret='some-secret-key')
    #hear i connect to a database that contains a user info
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1010992109', passwd='mypassword', db='1010992109_vef2lokaverkefni')

    cur = conn.cursor()

    #hear i check if  user is in database if not it vill append
    cur.execute("SELECT count(*) FROM user where user=%s",(user))

    result = cur.fetchone()

    print(result)

    #hear i append user and redirect him to the web store
    if result[0] == 0:
        cur.execute("INSERT INTO user Values(%s,%s)", (user, password))

        conn.commit()
        cur.close()

        conn.close()
        return redirect("/shop")
#this takes you to login to login if user is already inn database
@route('/innskra')
def inn():
    return template('login.tpl')
@route('/doinnskra', method='POST')
def doinn():
    user = request.forms.get('user')
    password = request.forms.get('pass')
    response.set_cookie("account", user, secret='some-secret-key')
    # hear we connect to database
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1010992109', passwd='mypassword', db='1010992109_vef2lokaverkefni')
    cur = conn.cursor()
    #hear we check if user is in database
    cur.execute("SELECT count(*) FROM user where user=%s and pass=%s",(user,password))
    result = cur.fetchone()
    print(result)
    #if user is in database he wil be redirect to the web store
    if result[0] == 1:
        cur.close()
        conn.close()
        return redirect("/shop")
#this is where you logout from cart
@route("/logout")
def logout():
    response.set_cookie("account", "", expires=0)
    return redirect("/")

@route("/shop")
def shop():
    return template("shop.tpl" ,products=products)

#this is the users cart that saves the items that user wants to buy
@route("/cart")
def cart():
    username = request.get_cookie("account", secret='some-secret-key')
    if username:
        session = request.environ.get('beaker.session')

        karfa = []


        if session.get('1'):

            vara1 = session.get('1')
            karfa.append(vara1)

        if session.get('2'):
            vara2 = session.get('2')
            karfa.append(vara2)

        if session.get('3'):
            vara3 = session.get('3')
            karfa.append(vara3)

        if session.get('4'):
            vara4 = session.get('4')
            karfa.append(vara4)

        if session.get('5'):
            vara5 = session.get('5')
            karfa.append(vara5)

        if session.get('6'):
            vara6 = session.get('6')
            karfa.append(vara6)
        if session.get('7'):
            vara7 = session.get('7')
            karfa.append(vara7)

        if session.get('8'):
            vara8 = session.get('8')
            karfa.append(vara8)


        return template("cart.tpl", karfa=karfa)

#hear you add the products in to your cart
@route("/cart/add/<id:int>")
def add_to_cart(id):
    if id == 1:
        session = request.environ.get('beaker.session')
        session["1"] = "AK-47 Bloodsport FN"
        session.save()
        return redirect("/cart")
    if id == 2:
        session = request.environ.get('beaker.session')
        session[str(id)] = products[id - 1]["name"]
        session.save()
        return redirect("/cart")
    if id == 3:
        session = request.environ.get('beaker.session')
        session[str(id)] = products[id - 1]["name"]
        session.save()
        return redirect("/cart")
    if id == 4:
        session = request.environ.get('beaker.session')
        session[str(id)] = products[id - 1]["name"]
        session.save()
        return redirect("/cart")
    if id == 5:
        session = request.environ.get('beaker.session')
        session[str(id)] = products[id - 1]["name"]
        session.save()
        return redirect("/cart")
    if id == 6:
        session = request.environ.get('beaker.session')
        session[str(id)] = products[id - 1]["name"]
        session.save()
        return redirect("/cart")
    if id == 7:
        session = request.environ.get('beaker.session')
        session[str(id)] = products[id - 1]["name"]
        session.save()
        return redirect("/cart")
    if id == 8:
        session = request.environ.get('beaker.session')
        session[str(id)] = products[id - 1]["name"]
        session.save()
        return redirect("/cart")

    else:
        return redirect("/shop")


@route("/cart/remove")
def remove_from_cart():
    session = request.environ.get('beaker.session')

    session.delete()
    return redirect("/cart")
@route('/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='css')
@route('images/<filename:re:.*\.jpg>')
def send_image(filename):
    # static/img directory
    return static_file(filename, root='images', mimetype='images/jpg')
@route('/images/<filename:re:.*\.png>')
def send_image(filename):
    # static/img directory
    return static_file(filename, root='images', mimetype='images/png')

run(app=app,host="0.0.0.0", port=argv[1])

