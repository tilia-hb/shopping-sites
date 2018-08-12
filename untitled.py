from flask import Flask, render_template, redirect, flash, make_response, request
import jinja2

import melons

app = Flask(__name__)
app.secret_key = 'this-should-be-something-unguessable'
app.jinja_env.undefined = jinja2.StrictUndefined




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
