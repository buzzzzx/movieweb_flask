from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, FileField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, Regexp, EqualTo
from app.models import User


class RegistForm(FlaskForm):
    name = StringField(
        label="昵称",
        validators=[
            DataRequired("请输入昵称！")
        ],
        description="昵称",
        render_kw={
            "id": "input_name",
            "class": "form-control input-lg",
            "placeholder": "昵称",
        }
    )
    email = StringField(
        label="邮箱",
        validators=[
            DataRequired("请输入邮箱！"),
            Email("邮箱格式不正确！")
        ],
        description="邮箱",
        render_kw={
            "id": "input_email",
            "class": "form-control input-lg",
            "placeholder": "邮箱",
        }
    )
    phone = StringField(
        label="手机号码",
        validators=[
            DataRequired("请输入手机号码！"),
            Regexp("1[34578][0-9]{9}", message="手机号码格式不正确")
        ],
        description="手机号码",
        render_kw={
            "id": "input_phone",
            "class": "form-control input-lg",
            "placeholder": "手机号码",
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码！")
        ],
        description="密码",
        render_kw={
            "id": "input_password",
            "class": "form-control input-lg",
            "placeholder": "密码",
        }
    )
    repwd = PasswordField(
        label="确认密码",
        validators=[
            DataRequired("请输入确认密码！"),
            EqualTo('pwd', message="两次密码不一致！")
        ],
        description="确认密码",
        render_kw={
            "id": "input_repassword",
            "class": "form-control input-lg",
            "placeholder": "确认密码",
        }
    )
    submit = SubmitField(
        "注册",
        render_kw={
            "class": "btn btn-lg btn-success btn-block"
        }
    )

    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user == 1:
            raise ValidationError("昵称已经存在！")

    def validate_email(self, field):
        email = field.data
        user = User.query.filter_by(email=email).count()
        if user == 1:
            raise ValidationError("该邮箱已经被注册！")

    def validate_phone(self, field):
        phone = field.data
        user = User.query.filter_by(phone=phone).count()
        if user == 1:
            raise ValidationError("该手机已经被注册！")


class LoginForm(FlaskForm):
    account = StringField(
        label="账号",
        validators=[
            DataRequired("请输入账号！")
        ],
        description="账号",
        render_kw={
            "id": "input_contact",
            "class": "form-control input-lg",
            "placeholder": "用户名/邮箱/手机号码"
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码！")
        ],
        description="密码",
        render_kw={
            "id": "input_password",
            "class": "form-control input-lg",
            "placeholder": "密码"
        }
    )
    submit = SubmitField(
        "登录",
        render_kw={
            "class": "btn btn-lg btn-success btn-block"
        }
    )

    def validate_account(self, field):
        account = field.data
        account_count = User.query.filter_by(name=account).count()
        if account_count == 0:
            raise ValidationError("该用户名不存在！")


class UserdetailForm(FlaskForm):
    name = StringField(
        label="昵称",
        validators=[
            DataRequired("请输入昵称！")
        ],
        description="昵称",
        render_kw={
            "id": "input_name",
            "class": "form-control input-lg",
            "placeholder": "昵称",
        }
    )
    email = StringField(
        label="邮箱",
        validators=[
            DataRequired("请输入邮箱！"),
            Email("邮箱格式不正确！")
        ],
        description="邮箱",
        render_kw={
            "id": "input_email",
            "class": "form-control input-lg",
            "placeholder": "邮箱",
        }
    )
    phone = StringField(
        label="手机号码",
        validators=[
            DataRequired("请输入手机号码！"),
            Regexp("1[34578][0-9]{9}", message="手机号码格式不正确")
        ],
        description="手机号码",
        render_kw={
            "id": "input_phone",
            "class": "form-control input-lg",
            "placeholder": "手机号码",
        }
    )
    face = FileField(
        label='头像',
        validators=[
            DataRequired("请选择头像！")
        ],
        description="头像",
        render_kw={
            "id": "input_face",
            "class": "form-control"
        }
    )
    info = TextAreaField(
        label='简介',
        validators=[
            DataRequired("请输入简介！")
        ],
        description="简介",
        render_kw={
            "class": "form-control",
            "rows": "10",
            "id": "input_info"
        }
    )
    submit = SubmitField(
        '保存修改',
        render_kw={
            "class": "btn btn-success"
        }
    )


class PwdForm(FlaskForm):
    old_pwd = PasswordField(
        label="旧密码",
        validators=[
            DataRequired("请输入旧密码！")
        ],
        description="旧密码",
        render_kw={
            "class": "form-control",
            "id": "input_oldpwd",
            "placeholder": "请输入旧密码！"
        }

    )
    new_pwd = PasswordField(
        label="新密码",
        validators=[
            DataRequired("请输入新密码！")
        ],
        description="新密码",
        render_kw={
            "class": "form-control",
            "id": "input_newpwd",
            "placeholder": "请输入新密码！"
        }

    )
    submit = SubmitField(
        "修改密码",
        render_kw={
            "class": "btn btn-primary"
        }
    )

    def validate_old_pwd(self, field):
        from flask import session

        oldpwd = field.data
        name = session["user"]
        user = User.query.filter_by(name=name).first()
        if not user.check_pwd(oldpwd):
            raise ValidationError("旧密码错误！")


class CommentForm(FlaskForm):
    content = TextAreaField(
        label='内容',
        validators=[
            DataRequired("请输入内容！")
        ],
        description="评论内容",
        render_kw={
            'id': "input_content"
        }

    )
    submit = SubmitField(
        '提交评论',
        render_kw={
            'class': "btn btn-success",
            'id': "btn-sub"
        }
    )
