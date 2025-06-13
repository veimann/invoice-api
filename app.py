from flask import Flask, jsonify

app = Flask(__name__)

invoices = [
    {"id": 1, "customer": "ACME Corp", "amount": 1200.50, "status": "open"},
    {"id": 2, "customer": "Beta LLC", "amount": 875.00, "status": "open"},
    {"id": 3, "customer": "Gamma Inc", "amount": 540.00, "status": "paid"}
]

@app.route('/invoices')
def get_all_invoices():
    return jsonify(invoices)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
