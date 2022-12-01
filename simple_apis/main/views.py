from . import main_blueprint

@main_blueprint.route('/')
def index():
    return 'this is the index route'