from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/index.html')
# def index2():
#     return render_template('index.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/work.html')
# def work():
#     return render_template('work.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

@app.route('/<string:page_name>')
def html_pages(page_name):
    return render_template(page_name)

@app.route('/submit', methods=['POST', 'GET'])
def login():
    
    if request.method == 'POST':
        data=request.form.to_dict()
        print(data)
        return redirect('/thankyou.html')
    else:
      return 'Invalid username/password'
    