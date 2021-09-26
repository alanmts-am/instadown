# Insta Down

Aqui temos o sistema que baixa posts do Instagram de determinados perfis listados ou não em determinado arquivo.

Podem ser baixados de determinadas datas de inicio e fim ou todos os dados.

## Variáveis de ambiente

Aqui precisamos rodar o programa em linha de comando com os argumentos. Veja o exemplo abaixo:
```Shell
py {CAMINHO_DO_ARQUIVO}/insta_down.py --post --profile instagram --idate 01/01/2021 --fdate 31/07/2021 --download-dir D:\User\Example\Images\Instagram
```
```MarkDown
Entendendo cada argumento:
  --post ou --story -> indica o tipo de download a ser feito 
  --profile -> indicar um perfil específico para realizar o download. Caso não informado, buscará do arquivo padrão
  --idate -> data inicial dos posts
  --fdate -> data final dos posts
  --download-dir -> pasta onde os download serão salvos. Caso não fornecido, será usada a pasta padrão

Outros comandos:
  --user -> usuário
  --pass -> senha
  --profile-file -> arquivo onde serão buscados os perfis. Caso não informado, será usado o arquivo padrão
```

Alguns argumentos precisam ser passados em conjunto para o resultado desejado. Veremos mais abaixo em seus tópicos

## Arquivo de perfis

Aqui precisaremos que você informe primeiramente alguns dados em um arquivo:
* profiles.txt
  
OBS: este é nome padrão do arquivo de usuários. Para informar um arquivo diferente, basta usar o argumento --profile-file
```Shell
py {CAMINHO_DO_ARQUIVO}/insta_down.py --post --profle-file teste.txt --idate 01/01/2021 --fdate 10/01/2021
```

É importante que o arquivo seja do tipo txt e que cada usuário seja posto em uma linha, caso contrário, o programa pode não funcionar devidamente

```Python
USERNAME1
USERNAME2
USERNAME2
...
```

Estas informações serão usadas mais a frente pelos comandos

## Todos os post

Aqui temos o comando onde podem ser gerados todos os posts de um determinado perfil, apenas reunindo os argumentos

Por exemplo:
```Shell
py {CAMINHO_DO_ARQUIVO}/insta_down.py --post --profile instagram
```

Já quando quisermos gerar os posts de todos os perfis listados no arquivo profiles, basta omitir o argumento --profile

Por exemplo, basta informar apenas o tipo:
```Shell
py {CAMINHO_DO_ARQUIVO}/insta_down.py --post
```

## Todos os post por data

Aqui temos o comando onde podem ser gerados todos os posts em determinado periodo de um perfil

Por exemplo, basta o tipo, perfil e os argumentos de data:
```Shell
py {CAMINHO_DO_ARQUIVO}/insta_down.py --post --profile instagram --idate 01/01/2021 --fdate 10/01/2021
```

Já a situação onde seja necessário buscar através da lista de perfis, basta omitir o argumento --profile:
```Shell
py {CAMINHO_DO_ARQUIVO}/insta_down.py --post --idate 01/01/2021 --fdate 10/01/2021
```

## Mover arquivos

Por padrão, todas as pastas são salvas em 'files', cada uma em seu respectivo user.

Caso deseje informar um novo arquivo para onde as imagens devam ir, basta utilizar o argumento --download-dir
```Shell
py {CAMINHO_DO_ARQUIVO}/insta_down.py --post --idate 01/01/2021 --fdate 10/01/2021 --download-dir example
```

## Stories 

A funcionalidade segue os mesmos moldes do que já se vem sendo visto, necessitando agora da inserção de usuário e senha além do argumento --story ao invés de --post.

Para os casos onde os mesmos serão extraídos do arquivo profiles:
```Shell
py {CAMINHO_DO_ARQUIVO}/insta_down.py --story --username teste --password abcd1234
```

Já quando necessitar informar perfil específico, basta inserir o argumento --profile
 ```Shell
py {CAMINHO_DO_ARQUIVO}/insta_down.py --story --profile instagram --username teste --password abcd1234
```

Perceba que os stories não há verificação temporal devido a sua natureza de ficar visualizavel por 24h
## Motor de Busca

Todos os créditos devem ser dados ao módulo Python do projeto instaloader.  
Nosso projeto é apenas uma lógica mais direta da ideia inicial.
### Instaloader Links
[Manual](https://instaloader.github.io/) - 
[Github](https://github.com/instaloader/instaloader)