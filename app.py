from flask import Flask, request, render_template

app = Flask(__name__)


def read_words():
    with open('words.txt', 'r') as file:
        return file.read().split("\n")


def levenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2 + 1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        max_distance = int(request.form['max_distance'])

        words_list = read_words()
        data = ' '.join(text.splitlines())

        D = {}

        for word in data.split(" "):
            para = "".join([x for x in word if x.isalnum()])
            if para.lower() in words_list:
                continue
            else:
                b = []
                for crt in words_list:
                    if crt[:1] == para[:1]:
                        r = levenshteinDistance(crt, para.lower())
                        if r <= max_distance:
                            b.append(crt)
                            D[para] = b

        if len(D) == 0:
            return render_template('index.html', message="CONGRATS NO ERROR FOUND!", text=text)

        return render_template('index.html', corrections=D, text=text)

    return render_template('index.html')


@app.route('/update_text', methods=['POST'])
def update_text():
    original_text = request.form['original_text']
    corrections = request.form.getlist('correction')

    for correction in corrections:
        if correction:
            incorrect, correct = correction.split(':')
            original_text = original_text.replace(incorrect, correct)

    return render_template('index.html', message="CONTENT UPDATED!", text=original_text, corrected_text=original_text)


if __name__ == '__main__':
    app.run(debug=True)
