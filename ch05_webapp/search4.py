from flask import Flask, render_template, request, escape

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


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


@app.route('/viewlog')
def log_page() -> str:
    return escape(open('vsearch.log').read())


if __name__ == '__main__':
    app.run(debug=True, port=80)
