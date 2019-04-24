# _*_coding:utf-8_*_
# author：qq823947488
# date：2019/4/24 20:15


from  flask import request, render_template, Flask, redirect

from src.dao import user_dao

app = Flask(__name__)


@app.route("/")
def list_all_user():
    user_list = user_dao.list_all()
    return render_template('user_list.html', user_list=user_list)


@app.route('/add_form')
def show_add_form():
    return render_template('user_form.html')


@app.route("/add_user", methods=['POST'])
def add_user():
    username = request.form['username']
    password = request.form['password']
    user_dao.add(username, password)
    return redirect('/')


@app.route("/del/<id>")
def delete_user(id):
    user_dao.delete(id)
    return redirect('/')


if __name__ == '__main__':
    app.run(port=5555)
