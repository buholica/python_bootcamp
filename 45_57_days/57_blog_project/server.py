from flask import Flask, render_template
import requests
from post import Post

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
blog_posts = response.json()

post_list = []
for post in blog_posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_list.append(post_obj)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", all_posts=post_list)


@app.route('/post/<int:blog_id>')
def read_post(blog_id):
    requested_post = None
    for blog_post in post_list:
        if blog_post.id == blog_id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
