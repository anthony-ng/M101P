import bottle

@bottle.route('/')
def home_page():
    return "<h1>Hello World!</h1>"

@bottle.route('/test')
def test_page():
    return 'this is a test page'

@bottle.route('/fruits')
def fruits_page():
    fruits = ['apple', 'orange', 'peach']
    return bottle.template('fruits', {'name':'Anthony', 'fruits':fruits})

@bottle.post('/favorite')
def favorite():
    fruit = bottle.request.forms.get("fruit")
    if (fruit == None or fruit == ""):
        fruit = "No Fruit Selected"
        return fruit

    bottle.response.set_cookie("fruit", fruit)
    bottle.redirect('/show_fruit')
    # return bottle.template('favorite', fruit=fruit)

@bottle.route('/show_fruit')
def show_fruit():
    fruit = bottle.request.get_cookie("fruit")

    return bottle.template('favorite', {'fruit':fruit})

bottle.debug(True)
bottle.run(host='localhost', port=8080)
