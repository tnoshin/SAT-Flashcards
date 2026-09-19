from csv import DictReader
from flask import Flask, render_template

app = Flask(__name__)


def load_cards():
    with open('vocab.csv','r', encoding='utf-8-sig') as file:
        csv_reader = DictReader(file)
        flashcards = []

        for r in csv_reader:
            flashcards.append(r)
    return flashcards

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', cards=load_cards()) 

if __name__ =='__main__':
    app.run() 
