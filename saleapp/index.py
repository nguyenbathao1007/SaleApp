from flask import Flask, render_template, request
import dao
from saleapp.dao import load_categories, load_products

app = Flask(__name__)


@app.route("/")
def index():
    q = request.args.get("q")
    print(q)
    cates = load_categories()
    products = load_products(Q=q)
    return render_template("index.html", cates=cates, products=products)


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
