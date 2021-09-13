import os
import argparse
import dotenv

def import_variables():
    dotenv.load_dotenv(dotenv.find_dotenv('.env'))

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user', action='store', dest='username', default=os.getenv("USER"), help='Insira o seu usuário')
    parser.add_argument('-p', '--pass', action='store', dest='password', default=os.getenv("PASSWORD"), help='Insira a sua senha')
    args = parser.parse_args()

    return args