# coding: utf8

from . import home
from flask import render_template, redirect, url_for, flash, session, request
from app.models import User, Userlog
from app.home.forms import RegistForm, LoginForm
from werkzeug.security import generate_password_hash
import uuid
from app import db
from functools import wraps


# 登录装饰器（访问控制）
def user_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for('home.login', next=request.url))
        return f(*args, **kwargs)

    return decorated_function


@home.route("/")
def index():
    return render_template("home/index.html")


# 会员登录
@home.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(name=data['account']).first()
        if not user.check_pwd(data['pwd']):
            flash("密码错误！", "err")
            return redirect(url_for('home.login'))
        session["user"] = user.name
        session["user_id"] = user.id
        userlog = Userlog(
            user_id=user.id,
            ip=request.remote_addr
        )
        db.session.add(userlog)
        db.session.commit()
        return redirect(url_for("home.user"))
    return render_template("home/login.html", form=form)


@home.route("/logout/")
def logout():
    session.pop("user", None)
    session.pop("user_id", None)
    return redirect(url_for("home.login"))


# 会员注册
@home.route("/regist/", methods=["GET", "POST"])
def regist():
    form = RegistForm()
    if form.validate_on_submit():
        data = form.data
        user = User(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            pwd=generate_password_hash(data['pwd']),
            uuid=uuid.uuid4().hex
        )
        db.session.add(user)
        db.session.commit()
        flash("注册成功！", "success")
    return render_template("home/regist.html", form=form)


@home.route("/user/")
@user_login_req
def user():
    return render_template("home/user.html")


@home.route("/psw/")
@user_login_req
def psw():
    return render_template("home/psw.html")


@home.route("/comments/")
@user_login_req
def comments():
    return render_template("home/comments.html")


@home.route("/loginlog/")
@user_login_req
def loginlog():
    return render_template("home/loginlog.html")


@home.route("/moviecol/")
@user_login_req
def moviecol():
    return render_template("home/moviecol.html")


@home.route("/animation/")
def animation():
    return render_template("home/animation.html")


@home.route("/search/")
def search():
    return render_template("home/search.html")


@home.route("/play/")
def play():
    return render_template("home/play.html")
