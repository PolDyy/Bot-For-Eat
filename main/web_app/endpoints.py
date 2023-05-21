from flask import render_template, request, session, jsonify
from flask import Flask
from pathlib import Path
from os import getenv
from dotenv import load_dotenv
from services.product import Product, Additive
from services.context import get_popup_header
from services.form_processing import add_product_form_processing
from forms import ProductForm


env_path = Path(__file__).parents[1].joinpath('.env')
load_dotenv(env_path)

app = Flask(__name__)
app.config["SECRET_KEY"] = getenv("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/product/add", methods=["POST"])
def add_product():
    form = ProductForm(request.form)

    result = add_product_form_processing(form)
    print(session.get('order'))
    return jsonify(result)


@app.context_processor
def context_processor():
    return dict(products=Product(),
                additive=Additive().get_additive(),
                exceptions=Additive().get_exceptions(),
                get_popup_header=get_popup_header,
                product_form=ProductForm(),
                )


if __name__ == "__main__":
    app.run(debug=True)


