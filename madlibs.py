"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return render_template("landing_page.html")


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form(): 
    """Play game"""

    game_status = request.args.get("game_status")

    if game_status == "Yes": 
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

@app.route('/madlib', methods=["POST"])
def show_madlib():
    """Show result of madlib form"""

    color = request.form.get("color")
    noun = request.form.get("noun")
    adjective = request.form.get("adjective")
    person = request.form.get("person")
    place = request.form.get("place")
    emotion = request.form.get("emotion")
    number = int(request.form.get("number"))

    num_range = range(1, number+1)

    view_madlib = choice(["final_madlib.html", "final_madlib2.html"])

    return render_template(view_madlib, color=color, 
        noun=noun, adjective=adjective, person=person, place=place, 
        emotion=emotion, number=number, num_range=num_range) 


 


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
