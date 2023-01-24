import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': " firebase url "
})

ref = db.reference('Students')

data = {
    "1006":
        {
            "name": "MIKE TYSON",
            "major": "BOXING",
            "starting_year": 1999,
            "total_attendance": 66,
            "standing": "G",
            "year": 99,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1007":
        {
            "name": "RDJ",
            "major": "IRON MAN",
            "starting_year": 1999,
            "total_attendance": 69,
            "standing": "G",
            "year": 99,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1002":
        {
            "name": "RONALDO",
            "major": "FOOTBALL",
            "starting_year": 1999,
            "total_attendance": 10,
            "standing": "A",
            "year": 99,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1003":
        {
            "name": "SACHIN TENDULKAR",
            "major": "Cricket",
            "starting_year": 1999,
            "total_attendance": 10,
            "standing": "10",
            "year": 100,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1004":
        {
            "name": "The Rock",
            "major": "WWE",
            "starting_year": 1999,
            "total_attendance": 22,
            "standing": "A",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1005":
        {
            "name": "JACKIE CHAN",
            "major": "MARTIAL ARTS",
            "starting_year": 1999,
            "total_attendance": 10,
            "standing": "10",
            "year": 77,
            "last_attendance_time": "2022-12-11 00:54:34"
        }

}

for key, value in data.items():
    ref.child(key).set(value)
print("added")
