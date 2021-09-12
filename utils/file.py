def get_initial_date(file):
    with open(file, 'r') as file:
        dates = file.readlines()
        for date in dates:
            return date

def write_new_date(file, new_date):
    with open(file, 'w') as file:
        file.write(new_date)
        