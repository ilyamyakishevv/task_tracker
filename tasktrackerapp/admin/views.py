from flask_login import current_user, login_required
from flask import Blueprint, render_template, flash, redirect, url_for
from tasktrackerapp.user.models import Users
from tasktrackerapp.admin.models import Roles
from tasktrackerapp.admin.forms import AddForm, DeleteForm

from tasktrackerapp.db import db

blueprint = Blueprint('admin', __name__, url_prefix='/admins')

@blueprint.route('/del_user', methods=['POST', 'GET'])
@login_required
def del_user():
    form = DeleteForm()
    if form.validate_on_submit():
        inp_login = form.del_login.data
        search = db.session.query(Users).filter(Users.login == inp_login).one()
        db.session.delete(search)
        db.session.commit()
    flash('Пользователь удален')
    return redirect(url_for('admin'))

@blueprint.route('/admin')
@login_required
def admin():
    form = AddForm()
    form2 = DeleteForm()
    roles = Roles.query.order_by(Roles.id).all() 
    form.role.choices = [role.role for role in roles]
    if current_user.role == 'admin':
        return render_template('admin.html', title='Sign In', form=form, form2=form2)
    else:
        return redirect(url_for('admin.index'))
    

@blueprint.route('/add_user', methods=['POST', 'GET'])
@login_required
def add_user():    
    form = AddForm()
    roles = Roles.query.order_by(Roles.id).all()     
    form.role.choices = [role.role for select in roles]
    if form.validate_on_submit():     
        login = form.login.data   
        password1 = form.password.data
        password2 = form.password.data
        firname_lasname = form.firname_lasname.data
        email = form.email.data
        role = form.role.data
        user_info = Users(login=login, firname_lasname=firname_lasname, email=email, role=role)     
        user_info.set_password(password1)
        db.session.add(user_info)  
        db.session.commit()                
    flash('Пользователь добавлен')
    return redirect(url_for('admin.admin'))
