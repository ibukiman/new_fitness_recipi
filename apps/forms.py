from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms import validators

class SignupForm(FlaskForm):
    username = StringField("ユーザー名",validators=[validators.DataRequired(message="入力が必要です。"),
                                               validators.length(max=30,message="30文字以内で入力して下さい。")])
    password = PasswordField("パスワード",validators=[validators.DataRequired(message="入力が必要です。"),
                                                validators.length(min=6,message="6文字以上で入力して下さい。")])
    submit = SubmitField("新規登録")