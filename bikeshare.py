import time
import pandas as pd
import numpy as np

# City data file to load
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Months filter selection
MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

# Days filter selection
DAYS = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city, month, day = 'chicago', 'january', 'monday'


    while city not in CITY_DATA:
        city = input("Please enter city to load data from: ").lower()

    # get user input for month (all, january, february, ... , june)
    while month not in MONTHS:
        month = input("Please enter month:").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while day not in DAYS:
        day = input("Please enter day of the week:").lower()



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    show_raw = None
    while show_raw not in ['yes', 'no']:
        show_raw = input("Show first 5 lines of raw data? yes/no:").lower()

    if show_raw == 'yes':
        print(df.head(5))

    # convert the Start Time column to to_datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        # use the index of the months list to get the corresponding int
        month_idx = MONTHS.index(month)

        # filter by month to create the new dataframe
        df =  df[df['month'] == month_idx]


     # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    print("Most common month: {}".format(df['month'].mode()[0]))

    # display the most common day of week
    print("Most common day of week: {}".format(df['day_of_week'].mode()[0]))

    # display the most common start hour
    print("Most common start hour: {}".format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most common start station: {}".format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print("Most common end station: {}".format(df['End Station'].mode()[0]))


    # display most frequent combination of start station and end station trip
    print("Most frequent combination of start and end station trip: {}".format((df['Start Station'] + df['End Station']).mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time (sec): {:.1f}".format(df["Trip Duration"].sum()))

    # display mean travel time
    print("Mean travel time (sec): {:.1f}".format(df["Trip Duration"].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].unique()

    for user in user_types:
        print("Counts of {} user: {}".format(user, df[df['User Type']== user].count()[0]))

    # Display counts of gender
    print("Counts of gender male: {}".format(df[df['Gender'] == 'Male'].count()[0]))
    print("Counts of gender female: {}".format(df[df['Gender'] == 'Female'].count()[0]))

    # Display earliest, most recent, and most common year of birth
    print("Earliest birth year {}".format(df['Birth Year'].min()))
    print("Most Recent birth year {}".format(df['Birth Year'].max()))
    print("Most common birth year {}".format(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        """Main program loop"""

        city, month, day = get_filters()

        print("{}, {}, {}".format(city, month, day))
        df = load_data(city, month, day)
        print("Load data success")

        # Display varies stats of the travel 
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # Run again if enter 'yes' otherwise quit
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
