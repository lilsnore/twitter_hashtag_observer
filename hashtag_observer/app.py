from flask import Flask, jsonify, request, render_template
from hashtag_observer.provider import HashtagRequest

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template("layout.html")

@app.route('/images')
def get_urls():
    hashtag = str(request.args.get("hashtag"))
    num_img = int(request.args.get("num_img"))

    req = HashtagRequest(hashtag, pages=2)
    return jsonify(req.get_urls(num_img))


def run():
    app.run(debug=True)


if __name__ == '__main__':
    run()
