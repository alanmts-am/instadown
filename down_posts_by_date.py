from datetime import datetime
from src.posts import get_data_posts
from utils.create import create_directory
from utils.extract import extract_data
from utils.file import get_initial_date, write_new_date

DATE_FILE = 'date.txt'
PROFILES_FILE = 'profiles.txt'
INITIAL_DATE = get_initial_date(DATE_FILE)
FINAL_DATE = datetime.today().strftime('%d/%m/%Y')

listInitial = extract_data(INITIAL_DATE)
listFinal = extract_data(FINAL_DATE)
SINCE = datetime(int(listInitial[2]), int(listInitial[1]), int(listInitial[0]))
UNTIL = datetime(int(listFinal[2]), int(listFinal[1]), int(listFinal[0]))

with open(PROFILES_FILE, 'r') as file:
    line_itens = file.readlines()
    
for line_item in line_itens:
    line_list = line_item.split(';')

    create_directory(line_list[0])
    get_data_posts(line_list[0], line_list[0], SINCE, UNTIL)

write_new_date(DATE_FILE, FINAL_DATE)
