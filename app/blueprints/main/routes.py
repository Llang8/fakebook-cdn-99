from . import bp as app
from flask import render_template

# Routes that return JSON
user_data = { # Mock database data
    'lucasl': {
        'user_id': 0,
        'name': 'Lucas',
        'favoriteColor': 'blue',
        'posts': [
            {
                'id': 0,
                'title': 'This is post 1',
                'body': 'This is the text for the post'
            },
            {
                'id': 1,
                'title': 'This is post 2',
                'body': 'This is the text for the post'
            },
            {
                'id': 2,
                'title': 'This is post 3',
                'body': 'This is the text for the post'
            }
        ]
    },
    'christophert': {
        'user_id': 1,
        'name': 'Christopher',
        'favoriteColor': 'orange',
        'posts': [
            {
                'id': 3,
                'title': 'This is post 4',
                'body': 'This is the text for the post'
            },
            {
                'id': 4,
                'title': 'This is post 5',
                'body': 'This is the text for the post'
            },
            {
                'id': 5,
                'title': 'This is post 6',
                'body': 'This is the text for the post'
            }
        ]
    },
    'joelc': {
        'user_id': 2,
        'name': 'Joel',
        'favoriteColor': 'red',
        'posts': [
            {
                'id': 6,
                'title': 'This is post 7',
                'body': 'This is the text for the post'
            },
            {
                'id': 7,
                'title': 'This is post 8',
                'body': 'This is the text for the post'
            },
            {
                'id': 8,
                'title': 'This is post 9',
                'body': 'This is the text for the post'
            }
        ]
    }
}

# Routes that return/display HTML
logged_in_user = user_data['joelc']

@app.route('/')
def home():
    cars = [
        {
            "name": "Maruti Swift Dzire VDI",
            "year": 2014,
            "selling_price": 450000
        },
        {
            "name": "Skoda Rapid 1.5 TDI Ambition",
            "year": 2014,
            "selling_price": 370000
        },
        {
            "name": "Honda City 2017-2020 EXi",
            "year": 2006,
            "selling_price": 158000
        }
    ]

    return render_template('home.html', user=logged_in_user, cars=cars)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')