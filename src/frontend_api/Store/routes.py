from flask import redirect, render_template, flash, url_for, request, Blueprint
from src.logic.extention.userEx import Current_user

blp = Blueprint('Stores', __name__)


@blp.route('/')
@blp.route('/home', methods=['GET'])
def home():
    return render_template('StoreTemplates/Home.html', current_user=current_user)


@blp.route('/about')
def about():
    return render_template('StoreTemplates/About.html')
