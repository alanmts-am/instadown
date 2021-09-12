# Insta Down

Aqui temos o sistema que baixa posts do Instagram de determinados perfils listados em determinados arquivos

Podem ser baixados arquivos de determinadas data de inicio e fim ou todos os dados.

## Post por data (down_by_date.py)

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

## Todos os Posts (down_all.py)

Aqui temos o download de todos os posts salvos em determinados perfil

Vale apenas a configuração do arquivo profiles.txt

## Motor de Busca

### Instaloader 
[Manual](https://instaloader.github.io/) - 
[Github](https://github.com/instaloader/instaloader)