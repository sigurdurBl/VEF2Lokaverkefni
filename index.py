from  bottle import run,route,redirect,request,post,template,app
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

products = [{"pid": 1, "name": "AK-47 Bloodsport FN", "price": "55$"},
            {"pid": 2, "name": "USP-S killconfirmed FN", "price": "40$"},
            {"pid": 3, "name": "AWP Dragon lore FN", "price": "2000$"},
            {"pid": 4, "name": "M4A1- Hyper Beast FN", "price": "61$"},
            {"pid": 5, "name": "Desert Eagle Crimson Web FN", "price": "55$"},
            {"pid": 6, "name": "FAMAS Roll Cage FN", "price": "7$"},
            {"pid": 7, "name": "P250 Supernova FN ", "price": "1$"},
            {"pid": 8, "name": "Krambit gamma doppler FN", "price": "360$"},

            ]
@route("/")
def homepage():
    return template("home.tpl")

@route('/nyskra')
def nyr():
    return template('newlogin.tpl')

@route('/donyskra', method='POST')
def nyr():
    user = request.forms.get('user')
    password = request.forms.get('pass')

    # Connection object, búum til tengingu við gagnagrunn
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1010992109', passwd='mypassword', db='1010992109_vef2lokaverkefni')
    # Cursor object, used to manage the context of a fetch operatio
    cur = conn.cursor()

    # Srepare and execute a database operation (query or command).
    # SQL fyrirspurn, sækjum notanda úr db
    cur.execute("SELECT count(*) FROM user where user=%s",(user))
    # Fetch the next row of a query result set, returning a single sequence, or None when no more data is available.
    result = cur.fetchone() #fáum tuple (runa eða listi af read-only objectum)

    print(result)

    # notandi er ekki til
    if result[0] == 0:
        cur.execute("INSERT INTO user Values(%s,%s)", (user, password))
        # Commit any pending transaction to the database.
        conn.commit()
        cur.close() # stundum sleppt, conn.close() lokar einnig cur.
        # lokum db tengingu
        conn.close()
        return redirect("/shop")
@route('/innskra')
def inn():
    return template('login.tpl')

@route('/doinnskra', method='POST')
def doinn():
    user = request.forms.get('user')
    password = request.forms.get('pass')

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1010992109', passwd='mypassword', db='1010992109_vef2lokaverkefni')
    cur = conn.cursor()

    cur.execute("SELECT count(*) FROM user where user=%s and pass=%s",(user,password))
    result = cur.fetchone()#fáum tuple
    print(result)
    # er u og p til í  db?
    if result[0] == 1:
        cur.close()
        conn.close()
        return redirect("/shop")
@route("/logout")
def logout():
    return redirect("/")

@route("/shop")
def shop():
    return template("shop.tpl" ,products=products)


@route("/cart")
def cart():
    session = request.environ.get('beaker.session')
    karfa = []

    # lesum úr sessions þær vörur sem notandi hefur valið í körfu
    if session.get('1'):
        # notum get aðferð, vísum í key til að sækja gildi
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

# fjarlægjum allar vörur úr körfu
@route("/cart/remove")
def remove_from_cart():
    session = request.environ.get('beaker.session')
    # fjarlægjum allar vörur úr sessions
    session.delete()
    return redirect("/cart")

run(app=app,host="0.0.0.0", port=argv[1])

