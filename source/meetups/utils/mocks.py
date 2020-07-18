from datetime import datetime
from werkzeug.security import generate_password_hash

MEETUPS = [
    {"name": "after-agosto", "description": "After terraza", "date": datetime(2020, 8, 24, 17, 45)},
    {"name": "fin-2020", "description": "Fiesta fin de año", "date": datetime(2020, 5, 6, 20, 30)},
    {"name": "despedida-ale", "description": "Birras despedida Ale", "date": datetime(2020, 7, 21, 17, 30)},
    {"name": "bienvenida-equipo", "description": "Bienvenida a nuevos integrantes al equipo", "date": datetime(2020, 8, 3, 17, 55)},
    {"name": "after-septiembre", "description": "After Puerto Madero", "date": datetime(2020, 9, 4, 18, 30)}
]

USERS = [
    {"name": "user", "email": "user@mail.com", "password_hash": generate_password_hash("user")},
    {"name": "sol", "email": "sol@mail.com", "password_hash": generate_password_hash("sol")},
    {"name": "nico", "email": "nico@mail.com", "password_hash": generate_password_hash("nico")},
    {"name": "ale", "email": "ale@mail.com", "password_hash": generate_password_hash("ale")},
    {"name": "manu", "email": "manu@mail.com", "password_hash": generate_password_hash("manu")},
    {"name": "carlos", "email": "carlos@mail.com", "password_hash": generate_password_hash("carlos")},
    {"name": "pedro", "email": "pedro@mail.com", "password_hash": generate_password_hash("pedro")},
    {"name": "juan", "email": "juan@mail.com", "password_hash": generate_password_hash("juan")},
    {"name": "ana", "email": "ana@mail.com", "password_hash": generate_password_hash("ana")},
    {"name": "flor", "email": "flor@mail.com", "password_hash": generate_password_hash("flor")}
]

ADMINS = [
    {"name": "admin", "email": "admin@mail.com", "password_hash": generate_password_hash("admin")},
    {"name": "mario", "email": "mario@mail.com", "password_hash": generate_password_hash("mario")}
]

ROLES = [
    {"name": "admin"},
    {"name": "user"}
]