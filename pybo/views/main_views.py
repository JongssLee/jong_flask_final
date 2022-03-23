from flask import Blueprint, url_for, render_template
from werkzeug.utils import redirect
bp = Blueprint('main', __name__, url_prefix='/')


# --------------------------------- [edit] ---------------------------------- #
@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
   return redirect(url_for('question._list'))

@bp.route('/graph')
def show_graph():
    return render_template('graph/graph.html')
# --------------------------------------------------------------------------- #

