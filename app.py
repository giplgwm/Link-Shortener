import sqlite3
import random
import string

from flask import Flask, redirect, request


app = Flask(__name__)

def get_db():
    db = sqlite3.connect('shortener.db')
    db.row_factory = sqlite3.Row
    return db

def insert_to_db(original_url, short_code):
    db = get_db()
    db.execute('INSERT INTO urls (original_url, short_code) VALUES (?, ?)', (original_url, short_code))
    db.commit()

def get_link_from_shortcode(shortcode):
    db = get_db()
    result = db.execute('SELECT original_url FROM urls WHERE short_code = ?', (shortcode, )).fetchone()
    return result

def is_already_in_db(link):
    db = get_db()
    result = db.execute('SELECT short_code FROM urls WHERE original_url = ?', (link, )).fetchone()
    return result

def get_shortcode():
    chars = string.ascii_lowercase + string.digits
    shortcode = ''.join(random.choice(chars) for _ in range(8))
    return shortcode

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['url']
        db_check = is_already_in_db(original_url)
        if db_check:
            short_code = db_check['short_code']
            return f"This link is already in the DB! " + request.host_url + short_code
        shortcode = get_shortcode()
        insert_to_db(original_url, shortcode)
        short_url = request.host_url + shortcode
        return f'Shortened URL: <a href="{short_url}">{short_url}</a>'
    else:
        return '''
        <form method="post">
            URL to shorten: <input type="url" name="url" required>
            <input type="submit" value="Shorten">
        </form>
    '''


@app.route('/<shortcode>')
def redirect_user_to_stored_link(shortcode):
    row = get_link_from_shortcode(shortcode)
    if row:
        link = row['original_url']
    else:
        return "CODE NOT FOUND", 404
    return redirect(link)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)