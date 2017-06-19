# Restaurant App.

* Has a list of restaurants. You can add/delete/edit a restaurant.
* Restaurant has: Restaurant id, name, address, category.
* Each restaurant has a menu. You can add/delete/edit menu items.
* Each menu item has: id, name, description, price, course, restaurant_id


## Restaurant End-points:
* `/` or `/restaurants/`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Show all restaurants.
* `/restaurant/new/`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Add a new restaurant.
* `/restaurant/<id>/edit/`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Edit a restaurant.
* `/restaurant/<id>/delete/`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Delete a restaurant


## Menu End-points:
* `/restaurant/<id>(/menu/)`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Show the full menu
* `/restaurant/<id>/new/`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Add a menu item
* `/restaurant/<id>/<menuid>/edit`&nbsp;&nbsp;&nbsp;&nbsp; Edit a menu item
* `/restaurant/<id>/<menuid>/delete` Edit a menu item

## API end-points in JSON:
* `/restaurants/JSON`                     List of Restaurants
* `/restaurant/<id>/menu/JSON`            List of menu items in a restaurant
* `/restaurant/<id>/menu/<menuid>/JSON`   List of items in a menu item of a restaurant


## CRUD functions:
* `showRestaurants()`
* `newRestaurant()`
* `editRestaurant()`
* `deleteRestaurant()`


* `showMenu()`
* `newMenuItem()`
* `editMenuItem()`
* `deleteMenuItem()`
