#! /usr/bin/env python3

from mongoengine import *
import datetime
import string
import random

FirstNames    = 'FirstNames.txt'
MiddleNames   = 'MiddleNames.txt'
LastNames     = 'LastNames.txt'
CountyNames   = 'CountyNames.txt'
PlaceNames    = 'PlaceNames.txt'
StateNames    = 'StateNames.txt'
CountryNames  = 'CountryNames.txt'
CompanyNames  = 'CompanyNames.txt'

class Post(Document):
    first_name = StringField(required=True)
    middle_name = StringField(required=True)
    last_name = StringField(required=True)
    state_name = StringField(required=True)
    place_name = StringField(required=True)
    county_name = StringField(required=True)
    country_name = StringField(required=True)
    company_name = StringField(required=True)
    published = DateTimeField(default=datetime.datetime.now())

def randomLine(name_of_file):
    top_num = 0
    if name_of_file == 'FirstNames.txt':
        top_num = 10537
    if name_of_file == 'MiddleNames.txt':
        top_num = 59343
    if name_of_file == 'LastNames.txt':
        top_num = 32409
    if name_of_file == 'CountyNames.txt':
        top_num = 3136
    if name_of_file == 'PlaceNames.txt':
        top_num = 20580
    if name_of_file == 'StateNames.txt':
        top_num = 50
    if name_of_file == 'CountryNames.txt':
        top_num = 241
    if name_of_file == 'CompanyNames.txt':
        top_num = 4205
    rnd_num = random.randrange(0, top_num, 1)
    with open(name_of_file, 'r') as f:
        for i, line in enumerate(f, 1):
            if i == rnd_num:
                break
    # print(line)
    return str(line.strip('\n'))

# edit connect string as needed
connect(
    host='mongodb://mongodb-standalone-0.database:27017,mongodb-standalone-1.database:27017,mongodb-standalone-2.database:27017/xilinxtest?replicaSet=rs0',
    username='xilinxUser',
    password='Cisco123',
    authentication_source='xilinxtest'
)

i=1
while i<10:
    post_1 = Post(
        first_name = randomLine(FirstNames),
        middle_name = randomLine(MiddleNames),
        last_name = randomLine(LastNames),
        state_name = randomLine(StateNames),
        place_name = randomLine(PlaceNames),
        county_name = randomLine(CountyNames),
        country_name = randomLine(CountryNames),
        company_name = randomLine(CompanyNames),
        published = datetime.datetime.now()
    )
    post_1.save()       # This will perform an insert
    i+=1
disconnect()
