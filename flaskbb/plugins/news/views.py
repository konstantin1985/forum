# -*- coding: utf-8 -*-
from flask import Blueprint, redirect
from flaskbb.utils.helpers import render_template

from .forms import AddForm
from .models import NewsPost
from flaskbb.extensions import db

news = Blueprint("news", __name__, template_folder="templates")


def inject_news_link():
    return render_template("navigation_snippet.html")


@news.route("/")
def index():
    
    newsposts = []
    for i in NewsPost.query.all():
        print(i)
        print(i.text)
        newsposts.append(i.text)
    
    return render_template("index.html", newsposts = newsposts)


@news.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        p = NewsPost(text = form.text.data)
        db.session.add(p)
        db.session.commit()
        return redirect('/news')
    return render_template('add.html', 
                           form=form)
