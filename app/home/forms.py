from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
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
