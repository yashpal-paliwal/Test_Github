from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/', methods=['GET'])
@app.route('/<name>', methods=['GET'])
def render_main_page(name=None):
    if name == 'index.html':
        return render_template('index.html', name=name)
    else:
        return "Page not found", 404

if __name__ == '__main__':
   app.run(debug=True,port=5001)
