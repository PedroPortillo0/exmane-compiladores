
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def analyzer():
    if request.method == 'POST':
        input_text = request.form['input_text']
        items = process_input(input_text)
        return render_template('result.html', items=items)
    return render_template('index.html')

def process_input(input_text):
    items = []
    item_text = input_text.strip().split()
    if len(item_text) == 2:
        name = item_text[0]
        try:
            price = float(item_text[1])
            if price < 0:
                raise ValueError("Price cannot be negative")
        except ValueError:
            price = 0.0
        
        iva = round(price * 0.16, 2)
        total = round(price + iva, 2)
        items.append({'name': name, 'price': f"{price:.2f}", 'iva': f"{iva:.2f}", 'total': f"{total:.2f}"})
    return items

if __name__ == '__main__':
    app.run(debug=True)
