# -*- coding: utf-8 -*-
from flask import Blueprint, redirect
from flaskbb.utils.helpers import render_template

from .forms import AddForm, DeleteForm
from .models import MyPost
from flaskbb.extensions import db

news = Blueprint("news", __name__, template_folder="templates")


def inject_news_link():
    return render_template("navigation_snippet.html")


@news.route("/")
def index():
    return render_template("index.html", newsposts = MyPost.query.all())


@news.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        p = MyPost(name = form.name.data, text = form.text.data)
        db.session.add(p)
        db.session.commit()
        return redirect('/news')
    return render_template('add.html', form=form)

@news.route('/delete', methods=['GET', 'POST'])
def delete():
    form = DeleteForm()
    if form.validate_on_submit():        
        p = MyPost.query.filter(MyPost.name == form.name.data).first()
        db.session.delete(p)
        db.session.commit()        
        return redirect('/news')
    return render_template('delete.html', form=form)


