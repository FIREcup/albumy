from flask import render_template, flash, redirect, url_for, Blueprint
from flask_login import login_user, logout_user, login_reuqired, current_user, login_fresh, confirm_login

from .extensions import db
from .froms.auth import RegisterForm
from .models import User


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.eamil.data
        username = form.username.data
        password = form.password.data
        user = User(name=name, email=email, username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        token = generate_token(user=user, operation='confirm')
        send_confirm_email(user=user, token=token)
        flash('Cofirm eamil send, check your inbox.', 'info')
        return redirect(url_for('.login')
    return render_template('auth/register.html', form=form)
