sun_count = 0
days_in_year = 365
days_in_leap_year = 366
year_tracker = 1901

first_day_of_months = [1,32,60,91,121,152,182,213,244,274,305,335]
first_day_of_months_leap_year = [1,32,61,92,122,153,183,214,245,275,306,336]

sunday_tracker = 6 #First Sunday date in 1901

while (year_tracker < 2001):
    if not year_tracker % 4:
        while(sunday_tracker <= 366):
            if(sunday_tracker in first_day_of_months_leap_year):
                sun_count +=1
            sunday_tracker += 7 
        sunday_tracker = sunday_tracker % 366
    else:
        while(sunday_tracker <= 365):
           if(sunday_tracker in first_day_of_months):
               sun_count +=1
           sunday_tracker += 7
        sunday_tracker = sunday_tracker % 365
    year_tracker +=1

print sun_count
