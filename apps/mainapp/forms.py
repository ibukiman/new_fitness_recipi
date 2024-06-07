from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms import validators
from flask_wtf import file

class UploadImageForm(FlaskForm):
    title = StringField("料理名",validators=[validators.DataRequired(message="入力が必要です。"),
                        validators.length(max=200,message="200文字以内で入力して下さい")])
    material = TextAreaField("材料")
    how_to = TextAreaField("作り方")
    p = StringField("p",validators=[validators.DataRequired(message="入力が必要です。"),])
    f = StringField("f",validators=[validators.DataRequired(message="入力が必要です。"),])
    c = StringField("c",validators=[validators.DataRequired(message="入力が必要です。"),])
    kcal = StringField("カロリー",validators=[validators.DataRequired(message="入力が必要です。"),])
    url = StringField("参照元url",validators=[validators.DataRequired(message="入力が必要です。"),])
    image = file.FileField(validators=[file.FileRequired("画像ファイルを選択して下さい"),
                                       file.FileAllowed(['png','jpg','jpeg'],'サポートされていないファイル形式です。')])
    submit = SubmitField('投稿する')

class SearchForm(FlaskForm):
    serch_input = StringField("検索")
    submit = SubmitField('検索')


# class Delete_Form(FlaskForm):
    # submit = SubmitField('削除')
    
    

    
    