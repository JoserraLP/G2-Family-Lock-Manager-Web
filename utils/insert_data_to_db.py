import datetime

from ..models import User, Role
from werkzeug.security import generate_password_hash

def insert_user_data(db):
    ''' Insert data in the database

        Parameters:
            db (object): database instance

    '''

    try:
        # ------- User ------- #

        user = User(
            email = "admin@admin.com",
            password = generate_password_hash("admin", method='sha256'),
            name = "admin",
            # Necessary to redirect to authorized views
            email_confirmed_at=datetime.datetime.utcnow()
        )

        user.roles.append(Role(name='admin'))

        db.session.add(user)

        user = User(
            email = "family@family.com",
            password = generate_password_hash("admin", method='sha256'),
            name = "family",
            # Necessary to redirect to authorized views
            email_confirmed_at=datetime.datetime.utcnow()
        )

        user.roles.append(Role(name='family'))

        db.session.add(user)

        db.session.commit()
    except Exception as e:
        print(e)