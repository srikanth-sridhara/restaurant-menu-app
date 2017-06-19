from flask import Flask, render_template, url_for, request, redirect, flash, jsonify

app = Flask(__name__)

#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}
restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]

#Fake Menu Items
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree', 'id':'1','restaurant_id':'1'}
items = [{'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'},
        {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},
        {'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},
        {'name':'Fresh Iced Tea', 'description':'with freshly squeezed lemon','price':'$.99', 'course':'Beverage','id':'4'},
        {'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'}]

# ############ Restaurant endpoints start ############
@app.route('/')
@app.route('/restaurants/')
def indexRestaurant():
    # return "This is the index page with a list of all restaurants"
    return render_template('restaurant/restaurants.html', restaurants=restaurants)


@app.route('/restaurant/new/', methods=['GET','POST'])
def addNewRestaurant():
    # return "Add a new restaurant."
    return render_template('restaurant/add_new_restaurant.html')


@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET','POST'])
def editRestaurant(restaurant_id):
    # return "Edit a restaurant."
    return render_template('restaurant/edit_restaurant.html', restaurant_id=restaurant_id, restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET','POST'])
def deleteRestaurant(restaurant_id):
    # return "Delete a restaurant."
    return render_template('restaurant/delete_restaurant.html', restaurant_id=restaurant_id, restaurant=restaurant)
# ############ Restaurant endpoints end  ############


# ############ Menu endpoints start      ############
@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def indexMenu(restaurant_id):
    # return "This is the index page of a restaurant with a list of menu items."
    return render_template('menu/menu.html', restaurant=restaurant, items=items)


@app.route('/restaurant/<int:restaurant_id>/new/', methods=['GET','POST'])
def addNewMenuItem(restaurant_id):
    # return "Add a new item to the menu"
    return render_template('menu/add_new_menu_item.html', restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit', methods=['GET','POST'])
def editMenuItem(restaurant_id, menu_id):
    # return "Edit a menu item"
    return render_template('menu/edit_menu_item.html', restaurant_id=restaurant_id, menu_id=menu_id, item=item)


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete', methods=['GET','POST'])
def deleteMenuItem(restaurant_id, menu_id):
    # return "delete a menu item."
    return render_template('menu/delete_menu_item.html', item=item)
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
