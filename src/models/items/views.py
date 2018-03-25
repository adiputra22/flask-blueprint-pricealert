from flask import Blueprint

item_blueprint = Blueprint("items", __name__)

@item_blueprint.route('/<string:name>')
def item_page():
    pass

@item_blueprint.route('/load')
def load_item():
    """
    Loads an items data using their store and a JSON representation of it.
    :return:
    """
    pass