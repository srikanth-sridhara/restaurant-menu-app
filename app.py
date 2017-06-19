from flask import Flask, render_template, url_for, request, redirect, flash, jsonify

app = Flask(__name__)


# ############ Restaurant endpoints start ############
@app.route('/')
@app.route('/restaurants/')
def indexRestaurant():
    return "This is the index page with a list of all restaurants"


@app.route('/restaurant/new/', methods=['GET','POST'])
def addNewRestaurant():
    return "Add a new restaurant."


@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET','POST'])
def editRestaurant(restaurant_id):
    return "Edit a restaurant."


@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET','POST'])
def deleteRestaurant(restaurant_id):
    return "Delete a restaurant."
# ############ Restaurant endpoints end  ############


# ############ Menu endpoints start      ############
@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def indexMenu(restaurant_id):
    return "This is the index page of a restaurant with a list of menu items."


@app.route('/restaurant/<int:restaurant_id>/new/', methods=['GET','POST'])
def addNewMenuItem(restaurant_id):
    return "Add a new item to the menu"


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit', methods=['GET','POST'])
def editMenuItem(restaurant_id, menu_id):
    return "Edit a menu item"


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete', methods=['GET','POST'])
def deleteMenuItem(restaurant_id, menu_id):
    return "delete a menu item."
# ############ Menu endpoints end        ############


# ############ API endpoints start       ############
@app.route('/restaurants/JSON/')
def getAllRestaurants():
    return "Get all restaurants JSON."


@app.route('/restaurant/<int:restaurant_id>/menu/JSON/')
def getAllMenuItems(restaurant_id):
    return "Get all menu items of restaurant JSON."


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON/')
def getAllItemsOfMenu(restaurant_id, menu_id):
    return "Get all fields in a menu item."
# ############ API endpoints end         ############


if __name__ == '__main__':
    app.debug = True
    app.secret_key = "my_preciousss"
    app.run(host='0.0.0.0', port=5000)
