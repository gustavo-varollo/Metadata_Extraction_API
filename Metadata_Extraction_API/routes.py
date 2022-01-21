from flask import render_template, Blueprint

main = Blueprint('main', __name__, url_prefix='/')


@main.route('/')
def main_template():
    return render_template('upload.html')
