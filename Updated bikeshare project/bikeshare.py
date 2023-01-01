import time
import pandas as pd
import numpy as np
import datetime
import os


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_city():

    """We shall start with getting the city"""

    city = str()

    print('\nHello! Let\'s explore US bikeshare dataset!\n')
    
    while True:
        
        city = input('Which city would you like to learn more about? Chicago, New york city or Washington?\n- ').lower()
        print('-'*40)
        
        try:
            assert(city == 'chicago' or city == 'new york city' or city == 'washington')
            break
        
        except AssertionError:
            print("\nSorry, we have no information about {}! Please make sure your spelling is correct and that you have chosen one of the metioned cites.".format(city))
      
    return city


def load_data(city):
    
    """Next we will load and add some data"""
    
    citybikeshare = pd.read_csv(CITY_DATA[city])
    
    citybikeshare["Start Time"] = pd.to_datetime(citybikeshare["Start Time"])
    #citybikeshare["year"] = citybikeshare["Start Time"].dt.year
    citybikeshare["month"] = citybikeshare["Start Time"].dt.month
    citybikeshare["day"] = citybikeshare["Start Time"].dt.day
    citybikeshare["hour"] = citybikeshare["Start Time"].dt.hour
    
    return citybikeshare


def data_filter(df):

    """Then we will apply some filters"""

    choice = input("\nWould you like to filter the data? Enter(y) if yes and any other key if no: ").lower()

    if choice == 'y':
        s_month = 0
        e_month = 0
        s_day = 0
        e_day = 0
        s_hour = 0
        e_hour = 0
        
        choice = input("\nWould you like to filter by month? Enter(y) if yes and any other key if no: ").lower()
        
        if choice == 'y':
            while True:
                s_month = int(input("\nFrom: "))
                try:
                    assert(s_month >= 1 and s_month <= 12)
                    break
                
                except AssertionError:
                    print("\nPlease make sure you choose a number from 1 -> 12!")

            while True:
                e_month = int(input("\nTo: "))
                if e_month >= s_month:
                    try:
                        assert(e_month >= 1 and e_month <= 12)
                        break
                
                    except AssertionError:
                        print("\nPlease make sure you choose a number from 1 -> 12!")
                
                else:
                    print("\nPlease make sure you choose a month bigger than or equal to the start month!")

            df = df[(df.month >= s_month) & (df.month <= e_month)]

        choice = input("\nWould you like to filter by day? Enter(y) if yes and any other key if no: ").lower()

        if choice == 'y':
            while True:
                s_day = int(input("\nFrom: "))
                try:
                    assert(s_day >= 1 and s_day <= 31)
                    break
                
                except AssertionError:
                    print("\nPlease make sure you choose a number from 1 -> 31!")

            while True:
                e_day = int(input("\nTo: "))
                if e_day >= s_day:
                    try:
                        assert(e_day >= 1 and e_day <= 31)
                        break
                
                    except AssertionError:
                        print("\nPlease make sure you choose a number from 1 -> 31!")
                
                else:
                    print("\nPlease make sure you choose a day bigger than or equal to the start day!")

            df = df[(df.day >= s_day) & (df.day <= e_day)]

        choice = input("\nWould you like to filter by hour? Enter(y) if yes and any other key if no: ").lower()

        if choice == 'y':
            while True:
                s_hour = int(input("\nFrom: "))
                try:
                    assert(s_hour >= 0 and s_hour <= 23)
                    break
                
                except AssertionError:
                    print("\nPlease make sure you choose a number from 0 -> 23!")

            while True:
                e_hour = int(input("\nTo: "))
                if e_hour >= s_hour:
                    try:
                        assert(e_hour >= 0 and e_hour <= 23)
                        break
                
                    except AssertionError:
                        print("\nPlease make sure you choose a number from 0 -> 23!")
                
                else:
                    print("\nPlease make sure you choose an hour bigger than or equal to the start hour!")

            df = df[(df.hour >= s_hour) & (df.hour <= e_hour)]

    return df


def time_data(df):

    """Here we will calculate time related information"""

    somelist = list()

    most_common_month = int()
    m_no_of_repetitions = 0

    m_repetitions = df.pivot_table(columns=['month'], aggfunc='size')
   
    for i, v in m_repetitions.items():
        if m_no_of_repetitions < v:
            m_no_of_repetitions = v
            most_common_month = i

    if most_common_month == 1:
        most_common_month = str('January')
    elif most_common_month == 2:
        most_common_month = str('February')
    elif most_common_month == 3:
        most_common_month = str('March')
    elif most_common_month == 4:
        most_common_month = str('April')
    elif most_common_month == 5:
        most_common_month = str('May')
    elif most_common_month == 6:
        most_common_month = str('June')
    elif most_common_month == 7:
        most_common_month = str('July')
    elif most_common_month == 8:
        most_common_month = str('August')
    elif most_common_month == 9:
        most_common_month = str('September')
    elif most_common_month == 10:
        most_common_month = str('October')
    elif most_common_month == 11:
        most_common_month = str('November')
    else:
        most_common_month = str('December')


    most_common_day = str()
    d_no_of_repetitions = 0

    d_repetitions = df.pivot_table(columns=['day'], aggfunc='size')
     
    for i, v in d_repetitions.items():
        if d_no_of_repetitions < v:
            d_no_of_repetitions = v
            most_common_day = i


    most_common_hour = int()
    h_no_of_repetitions = 0
        
    h_repetitions = df.pivot_table(columns=['hour'], aggfunc='size')
     
    for i, v in h_repetitions.items():
        if h_no_of_repetitions < v:
            h_no_of_repetitions = v
            most_common_hour = i


    somelist.append("The most common month is: {}. Number of bike rides is: {}.\n".format(most_common_month,m_no_of_repetitions))
    somelist.append("The most common day of the is: {}. Number of bike rides is: {}.\n".format(most_common_day,d_no_of_repetitions))
    somelist.append("The most common hour is: {}. Number of bike rides is: {}.".format(most_common_hour,h_no_of_repetitions))

    return str(somelist[0])+str(somelist[1])+str(somelist[2])


def stations_data(df):

    """Here we will calculate information related to stations and trips"""

    somelist = list()

    most_common_start = str()
    s_no_of_repetitions = 0
    
    s_repetitions = df.pivot_table(columns=['Start Station'], aggfunc='size')
    
    for i, v in s_repetitions.items():
        if s_no_of_repetitions < v:
            s_no_of_repetitions = v
            most_common_start = i


    most_common_end = str()
    e_no_of_repetitions = 0
    
    e_repetitions = df.pivot_table(columns=['End Station'], aggfunc='size')
    
    for i, v in e_repetitions.items():
        if e_no_of_repetitions < v:
            e_no_of_repetitions = v
            most_common_end = i


    df['arrow'] = " -> "
    df['Start and End'] = df['Start Station']+df['arrow']+df['End Station']

    most_common_start_end = str()
    s_e_no_of_repetitions = 0
    
    s_e_repetitions = df.pivot_table(columns=['Start and End'], aggfunc='size')
    
    for i, v in s_e_repetitions.items():
        if s_e_no_of_repetitions < v:
            s_e_no_of_repetitions = v
            most_common_start_end = i


    somelist.append('The most frequented Start Station is: {}. Number of customers is: {}.\n'.format(most_common_start,s_no_of_repetitions))
    somelist.append('The most frequented End Station is: {}. Number of customers is: {}.\n'.format(most_common_end,e_no_of_repetitions))
    somelist.append('The most frequented trip is: {}. Number of customers is: {}.'.format(most_common_start_end,s_e_no_of_repetitions))

    return str(somelist[0])+str(somelist[1])+str(somelist[2])


def mean_and_sum(df):

    """Here we will calculate the mean and sum"""

    somelist = list()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()/60
    total = round(total,2)

    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean()/60
    mean = round(mean,2)


    somelist.append('The total time taken through out all trips is: {} minutes.\n'.format(total))
    somelist.append('The average duration of a trip is: {} minutes.'.format(mean))

    return str(somelist[0])+str(somelist[1])


def users_info(df,city):

    """Here we will calculate some information about the users"""

    somelist = list()

    count_of_user_type = df.pivot_table(columns=['User Type'], aggfunc='size')

    somelist.append(count_of_user_type);

    # TO DO: Display counts of gender
    if not city == 'washington':
        females = len(df[(df.Gender == "Female")])
        males = len(df[(df.Gender == "Male")])
    
        somelist.append("\nNumber of known female customers: {}\nNumber of male customers: {}\n".format(females,males))

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min(skipna=True)
        most_recent = df['Birth Year'].max(skipna=True)
        
        birthyear_count = df.pivot_table(columns=['Birth Year'], aggfunc='size')
        
        most_common_birthyear = str()
        b_no_of_repetitions = 0
        
        for i, v in birthyear_count.items():
            if b_no_of_repetitions < v:
                b_no_of_repetitions = v
                most_common_birthyear = int(i)
                
        somelist.append("Earliest year of birth is: {}\nMost recent year of birth is: {}\nMost common year of birth is: {}".format(earliest,most_recent,most_common_birthyear))

        return str(somelist[0])+str(somelist[1])+str(somelist[2])

    return str(somelist[0])

def all_info():

    city = get_city()

    df = load_data(city)
    df = data_filter(df)

    time_list = time_data(df)
    station_list = stations_data(df)
    mean_and_sum_list = mean_and_sum(df)
    users_info_list = users_info(df,city)

    os.system('cls')

    print("\nInformation about the most common month, day and hour:\n")
    print(time_list,"\n",'-'*40)

    print("\nInformation about the most popular stations and trip:\n")
    print(station_list,"\n",'-'*40)

    print("\nInformation about the mean and sum:\n")
    print(mean_and_sum_list,"\n",'-'*40)

    print("\nInformation about the customers:\n")
    print(users_info_list,"\n",'-'*40)


def some_info():

    city = get_city()

    df = load_data(city)
    df = data_filter(df)

    time_list = time_data(df)
    station_list = stations_data(df)
    mean_and_sum_list = mean_and_sum(df)
    users_info_list = users_info(df,city)

    while True:
        
        temp = False
        os.system('cls')
        choice = input("\nWhat would you like to see?\n\n- For info about month, day and hour Enter(t):\n- For info about the most popular stations and trip Enter(s):\n- For info about the mean and sum Enter (m):\n- For info about the customers Enter(c):\n- ").lower()

        if choice == 't':
            print("Information about the most common month, day and hour:\n")
            print(time_list,"\n",'-'*40)
        elif choice == 's':
            print("\nInformation about the most popular stations and trip:\n")
            print(station_list,"\n",'-'*40)
        elif choice == 'm':
            print("\nInformation about the mean and sum:\n")
            print(mean_and_sum_list,"\n",'-'*40)
        elif choice == 'c':
            print("\nInformation about the customers:\n")
            print(users_info_list,"\n",'-'*40)
        else:
            input("No such choice! Enter any key to restart.")
            temp = True

        if not temp:
            choice  = input("Would you like to view some more info? Enter(y) if yes and another key if no: ").lower()

            if not choice == 'y':
                break
            

x = True
  
while x:

    os.system('cls')    
    
    hello = input("\nWould you like to display some information or all information? Enter(s) for some and any other key for all: ")
    hello.lower()

    os.system('cls')
    
    if hello == 's':
        some_info()
    else:
        all_info()
   
    userinterface = input("\nWould you like to restart the program? Enter(y) if yes and any other key if no: ").lower()
    
    if userinterface != 'y':
        x = False
            

