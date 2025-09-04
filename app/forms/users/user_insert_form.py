from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.choices import SelectMultipleField
from wtforms.validators import DataRequired


class UserInsertForm(FlaskForm):
    class Meta:
        csrf = False

    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    roles = SelectMultipleField(
        "Roles",
        choices=[("admin", "Admin"), ("user", "User"), ("guest", "Guest")],
        validators=[DataRequired()],
    )
