from flask import Flask, jsonify, request
app = Flask(__name__)

expenses = []

@app.route('/api/expenses', methods=['GET'])
def get_expenses():
    return jsonify(expenses)

@app.route('/api/expenses', methods=['POST'])
def add_expense():
    data = request.json
    expenses.append(data)
    return jsonify({'message': 'Expense added successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True)
