from flask import Flask, request, jsonify, render_template, json
import numpy

server = Flask(__name__)

@server.route('/')
def hello():
    return jsonify({"response": "I changed the response"})

@server.route('/another')
def another():
    return jsonify({"response": "This is another response"})


@server.route('/square_root', methods=['POST'])
def sq_root():
    '''
    Square root of input number
    '''
    
    # Get the input JSON
    input_data = request.form
    input_number =input_data.to_dict()

    number = float(list(input_number.keys())[0])
    square_root = numpy.sqrt(number)
    return jsonify({'The square root is': float(square_root)}), 201


if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=5000)
