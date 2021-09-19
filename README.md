# Insta Down

Aqui temos o sistema que baixa posts do Instagram de determinados perfis listados ou não em determinado arquivo.

Podem ser baixados de determinadas datas de inicio e fim ou todos os dados.

## Variáveis de ambiente

Aqui precisamos rodar o programa em linha de comando com os argumentos. Veja o exemplo abaixo:
```Python
{CAMINHO_DO_ARQUIVO}/insta_down.py -u teste -p abcd1234
```
```Shell
Perceba os argumentos passados:
  --post ou --story -> indica o tipo de download a ser feito 
  --user ou -u -> usuário
  --pass ou -p -> senha
  --idate ou -id -> data inicial do post
  --fdate ou -fd -> data final do post
  --profile -> indicar um perfil específico para realizar o download
```

Alguns argumentos precisam ser passados em conjunto para o resultado desejado. Veremos mais abaixo em seus tópicos

## Arquivo de perfis

Aqui precisaremos que você informe primeiramente alguns dados em um arquivo:
* profiles.txt

Para isso, você deve informar os dados de usuário da plataforma e pasta de destino do download daquele perfil, seguindo o padrão:

```Python
USERNAME;DIRECTORY
```
Por exemplo:
```Python
instagram;C://User//Teste//Downloads//Instagram
```

Estas informações serão usadas mais a frente pelos comandos

## Todos os post

Aqui temos o comando onde podem ser gerados todos os posts de um determinado perfil, apenas reunindo os argumentos

Por exemplo:
```Shell
{CAMINHO_DO_ARQUIVO}/insta_down.py --post --profile instagram
```

Já quando quisermos gerar os posts de todos os perfis listados no arquivo profiles, basta omitir o argumento --profile

Por exemplo, basta informar apenas o tipo:
```Shell
{CAMINHO_DO_ARQUIVO}/insta_down.py --post
```

## Todos os post por data

Aqui temos o comando onde podem ser gerados todos os posts em determinado periodo de um perfil

Por exemplo, basta o tipo, perfil e os argumentos de data:
```Shell
{CAMINHO_DO_ARQUIVO}/insta_down.py --post --profile instagram --idate 01/01/2021 --fdate 10/01/2021
```

Já a situação onde seja necessário buscar através da lista de perfis(profiles.txt), basta omitir o argumento --profile:
```Shell
{CAMINHO_DO_ARQUIVO}/insta_down.py --post --idate 01/01/2021 --fdate 10/01/2021
```

## Mover arquivos

Aqui, usaremos o segundo item do arquivo de perfis, onde serão enviadas as fotos geradas pelo programa.

Elas se reunen na pasta 'files' da raiz

O arquivo move_files usará o caminho informado no arquivo para realizar o processo
```Shell
{CAMINHO_DO_ARQUIVO}/move_files.py
```

## Stories

A funcionalidade está em desenvolvimento.
## Motor de Busca

Todos os créditos devem ser dados ao módulo Python do projeto instaloader.  
Este projeto é apenas uma lógica mais direta da ideia inicial.
### Instaloader Links
[Manual](https://instaloader.github.io/) - 
[Github](https://github.com/instaloader/instaloader)