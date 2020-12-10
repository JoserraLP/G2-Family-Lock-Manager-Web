from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

import json
import requests

# location blueprint
location = Blueprint('location', __name__)

URL = 'https://muii-g2-api-location.herokuapp.com/location'

# -------------- location -------------- #

def create_location(request):
    ''' Create a location with the data inserted on the form

        Parameters:
            request (object): Request with the form data

        Returns:
            Redirect to main web server page.
    '''
    try: 
        # Get data from request
        data = request.form.to_dict()

        headers={'Content-type':'application/json', 'Accept':'application/json'}
 
        r = requests.post(URL, json = data, headers=headers)

        return redirect(url_for('main.index'))
    except requests.exceptions.RequestException as e:   
        raise SystemExit(e)

@location.route('/add_location', methods=['GET', 'POST'])
@login_required
def add_location():
    ''' Add a location to the system or show the form 

        Returns:
             Add location form page or show the location form depending on the request method
    '''

    # POST method -> create a location and store it
    if request.method == 'POST':
        return create_location(request)
    # GET method -> show add location  form
    else:
        return render_template('add_location.html')

@location.route('/get_all_locations', methods=['GET'])
@login_required
def get_all_locations():
    ''' Get all the locations in the system 

        Returns:
            All the locations in the system 
    '''

    r = requests.get(URL)

    results = r.json() ['historial']

    results.reverse()

    return render_template('show_all_locations.html', results=results)

@location.route('/get_location', methods=['GET'])
@login_required
def get_location():
    ''' Get last location of the user in the system 

        Returns:
            Last location of the user in the system 
    '''

    r = requests.get(URL+"/user")

    result = r.json()

    return render_template('show_last_location.html', result=result)