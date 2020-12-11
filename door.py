from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from flask_user import roles_required

import json
import requests

# Door blueprint
door = Blueprint('door', __name__)

URL = 'https://muii-g2-api-door.herokuapp.com/door'

# -------------- Door -------------- #

def create_door(request):
    ''' Create a door with the data inserted on the form

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

@door.route('/add_door', methods=['GET', 'POST'])
@roles_required(['admin'])
def add_door():
    ''' Add a door to the system or show the form 

        Returns:
             Add door form page or show the door form depending on the request method
    '''

    # POST method -> create a door and store it
    if request.method == 'POST':
        return create_door(request)
    # GET method -> show add door  form
    else:
        return render_template('add_door.html')

@door.route('/get_door', methods=['GET'])
@login_required
def get_door():
    ''' Get all the doors in the system 

        Returns:
            All the doors in the system 
    '''

    r = requests.get(URL)

    results = r.json() ['doors']

    return render_template('show_doors.html', results=results)

def remove_door(request):
    ''' Remove a door with the data inserted on the form 

        Parameters:
            request (object): Request with the form data

        Returns:
            Redirect to main web server page.
    '''
    try: 
        # Get data from request
        data = request.form.to_dict()

        results = requests.get(URL).json() ['doors']

        door = [door for door in results if door['name'] == data['name']][0]

        if (door):
            r = requests.delete(URL+'/'+str(door['id']))

        return redirect(url_for('main.index'))
    except requests.exceptions.RequestException as e:   
        raise SystemExit(e)

@door.route('/delete_door', methods=['GET', 'POST'])
@roles_required(['admin'])
def delete_door():
    ''' Delete a door to the system or show the form 

        Returns:
             Delete door form page or show the door form depending on the request method
    '''

    # POST method -> delete a door and store it
    if request.method == 'POST':
        return remove_door(request)
    # GET method -> show add door  form
    else:
        return render_template('delete_door.html')

def update_value_door(request):
    ''' Update a door with the data inserted on the form 

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

@door.route('/update_door', methods=['GET', 'POST'])
@roles_required(['admin'])
def update_door():
    ''' Update a door to the system or show the form 

        Returns:
             Update door form page or show the door form depending on the request method
    '''

    # POST method -> delete a door and store it
    if request.method == 'POST':
        return update_value_door(request)
    # GET method -> show add door  form
    else:
        return render_template('update_door.html')
