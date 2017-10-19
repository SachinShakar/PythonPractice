from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<user>')
def index(user=None):
    return render_template("user.html", user=user)

@app.route('/shopping')
def shopping():
    myList = ["Cheese", "bread", "Butter", "Milk"]
    return render_template("shopping.html", list=myList)

@app.route('/about')
def about():
    return "<h2> This is about page </h2>"

@app.route('/profiles/<username>')
def profile(username):
    return render_template("profile.html", name=username)

@app.route('/posts/<int:post_id>')
def posts(post_id):
    return "<h2> This is post for %s </h2>" % post_id

@app.route('/methods', methods = ['GET', 'POST'])
def methods():
    if (request.method == 'POST'):
        return ("You requested using method POST")
    else:
        return ("You requested using method GET")

if __name__ == "__main__":
    app.run(debug=True)
