from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
import dbfunctions as dbf
app = Flask(__name__)

#Fake Restaurants
# restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}
# restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]

#Fake Menu Items
# item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree', 'id':'1','restaurant_id':'1'}
# items = [{'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'},
#         {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},
#         {'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},
#         {'name':'Fresh Iced Tea', 'description':'with freshly squeezed lemon','price':'$.99', 'course':'Beverage','id':'4'},
#         {'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'}]

# ############ Restaurant endpoints start ############
@app.route('/')
@app.route('/restaurants/')
def indexRestaurant():
    restaurants = dbf.showRestaurants()
    return render_template('restaurant/restaurants.html', restaurants=restaurants)


@app.route('/restaurant/new/', methods=['GET','POST'])
def addNewRestaurant():
    if request.method == 'POST':
        restaurantName = request.form['restaurantname']
        restaurantAddress = request.form['restaurantaddress']
        restaurantCategory = request.form['restaurantcategory']

        dbf.newRestaurant(restaurantName, restaurantAddress, restaurantCategory)
        flash("New restaurant added!")
        return redirect(url_for('indexRestaurant'))
    else:
        return render_template('restaurant/add_new_restaurant.html')


@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET','POST'])
def editRestaurant(restaurant_id):
    if request.method == 'POST':
        restaurantName = request.form['restaurantname']
        restaurantAddress = request.form['restaurantaddress']
        restaurantCategory = request.form['restaurantcategory']

        dbf.editRestaurant(restaurant_id, restaurantName, restaurantAddress, restaurantCategory)
        flash("Restaurant edited!")
        return redirect(url_for('indexRestaurant'))
    else:
        restaurant = dbf.getRestaurant(restaurant_id)
        return render_template('restaurant/edit_restaurant.html', restaurant_id=restaurant_id, restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET','POST'])
def deleteRestaurant(restaurant_id):
    if request.method == 'POST':
        dbf.deleteRestaurant(restaurant_id)
        flash("Restaurant deleted!")
        return redirect(url_for('indexRestaurant'))
    else:
        restaurant = dbf.getRestaurant(restaurant_id)
        return render_template('restaurant/delete_restaurant.html', restaurant_id=restaurant_id, restaurant=restaurant)
# ############ Restaurant endpoints end  ############


# ############ Menu endpoints start      ############
@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def indexMenu(restaurant_id):
    restaurant = dbf.getRestaurant(restaurant_id)
    items = dbf.showMenu(restaurant_id)
    return render_template('menu/menu.html', restaurant=restaurant, items=items)


@app.route('/restaurant/<int:restaurant_id>/new/', methods=['GET','POST'])
def addNewMenuItem(restaurant_id):
    if request.method == 'POST':
        name        =request.form['itemname']
        course      =request.form['itemcourse']
        description =request.form['itemdescription']
        price       =request.form['itemprice']

        dbf.newMenuItem(restaurant_id, name, course, description, price)
        flash("New menu item created!")
        return redirect(url_for('indexMenu', restaurant_id=restaurant_id))
    else:
        restaurant = dbf.getRestaurant(restaurant_id)
        return render_template('menu/add_new_menu_item.html', restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit', methods=['GET','POST'])
def editMenuItem(restaurant_id, menu_id):
    if request.method == 'POST':
        name        =request.form['itemname']
        course      =request.form['itemcourse']
        description =request.form['itemdescription']
        price       =request.form['itemprice']

        dbf.editMenuItem(restaurant_id, menu_id, name, course, description, price)
        flash("Menu item edited!")
        return redirect(url_for('indexMenu', restaurant_id=restaurant_id))
    else:
        item = dbf.getMenuItem(menu_id)
        return render_template('menu/edit_menu_item.html', restaurant_id=restaurant_id, item=item)


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete', methods=['GET','POST'])
def deleteMenuItem(restaurant_id, menu_id):
    if request.method == 'POST':
        dbf.deleteMenuItem(menu_id)
        flash("Menu item deleted!")
        return redirect(url_for('indexMenu', restaurant_id=restaurant_id))
    else:
        item = dbf.getMenuItem(menu_id)
        return render_template('menu/delete_menu_item.html', item=item)
# ############ Menu endpoints end        ############


# ############ API endpoints start       ############
@app.route('/restaurants/JSON/')
def getAllRestaurants():
    restaurants = dbf.showRestaurants()
    return jsonify(Restaurant=[r.serialize for r in restaurants])

@app.route('/restaurants/<int:restaurant_id>/JSON/')
def getRestaurant(restaurant_id):
    restaurant = dbf.getRestaurant(restaurant_id)
    return jsonify(Restaurant=restaurant.serialize)

@app.route('/restaurant/<int:restaurant_id>/menu/JSON/')
def getAllMenuItems(restaurant_id):
    items = dbf.showMenu(restaurant_id)
    return jsonify(MenuItem=[i.serialize for i in items])

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON/')
def getMenuItem(restaurant_id, menu_id):
    item = dbf.getMenuItem(menu_id)
    return jsonify(MenuItem=item.serialize)
# ############ API endpoints end         ############


if __name__ == '__main__':
    app.debug = True
    app.secret_key = "my_preciousss"
    app.run(host='0.0.0.0', port=5000)
