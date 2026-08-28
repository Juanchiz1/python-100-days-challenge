from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    blog_url = "https://api.npoint.io/674f5423f73deab1e9a7" 
    response = requests.get(blog_url)
    all_posts = response.json()
    
    
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:index>')
def show_post(index):
    blog_url = "https://api.npoint.io/674f5423f73deab1e9a7"
    response = requests.get(blog_url)
    all_posts = response.json()
    
    
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == index:
            requested_post = blog_post
            break
            
    return render_template("post.html", post=requested_post)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = requests.request.form["message"]
        
       
        print(f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")
        
        
        return render_template("contact.html", msg_sent=True)
    
    
    return render_template("contact.html", msg_sent=False)