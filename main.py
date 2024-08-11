from flask import Flask, request, render_template, redirect, url_for, session
import psycopg2

app = Flask(__name__)

app.secret_key = 'your_secret_key'

# Подключение к базе данных

@app.route("/")
def index():
    return redirect(url_for('authorization'))

@app.route("/authorization", methods=["GET", "POST"])
def authorization():
    dbname = 'pem'
    user = 'postgres'
    password = '1234'
    host = 'localhost'
    port = '5432'
    if request.method == "POST":


        try:
            # Подключение к базе данных
            conn = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port
            )
            username = request.form.get("loginLabel")
            password = request.form.get("passwordLabel")
            # Создание курсора
            cur = conn.cursor()
            print(username, password)
            # Выполнение SQL-запроса для проверки пользователя
            cur.execute("SELECT * FROM form WHERE username=%s AND password=%s", (username, password))
            user = cur.fetchone()

            # Закрытие курсора и соединения
            cur.close()
            conn.close()

            if user:
                session['username'] = username
                return redirect(url_for('home_page'))
            else:
                return render_template('authorization.html', msg='Invalid username or password')

        except Exception as e:
            return f"Ошибка: {e}"

    return render_template('authorization.html', msg='')

@app.route("/home-page")
def home_page():
    if 'username' in session:
        return render_template('home-page.html', username=session['username'])
    else:
        return redirect(url_for('authorization'))

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('authorization'))

if __name__ == "__main__":
    app.run(debug=True)