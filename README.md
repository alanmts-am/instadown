# InstaDown

Aqui temos o sistema que baixa posts do Instagram de determinados perfis listados ou não em determinado arquivo.

Podem ser baixados de determinadas datas de inicio e fim ou todos os dados.

## Funcionalidades

- [x] Baixar de perfis públicos
- [x] Baixar por datas especificadas
- [x] Baixar de diversos perfis informados em arquivos
- [ ] Baixar stories [provável]
- [ ] Baixar de contas privadas com login [remoto]
- [ ] Analytics; estatísticas de perfis [provável]

## Argumentos de comando

Aqui precisamos rodar o programa em linha de comando com os argumentos. Veja o exemplo abaixo:
```Shell
python {CAMINHO_DO_ARQUIVO}/instadown.py --post --profile instagram --idate 2024-01-01 --fdate 2024-01-31 --download-dir D:\User\Example\Images\Instagram
```
O exemplo acima fará a download dos posts do perfil do Instagram entre as datas 01/01/2024 e 31/01/2024, além de mover os resultados para o caminho "D:\User\Example\Images\Instagram"
```MarkDown
Entendendo cada argumento:
  --post -> indica o tipo de download a ser feito 
  --profile -> indicar um perfil específico para realizar o download. Caso não informado, buscará do arquivo padrão
  --idate -> data inicial dos posts
  --fdate -> data final dos posts
  --target -> pasta onde os download serão salvos. Caso não fornecido, será usada a pasta padrão

Outros comandos:
  --today -> Informa a data atual para os campos de idate e fdate
  --file -> arquivo onde serão buscados os perfis. Caso não informado, será usado o arquivo padrão
```

Alguns argumentos precisam ser passados em conjunto para o resultado desejado. Veremos mais abaixo em seus tópicos

## Arquivo de perfis

Aqui precisaremos que você informe primeiramente alguns dados em um arquivo:
* profiles.json
  
OBS: este é nome padrão do arquivo de usuários. Para informar um arquivo diferente, basta usar o argumento --file  
OBS2: Caso este não tenha sido informado explicitamente pelos seu argumento --file, ele irá buscar o arquivo da raiz de onde esta sendo executado.
```Shell
python {CAMINHO_DO_ARQUIVO}/insta_down.py --post --file teste.json --idate 2024-01-01 --fdate 2024-01-10
```

É importante que o arquivo seja do tipo JSON e que cada usuário seja posto dentro do array "profiles".

```Json
{
    "profiles":[
        "user 1",
        "user 2",
        "user 3",
        ...
    ]
}
```

Estas informações serão usadas mais a frente pelos comandos.

## Todos os post

Aqui temos o comando onde podem ser gerados todos os posts de um determinado perfil, apenas reunindo os argumentos

Por exemplo:
```Shell
python {CAMINHO_DO_ARQUIVO}/insta_down.py --post --profile instagram
```

Já quando quisermos gerar os posts de todos os perfis listados no arquivo profiles, basta omitir o argumento --profile

Por exemplo, basta informar apenas o tipo:
```Shell
python {CAMINHO_DO_ARQUIVO}/insta_down.py --post
```

## Todos os post por data

Aqui temos o comando onde podem ser gerados todos os posts em determinado periodo de um perfil

Por exemplo, basta o tipo, perfil e os argumentos de data:
```Shell
python {CAMINHO_DO_ARQUIVO}/insta_down.py --post --profile instagram --idate 2024-01-01 --fdate 2024-01-10
```

Já a situação onde seja necessário buscar através da lista de perfis, basta omitir o argumento --profile:
```Shell
python {CAMINHO_DO_ARQUIVO}/insta_down.py --post --idate 2024-01-01 --fdate 2024-01-10
```

## Mover arquivos

Por padrão, todas as pastas são salvas em 'files', cada uma em seu respectivo user.

Caso deseje informar um novo arquivo para onde as imagens devam ir, basta utilizar o argumento --target
```Shell
python {CAMINHO_DO_ARQUIVO}/insta_down.py --post --idate 2024-01-01 --fdate 2024-01-10 --target example
```
## Motor de Busca

Todos os créditos devem ser dados ao módulo Python do projeto instaloader.  
Nosso projeto é apenas uma lógica mais direta da ideia inicial.
### Instaloader Links
[Manual](https://instaloader.github.io/) - 
[Github](https://github.com/instaloader/instaloader)