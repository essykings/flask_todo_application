from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField,SelectField, BooleanField, DateField, SubmitField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')




class TodoForm(FlaskForm):
    task_name = StringField('Name', validators=[DataRequired()])
    due_date = DateField('Due Date', validators=[DataRequired()])
    status = SelectField('Status', choices=[('Complete', 'Complete'), ('Not Started', 'Not Started ')])
    submit = SubmitField('Add Task')

class EditTodoForm(FlaskForm):
    task_name = StringField('Name', validators=[DataRequired()])
    due_date = DateField('Due Date', validators=[DataRequired()])
    status = SelectField('Status', choices=[('COMPLETED', 'COMPLETED'), ('NOTSTARTED', 'NOTSTARTED')])
    submit = SubmitField('Edit Task')