from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

import json
import requests

# Historic blueprint
historic = Blueprint('historic', __name__)

URL = 'https://muii-g2-api-historic.herokuapp.com/historic'

# -------------- Historic -------------- #

@historic.route('/show_historic', methods=['GET'])
@login_required
def  show_historic():
    ''' Get all the legitimate people in the system 

        Returns:
            All the legitimate people in the system 
    '''

    r = requests.get(URL)

    results = r.json() ['historic']

    return render_template('show_historic.html', results=results)