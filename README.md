# Insta Down

Aqui temos o sistema que baixa posts do Instagram de determinados perfils listados em determinados arquivos

Podem ser baixados arquivos de determinadas data de inicio e fim ou todos os dados.

## Post por data (down_posts_by_date.py)

Aqui precisaremos que você informe alguns dados em dois arquivos:
* date.txt
* profiles.txt

Para o primeiro arquivo, é preciso que informe a data inicial da busca. A data final sempre será a data atual, de hoje.
Padrão da data:
```Python
DIA/MES/ANO
```

Após a busca, o sistema sobrescreve a data do arquivo com a atual, para manter uma sequência de downloads

OBS: a busca por datas específicas está em desenvolvimento

Para o segundo arquivo, você deve informar os dados de usuário da plataforma e pasta de destino do download daquele perfil, seguindo o padrão:

```Python
USERNAME;DIRECTORY
```
Por exemplo:
```Python
instagram;C://User//Teste//Downloads//Instagram
```

## Todos os Posts (down_all_posts.py)

Aqui temos o download de todos os posts salvos em determinados perfil

Vale apenas a configuração do arquivo profiles.txt

## Stories (down_stories.py)

Para baixar os stories de uma conta, é preciso indicar o seu usuário e senha para que o processo possa ocorrer. Existe duas formas de fazer isso:
* Arquivo .env (Variável de ambiente)
* Ao lançar o arquivo, com argumentos

OBS: os profiles das contas ficarão salvos no arquivo profiles.txt

### .env

O arquivo vem com a indicação de duas variáveis para ser inserida:
```Python
USERNAME = 'USERNAME'
PASSWORD = 'PASSWORD'
```

Quando o arquivo for rodado sem argumentos, ele buscará os dados destas variáveis

### Variáveis de ambiente

Aqui precisamos rodar o programa em linha de comando com os argumentos. Veja o exemplo abaixo:
```Python
{CAMINHO_DO_ARQUIVO}/down_stories.py -u teste -p abcd1234
```
Perceba os argumentos passados:
* -u ou -user -> usuário
* -p ou -pass -> senha
## Arquivos baixados

Os arquivos baixados ficarão na pasta raiz do projeto com os nomes dos usuários. 
Para move-los, basta rodar o arquivo move_files.py. O mesmo usará o destino informado no segundo parametro do arquivo profiles.txt

## Motor de Busca

### Instaloader 
[Manual](https://instaloader.github.io/) - 
[Github](https://github.com/instaloader/instaloader)