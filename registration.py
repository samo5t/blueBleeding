from flask import Flask, request, render_template, Blueprint

app = Flask(__name__)


@app.route("/register", methods=["GET"])
def register():
    # username = request.form.get("username")
    # password = request.form.get("password")
    #
    # # Добавьте свой код для обработки регистрации

    return render_template('RegistrationWindow.html', msg='')

if __name__ == "__main__":
    app.run()