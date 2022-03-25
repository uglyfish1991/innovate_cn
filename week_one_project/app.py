from flask import Flask, Blueprint, render_template, url_for, redirect

# a blueprint of the website structure

views = Blueprint(__name__, "views")

app = Flask(__name__)
# this is the prefix that distinguishes the pages
app.register_blueprint(views, url_prefix="/")

                #########################################################
                #                                                       #
                #                 Application Pages                     #                     
                #                                                       #
                #########################################################

# this is how the homepage is accessed
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/page1")
def page_one():
    return render_template("page1.html")

@app.route("/page2")
def page_two():
    return render_template("page2.html")

@app.route("/page3")
def page_three():
    return render_template("page3.html")

@app.route("/page4")
def page_four():
    return render_template("page4.html")

@app.route("/page5")
def page_five():
    return render_template("page5.html")




                #########################################################
                #                                                       #
                #                  Redirects Pages                      #                     
                #                                                       #
                #########################################################

@app.route("/home")
def home_redirect():
    return redirect(url_for("home"))

@app.route("/js")
def js_redirect():
    return redirect(url_for("home"))

@app.route("/javascript")
def javascript_redirect():
    return redirect(url_for("home"))


                #########################################################
                #                                                       #
                #                     Error Pages                       #                     
                #                                                       #
                #########################################################

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

                #########################################################
                #                                                       #
                #                 Initialising                          #                     
                #                                                       #
                #########################################################

if __name__ == "__main__":
    app.run(debug=True, port = 8000)