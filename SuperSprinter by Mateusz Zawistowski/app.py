from flask import Flask, render_template, url_for, request, redirect
import user_stories

app = Flask(__name__)


@app.route('/')
def index():
    dictionary_keys = user_stories.in_memory_dictionary_keys
    stories = user_stories.in_memory_user_stories
    return render_template("index.html", headers=dictionary_keys, stories=stories)


@app.route('/add', methods=["GET"])
def add_user_story_get():
    return render_template("edit_user_story.html", story=None)


@app.route('/add', methods=["POST"])
def add_user_story_post():
    data = dict(request.form)
    data["Status"] = "Planning"
    data["Id"] = user_stories.greatest_id() + 1
    user_stories.add_user_story(data)
    return redirect(url_for("index"))


@app.route('/edit/<user_story_id>', methods=["GET"])
def edit_user_story_get(user_story_id):
    if not user_story_id.isnumeric():
        return redirect(url_for("index"))

    user_story_id = int(user_story_id)
    story = user_stories.get_user_story(user_story_id)

    if story is None:
        return redirect(url_for("index"))

    return render_template("edit_user_story.html", story=story)


@app.route('/edit', methods=["POST"])
def edit_user_story_post():
    data = dict(request.form)
    data["Id"] = int(data["Id"])
    user_stories.update_user_story(data)

    return redirect(url_for("index"))




if __name__ == '__main__':
    app.run()
