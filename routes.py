from flask import Flask, render_template

def register_routes(app):

  @app.route("/")
  def homepage():
    return render_template("homepage.html")
