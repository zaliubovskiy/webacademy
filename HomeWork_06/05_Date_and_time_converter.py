# Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
# Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
# Your task is simple - convert the input date and time from computer format into a "human" format.

# It feels like the code may be optimized, but not sure how exactly
def date_time(time: str) -> str:
    # Separate date from time
    separated = list(time.split())
    my_date = separated[0]
    my_time = separated[1]

    # Separate each item to the correct variable
    date_split = list(my_date.split("."))
    day = int(date_split[0])
    month = int(date_split[1])
    year = int(date_split[2])

    time_split = list(my_time.split(":"))
    hours = int(time_split[0])
    minutes = int(time_split[1])

    # Define singularity or plurality of the words "hour" and "minute"
    if hours == 1:
        str_hours = "hour"
    else:
        str_hours = "hours"

    if minutes == 1:
        str_minutes = "minute"
    else:
        str_minutes = "minutes"

    # Define dictionary for months
    month_name = {1: "January",
                  2: "February",
                  3: "March",
                  4: "April",
                  5: "May",
                  6: "June",
                  7: "July",
                  8: "August",
                  9: "September",
                  10: "October",
                  11: "November",
                  12: "December"}

    # Collect everything into one string
    human_date = f"{day} {month_name[month]} {year} year {hours} {str_hours} {minutes} {str_minutes}"

    return human_date


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))