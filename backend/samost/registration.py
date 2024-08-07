from flask import Flask, request

app = Flask(__name__)


@app.route("/RegistrationWindow.html", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")

    # Добавьте свой код для обработки регистрации

    return "Регистрация успешно выполнена"


if __name__ == "__main__":
    app.run()