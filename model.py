colleges = [
    {'name': 'Baruch College',
    'gpa': 90.8, 
    'sat': 1350
    },
    {'name': 'Brooklyn College',
    'gpa': 89.0, 
    'sat': 1230
    },
    {'name': 'The Sophie Davis Biomedical Education Program/CUNY School of Medicine',
    'gpa': 94.0, 
    'sat': 1430
    },
    {'name': 'Hunter College',
    'gpa': 90.1, 
    'sat': 1300
    },
    {'name': 'Lehman College',
    'gpa': 87.2, 
    'sat': 1120
    },
    {'name': 'Macaulay Honors College',
    'gpa': 94.4, 
    'sat': 1460
    },
    {'name': 'New York City College of Technology',
    'gpa': 81.3, 
    'sat': 1010
    },
    {'name': 'Medgar Evers College',
    'gpa': 79.3, 
    'sat': 910
    },
    {'name': 'The City College of New York',
    'gpa': 89.8, 
    'sat': 1250
    },
    {'name': 'College of Staten Island',
    'gpa': 88.4, 
    'sat': 1160
    },
    {'name': 'John Jay College of Criminal Justice',
    'gpa': 88.3, 
    'sat': 1130
    },
    {'name': 'Queens College',
    'gpa': 89.2, 
    'sat': 1210
    },
    {'name': 'York College',
    'gpa': 82.5, 
    'sat': 1040
    },
    {'name': 'Bourough of Manhattan Community College',
    'gpa': 78.5, 
    'sat': 0
    },
    {'name': 'Bronx Community College',
    'gpa': 77.5, 
    'sat': 0
    },
    {'name': 'LaGuardia Community College',
    'gpa': 77.7, 
    'sat': 0
    },
    {'name': 'Guttman Community College',
    'gpa': 73.8, 
    'sat': 0
    },
    {'name': 'Hostos Community College',
    'gpa': 75.7, 
    'sat': 0
    },
    {'name': 'Kingsborough Community College',
    'gpa': 76.3, 
    'sat': 0
    },
    {'name': 'Queensborough Community College',
    'gpa': 76.2, 
    'sat': 0
    },
]


def college_finder(grade, score):
    empty = []
    for college in colleges:
        if float(grade) >= college['gpa'] and float(score) >= college['sat']:
            empty.append(college['name'])
    return empty
