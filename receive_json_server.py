#!/usr/bin/env python

from flask import Flask, jsonify, render_template, Response, request
import json

app = Flask(__name__)
app.debug = True


@app.route('/')
def main_page():
    return render_template("index.html")


@app.route('/form', methods=['POST'])
def receive_json_form():

    print('You are here!!')
    payload = (request.form)

    print('Printing request:', payload)

    print('Name: -', payload['name'])
    print('Email: -', payload['email'])
    print('Password: -', payload['password'])
    print('Username: -', payload['username'])

    rtr_data = {'val1' : 'FirstValue',
                'val2' : 'SecondValue',
                'val3' : 'ThirdValue'
                }


    resp = json.dumps(rtr_data)
    return Response(resp, status=200, mimetype='application/json')


app.run(host='10.55.16.10', port=8082)

