from flask import Flask, render_template, request, escape
import mysql.connector

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the request in a database"""

    _DBCONFIG = {'user': 'vsearch',
                 'password': 'vsearchpasswd',
                 'host': 'hfrey.de',
                 'database': 'vsearchlogDB'}

    conn = mysql.connector.connect(**_DBCONFIG)
    cursor = conn.cursor()

    _SQL = """insert into log (phrase, letters, ip, browser_string, results)
              values
              (%s, %s, %s, %s, %s)"""
    cursor.execute(_SQL, (req.form['phrase'], req.form['letters'], req.remote_addr, req.user_agent.browser, res, ))

    cursor.close()
    conn.commit()
    conn.close()


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form["phrase"]
    letters = request.form["letters"]
    result = str(lettersCheck(phrase, letters))
    log_request(request, result)
    return render_template('results.html',
                           the_title="Ergebnisse ihrer Suche!",
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=result)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title="Wilkommen zur Webversion von letterSearch!")


def lettersCheck(phrase: str, letters: str = 'aeiou') -> set:
    return set(letters).intersection(set(phrase))  # Check for intersection


@app.route('/cv')
def cvPage() -> 'html':
    return render_template('cv.html')


@app.route('/viewlog')
def log_page() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote Address', 'User Agent', 'Results')
    return render_template('viewlog.html',
                           the_data=contents,
                           the_row_titles=titles,
                           the_title='View Logs')


if __name__ == '__main__':
    app.run(debug=True, port=80)
