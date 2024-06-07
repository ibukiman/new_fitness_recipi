from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms import validators

class LoginForm(FlaskForm):
    username = StringField("ユーザー名",validators=[validators.DataRequired(message="ユーザーネームの入力が必要です")])
    password = PasswordField("パスワード",validators=[validators.DataRequired(message="パスワードの入力が必要です")])
    submit = SubmitField("ログイン")