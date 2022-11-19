from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from tasktrackerapp.task.forms import TaskAdd, TaskEdit, CommentForm
from tasktrackerapp.user.models import Users
from tasktrackerapp.task.models import Tasks, Actions, Comment, Changes
from tasktrackerapp.db import db
from datetime import datetime, date



blueprint = Blueprint('task', __name__)

@blueprint.route('/add_task')
@login_required
def add_task():
    title = "Добавить задачу"
    all_responsible = Users.query.order_by(Users.id).all()
    add_task_form = TaskAdd()
    add_task_form.responsible.choices = [r.firname_lasname for r in all_responsible]
    return render_template(
                    'tasks/add_task.html',
                    title=title,
                    form=add_task_form
                    )


@blueprint.route('/adding_task', methods=['POST'])
@login_required
def adding_task():
    adding_form = TaskAdd()
    all_responsible = Users.query.order_by(Users.id).all()
    adding_form.responsible.choices = [r.firname_lasname for r in all_responsible]
    if adding_form.validate_on_submit():
        task_name = adding_form.name.data
        task_description = adding_form.description.data
        task_deadline = adding_form.deadline.data
        if task_deadline < date.today():
            flash("Ввелите корректную дату!")
            return redirect(url_for('task.add_task'))
        task_creator = current_user.firname_lasname
        task_responsible = adding_form.responsible.data
        new_task = Tasks(
            name=task_name,
            description=task_description,
            status='OPEN',
            deadline=task_deadline,
            creator=task_creator,
            responsible=task_responsible,
            is_deleted=False
            )
        db.session.add(new_task)
        db.session.commit()
        new_action = Actions(
            action_user=current_user.id, 
            action_object=new_task.id, 
            action_description=Actions.ADD_TASK
        )
        db.session.add(new_action)
        db.session.commit()
        flash("Задание успешно добавлено")
        return redirect(url_for('task.add_task'))
    flash("Заполните все поля!")
    return redirect(url_for('task.add_task'))

@blueprint.route('/task/<int:id>/edit', methods=['POST', 'GET'])
@login_required
def edit_task(id):
    task = Tasks.query.get(id)
    edit_form = TaskEdit()
    if edit_form.validate_on_submit():
        task.name = edit_form.name.data
        task.description = edit_form.description.data
        task.deadline = edit_form.deadline.data
        if task.deadline < date.today():
            flash("Ввелите корректную дату!")
            return redirect(url_for('task_edit'))
        db.session.commit()
        new_action = Actions(
            action_user=current_user.id, 
            action_object=task.id, 
            action_description=Actions.EDIT_TASK
        )
        db.session.add(new_action)
        db.session.commit()
        flash("Задание успешно измненено")
        return redirect(url_for('view_tasks'))
    return render_template('tasks/edit_task.html', form=edit_form)


@blueprint.route('/task/<int:id>/delete')
@login_required
def delete_task(id):
    task = Tasks.query.get_or_404(id)
    try: 
        task.is_deleted = True
        db.session.commit()
        new_action = Actions(
            action_user=current_user.id, 
            action_object=task.id, 
            action_description=Actions.DELETE_TASK
        )
        db.session.add(new_action)
        db.session.commit()
        return redirect(url_for('view_tasks'))
    except:
        db.session.rollback()
        return flash("При удалении задания произошла ошибка")


@blueprint.route('/task/<int:id>', methods=['GET', 'POST'])
@login_required
def get_task(id):
    task = Tasks.query.get(id)
    comment_form = CommentForm(task_id=task.id)
    if request.method == "POST":
        new_action = Actions(
                action_user=current_user.id,
                action_object=task.id
        )
        if "in work" in request.form: 
            task.status = "IN WORK"
            new_action.action_description = Actions.STATUS_IN_WORK
        elif "in review" in request.form: 
            task.status = "IN REVIEW"
            new_action.action_description = Actions.STATUS_IN_REVIEW
        elif "in work again" in request.form: 
            task.status = "IN WORK"
            new_action.action_description = Actions.STATUS_IN_WORK_AGAIN
        elif "done" in request.form:
            task.status = "DONE"
            new_action.action_description = Actions.STATUS_DONE
        elif "cancel" in request.form:
            task.status = "DONE"
            new_action.action_description = Actions.CANCELATION 
        db.session.add(new_action)
        db.session.commit()   
    return render_template('tasks/task.html', task=task, comment_form=comment_form) 


@blueprint.route('/task/comment', methods=['POST'])
def add_comment():
    form = CommentForm()
    if form.validate_on_submit():
        if Tasks.query.filter(Tasks.id == form.task_id.data).first():
            comment = Comment(text=form.comment_text.data, task_id=form.task_id.data, user_id=current_user.id)
            db.session.add(comment)
            db.session.commit()
            flash('Комментарий успешно добавлен')
            new_action = Actions(
                action_user=current_user.id, 
                action_object=comment.task_id,
                action_description=Actions.COMMENT
            )
            db.session.add(new_action)
            db.session.commit()
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в заполнении поля "{}": - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
    return redirect(request.referrer)
  


@blueprint.route('/view_tasks')
@login_required
def view_tasks():
    title = "Все задачи"
    tasks = Tasks.query.order_by(Tasks.id).all()
    return render_template('tasks/view_tasks.html', title=title, tasks=tasks)