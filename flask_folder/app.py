#extensions that allow specific classes and functions

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

@app.route("/katy")
def katy_page():
    return render_template("katy.html", favourite_thing = "fish")


@app.route("/pets")
def pet_page():
    return render_template("pets.html", pets=["Truffles","Ray","Coconut","Dad Degu","Baby Degu","Horrible","Bjorn","Ragnar","Floki"])



                #########################################################
                #                                                       #
                #                  Redirects Pages                      #                     
                #                                                       #
                #########################################################

@app.route("/home")
def home_redirect():
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