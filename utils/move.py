import shutil
import os
    
def move_posts(source_dir, target_dir):
    file_names = os.listdir(source_dir)
    
    for file_name in file_names:
        try:
            shutil.move(os.path.join(source_dir, file_name), target_dir)
        except:
            print('Arquivo ' + file_name + ' já se encontra na pasta')
    
    try:
        os.rmdir(source_dir)
    except:
        print('Alguns arquivos que tentamos mover já se encontram na pasta de destino. Por favor, verificar os dados da pasta destino antes de mover')