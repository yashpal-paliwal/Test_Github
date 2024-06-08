from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        base_url = request.form.get('base_url')
        username = request.form.get('username')
        password = request.form.get('password')
        package_name = request.form.get('package_name')
        file = request.files.get('file')
        print("base_url: "+base_url)
        print("username: "+username)
        print("password: "+password)
       
        # Now you can use these variables in your application
        # For example, you might want to save the file or use the other data in some way
        return "POST request handled", 200
    else:
        return redirect(url_for('render_main_page', name='index.html'))

@app.route('/<name>', methods=['GET'])
def render_main_page(name=None):
    if name == 'index.html':
        return render_template('index.html', name=name)
    else:
        return "Page not found", 404

if __name__ == '__main__':
   app.run(debug=True,port=5001)
