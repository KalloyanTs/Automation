def book_reader():
    page_counter = int(input("Enter total book pages[1 - 1000]: "))
    if 1 < page_counter > 1000:
        print("Invalid book pages!")
        return()
    pages_per_hour = int(input("How many pages per hour read[1 - 1000]: "))
    if 1 < pages_per_hour > 1000:
        print("Invalid pages per hour read!")
        return()   
    days_left = int(input("Days to read the book[1 - 1000]:"))
    if 1 < days_left > 1000:
        print("Invalid days left!")
        return()
    total_hours = float(page_counter/pages_per_hour)
    mins_per_day = float(total_hours/days_left)*60
    int_mins = int(mins_per_day)
    seconds_per_day = (mins_per_day % int_mins)*60
    int_secs = int(seconds_per_day)
    print(f"You need {int_mins} minutes and {int_secs} seconds per day to read the whole {page_counter} pages long book!")
book_reader()