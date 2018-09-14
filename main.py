from flask import Flask, render_template, request, redirect, url_for
import os
import caesar
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def landing(encryption=None):
    return render_template('index.html', encryption=encryption)


@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():

    encryption = request.form.get('encryption', None)
    if request.method == "POST":
        if encryption:
            return render_template(
                'index.html',
                encryption=caesar.encrypt_value(
                    encryption
                    )
                )
        else:
            return render_template(
                'index.html',
            )
    else:
        return render_template('index.html',encryption='')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(
        host='0.0.0.0',
        port=port,
        debug=True,
    )