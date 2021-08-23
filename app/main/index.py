# 필요한 모듈 import
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

main = Blueprint('main', __name__, url_prefix='/')  # url_prefix : '/'로 url을 붙여라


@main.route('/', methods=['GET'])
def index():
    return render_template('/main/index.html')

@main.route('/season', methods=['GET'])
def season():
    return render_template('/main/selectseason.html')

@main.route('/ingredient', methods=['GET'])
def ingredient():
    return render_template('/main/ingredient.html')