import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register')
def register():
    return "register page"
            
            
@bp.route('/login')
def login():
    return "register page"
        
        
@bp.route('/logout')
def logout():
    return "register page"