from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from flask_user import roles_required

import json
import requests

# Legitimate person blueprint
legitimate_person = Blueprint('legitimate_person', __name__)

URL = 'https://muii-g2-api-legitimate.herokuapp.com/legitimate_person'

# -------------- Legitimate person -------------- #

def create_legitimate_person(request):
    ''' Create a legitimate person with the data inserted on the form

        Parameters:
            request (object): Request with the form data

        Returns:
            Redirect to main web server page.
    '''
    try: 
        # Get data from request
        data = request.form.to_dict()
        
        data ['notification'] = True if data['notification'] == 'true' else False

        headers={'Content-type':'application/json', 'Accept':'application/json'}
 
        r = requests.post(URL, json = data, headers=headers)

        return redirect(url_for('main.index'))
    except requests.exceptions.RequestException as e:   
        raise SystemExit(e)

@legitimate_person.route('/add_legitimate_person', methods=['GET', 'POST'])
@roles_required(['admin'])
def add_legitimate_person():
    ''' Add a legitimate person to the system or show the form 

        Returns:
             Add legitimate person form page or show the legitimate person form depending on the request method
    '''

    # POST method -> create a legitimate person and store it
    if request.method == 'POST':
        return create_legitimate_person(request)
    # GET method -> show add legitimate person  form
    else:
        return render_template('add_legitimate_person.html')

@legitimate_person.route('/get_legitimate_person', methods=['GET'])
@login_required
def get_legitimate_person():
    ''' Get all the legitimate people in the system 

        Returns:
            All the legitimate people in the system 
    '''

    r = requests.get(URL)

    results = r.json() ['legitimate']

    return render_template('show_legitimate_person.html', results=results)

def remove_legitimate_person(request):
    ''' Remove a legitimate person with the data inserted on the form 

        Parameters:
            request (object): Request with the form data

        Returns:
            Redirect to main web server page.
    '''
    try: 
        # Get data from request
        data = request.form.to_dict()

        r = requests.delete(URL+'/'+data['person_MAC'])

        return redirect(url_for('main.index'))
    except requests.exceptions.RequestException as e:   
        raise SystemExit(e)

@legitimate_person.route('/delete_legitimate_person', methods=['GET', 'POST'])
@roles_required(['admin'])
def delete_legitimate_person():
    ''' Delete a legitimate person to the system or show the form 

        Returns:
             Delete legitimate person form page or show the legitimate person form depending on the request method
    '''

    # POST method -> delete a legitimate person and store it
    if request.method == 'POST':
        return remove_legitimate_person(request)
    # GET method -> show add legitimate person  form
    else:
        return render_template('delete_legitimate_person.html')

def update_value_legitimate_person(request):
    ''' Update a legitimate person with the data inserted on the form 

        Parameters:
            request (object): Request with the form data

        Returns:
            Redirect to main web server page.
    '''
    try: 
        # Get data from request
        data = request.form.to_dict()

        headers={'Content-type':'application/json', 'Accept':'application/json'}

        r = requests.put(URL, json=data, headers=headers)

        return redirect(url_for('main.index'))
    except requests.exceptions.RequestException as e:   
        raise SystemExit(e)

@legitimate_person.route('/update_legitimate_person', methods=['GET', 'POST'])
@roles_required(['admin'])
def update_legitimate_person():
    ''' Update a legitimate person to the system or show the form 

        Returns:
             Update legitimate person form page or show the legitimate person form depending on the request method
    '''

    # POST method -> delete a legitimate person and store it
    if request.method == 'POST':
        return update_value_legitimate_person(request)
    # GET method -> show add legitimate person  form
    else:
        return render_template('update_legitimate_person.html')
