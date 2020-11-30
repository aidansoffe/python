# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# @app.route("/add")
# def do_add():
#     """Add a and b parameters."""

#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     result = add(a, b)

#     return str(result)

    #http://127.0.0.1:5000/add?a=2&b=3 this is what you enter on link

# @app.route("/sub")
# def do_sub():
#     """Subtract and b parameters."""

#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     result = sub(a, b)

#     return str(result)
#http://127.0.0.1:5000/sub?a=5&b=3 this is what you enter on link


# @app.route("/mult")
# def do_mult():
#     """Multiply a and b parameters."""

#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     result = mult(a, b)

#     return str(result)
#http://127.0.0.1:5000/mult?a=5&b=3 this is what you enter on link

# @app.route("/div")
# def do_div():
#     """Divide a and b parameters."""

#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     result = div(a, b)

#     return str(result)

#http://127.0.0.1:5000/div?a=5&b=3 this is what you enter on link

### PART TWO of this solution

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)

    #its the same but shortened version of all math operator above