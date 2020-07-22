from datetime import datetime
import random

from meetups.core.database import get_session
from meetups.models.meetup import Meetup
from meetups.models.user import User
from meetups.models.meetup_user import MeetupUser
from meetups.models.role import Role
from meetups.models.user_role import UserRole

MEETUPS = [
    {"name": "after-agosto", "description": "After terraza", "date": datetime(2020, 8, 24, 17, 45)},
    {"name": "fin-2020", "description": "Fiesta fin de año", "date": datetime(2020, 12, 20, 20, 30)},
    {"name": "despedida-ale", "description": "Birras despedida Ale", "date": datetime(2020, 7, 19, 17, 30)},
    {"name": "bienvenida-equipo", "description": "Bienvenida a nuevos integrantes al equipo", "date": datetime(2020, 8, 3, 17, 55)},
    {"name": "after-septiembre", "description": "After Puerto Madero", "date": datetime(2020, 9, 4, 18, 30)}
]

USERS = [
    {"name": "user", "email": "user@mail.com", "password": "user"},
    {"name": "sol", "email": "sol@mail.com", "password": "sol"},
    {"name": "nico", "email": "nico@mail.com", "password": "nico"},
    {"name": "ale", "email": "ale@mail.com", "password": "ale"},
    {"name": "manu", "email": "manu@mail.com", "password": "manu"},
    {"name": "carlos", "email": "carlos@mail.com", "password": "carlos"},
    {"name": "pedro", "email": "pedro@mail.com", "password": "pedro"},
    {"name": "juan", "email": "juan@mail.com", "password": "juan"},
    {"name": "ana", "email": "ana@mail.com", "password": "ana"},
    {"name": "flor", "email": "flor@mail.com", "password": "flor"}
]

ADMINS = [
    {"name": "admin", "email": "admin@mail.com", "password": "admin"},
    {"name": "mario", "email": "mario@mail.com", "password": "mario"}
]

ROLES = [
    {"name": "admin"},
    {"name": "user"}
]

def generate_mocks(dsn):
    try:
        with get_session(dsn) as db_session:
            roles = []
            users = []
            admins = []
            meetups = []

            for role in ROLES:
                role = Role(**role)
                db_session.add(role)
                db_session.commit()
                db_session.refresh(role)
                roles.append(role)

            for user in ADMINS:
                admin = User(**user)
                admin.roles.append(roles[0])
                admin.roles.append(roles[1])
                db_session.add(admin)
                db_session.commit()
                db_session.refresh(admin)
                admins.append(admin)

            for user in USERS:
                user = User(**user)
                user.roles.append(roles[1])
                db_session.add(user)
                db_session.commit()
                db_session.refresh(user)
                users.append(user)

            for meetup in MEETUPS:
                meetup = Meetup(**meetup)
                for user in random.sample(users, k=random.randrange(1, len(users)+1)):
                    meetup.users.append(user)
                db_session.add(meetup)
                db_session.commit()
                db_session.refresh(meetup)
                meetups.append(meetup)
    except:
        pass
