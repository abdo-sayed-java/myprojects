from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

movies = ["Transporter", "Openheimer", "Arnator"]

@app.route("/")
def index():
    return render_template("index.html", movies=movies)

@app.route("/add", methods=["GET", "POST"])
def add_movie():
    if request.method == 'POST':
        movie = request.form["movie"]
        if movie:
            movies.append(movie)
            return redirect(url_for("index"))
    return render_template("addMovie.html")

@app.route("/delete/<int:movie_id>")
def delete_movie(movie_id):
    if 0 <= movie_id < len(movies):
        movies.pop(movie_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)