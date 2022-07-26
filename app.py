from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favirote_5')
def five_fav():
    top_five = [{'name': 'Walter Payton',
    'nickname': 'Sweetness',
    'img': 'https://www.sportscasting.com/wp-content/uploads/2020/06/Walter-Payton.jpg'},
    {'name': 'Derrick Henry', 'nickname': 'King Henry',
    'img': 'https://cdn-japantimes.com/wp-content/uploads/2021/01/np_file_61754.jpeg'},
    {'name': 'Kobe Bryant', 'nickname': 'Black Mamba',
    'img': 'https://m.media-amazon.com/images/I/81eoZPw2UuL._AC_SL1500_.jpg'},
    {'name': 'Steve McNair', 'nickname': 'Big Air McNair',
    'img': 'http://tshf.net/wp-content/uploads/2017/06/mcnair-and-mvp.jpg'},
    {'name': 'Dwayne Johnson', 'nickname': 'The Rock',
    'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTc51_asjmoJwKAJXD3DLpqEnM0DQmiEIjBAQ&usqp=CAU'}]
    return render_template('five_fav.html', five_top=top_five)

if __name__ == '__main__':
    app.run(debug=True)