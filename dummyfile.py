# Initialize the Flask application
# @app.route('/')
# def index():
#    return render_template('log_in.html')


# @app.route('/login',methods = ['POST', 'GET']) 
# def login(): 
#    if request.method == 'POST' and request.form['username'] == 'admin' :
#       return redirect(url_for('success'))
#    else:
#       return redirect(url_for('index'))


# @app.route('/success')
# def success():
#    return 'logged in successfully'


# @app.route('/')
# def student():
#    return render_template('student.html')


# @app.route('/result',methods = ['POST', 'GET'])
# def result():
#    if request.method == 'POST':
#       result = request.form
#       return render_template("result.html",result = result)


# class ContactForm(Form):
#    name = TextField("Name Of Student",[validators.Required("Please enter your name.")])
#    Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
#    Address = TextAreaField("Address")
   
#    email = TextField("Email",[validators.Required("Please enter your email address."),
#       validators.Email("Please enter your email address.")])
   
#    Age = IntegerField("age")
#    language = SelectField('Languages', choices = [('cpp', 'C++'), 
#       ('py', 'Python')])
#    submit = SubmitField("Send")



# class Todo(object):
#     def __init__(self, todo_id, todo_title):
#         self.todo_id = todo_id
#         self.todo_title = todo_title

# api.add_resource(Todo, '/todos/<int:todo_id>')

# @app.route('/getcookie')
# def getcookie():
#    name = request.cookies.get('userID')
#    return '<h1>welcome '+name+'</h1>'

# @app.route('/logout')
# def logout():
#    # remove the username from the session if it is there
#    session.pop('username', None)
#    return redirect(url_for('index'))
