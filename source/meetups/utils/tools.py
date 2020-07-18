from meetups.core.database import get_session
from meetups.utils.mocks import MEETUPS, USERS, ADMINS, ROLES
from meetups.models.meetup import Meetup
from meetups.models.user import User
from meetups.models.meetup_user import MeetupUser
from meetups.models.role import Role
from meetups.models.user_role import UserRole

def generate_mocks(dsn):
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
            for user in users:
                meetup.users.append(user)
            db_session.add(meetup)
            db_session.commit()
            db_session.refresh(meetup)
            meetups.append(meetup)