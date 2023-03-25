from flask import redirect, render_template, flash, url_for, request, Blueprint


blp = Blueprint('Stores', __name__)



@blp.route('/')
@blp.route('/home',methods=['GET'])
def home():
    return render_template('StoreTemplates/Home.html')


@blp.route('/about')
def about():
    return render_template('StoreTemplates/About.html')