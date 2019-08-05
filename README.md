
# ClickCall
O objetivo da Clickcall é projetar uma interface disruptiva a fim de melhorar a experiência do usuário no sistema e tornar os clientes da Ligue Comunicações mais orientados as métricas que o sistema proporciona.

## Primeiros passos
Siga estes passos caso queira ter uma cópia do projeto configurada e executando no seu host local para propósitos de desenvolvimento e testes. Veja a seção `Realizando Deploy` para entender como fazer a instalação em um ambiente de produção.

### Requisitos
- Python 3
- Pip
- Virtualenv
- Pipenv


## Instalação em ambiente de desenvolvimento
Após clonar e acessar a pasta raiz do repositório

### Windows
Instale o python3, pip e virtualenv na sua máquina e garanta que todos estejam sendo reconhecidos como variáveis de ambiente - "PATH"

Abra o terminal na pasta clonada e crie uma pasta para conter seu projeto e acesse-o:

```
mkdir clickcall
cd clickcall
```

Crie um ambiente virtual usando o virtualenv e ative-o:

```
virtualenv env
C:\(path_de_onde_você_está)>virtualenv\env\Scripts\activate
```

Aparecerá isto na sua linha de comando:

```
(env) C:\(path_de_onde_você_está)>
```

Instale as demais dependências do projeto:

```
cd ClickCall
pip install -r requirements.txt
```

Agora aplique as migrações e rode o projeto localmente:

```
python magane.py makemigrations
python magane.py migrate
python magane.py runserver
```

Esse processo só precisa ser feito uma vez por máquina. Depois disso, caso queira abrir o projeto outrora, basta ativar o ambiente virtual com o comando de ativação do virtualenv, e usar o comando ```python magane.py runserver```

Finalizando, acesse em seu browser o seguinte endeço:
```http://localhost:8000/```

Quando finalizar o projeto, basta desativar o virtualenv: ```deactivate``` Ou fechar o cmd prompt.

### Linux (Ubuntu)
Caso não possua, instale as dependências:

```
sudo apt install python python3 python-pip virtualenv && sudo pip install pipenv 
```

Abra o terminal na pasta clonada e crie um ambiente virtual usando o pipenv:

```
pipenv --python 3
```

Após isso, instale as dependências necessárias ao projeto ClickCall:

```
pipenv install
```

Para ativar o ambiente virtual, basta fazê-lo também pelo pipenv com o comando `pipenv shell`. Se tudo tiver sido configurado com sucesso, basta aplicar as migrações com 

```
python manage.py migrate
``` 
exportar as seguintes variáveis de ambiente:
- `DJANGO_SECRET_KEY`, que deve receber como valor uma [chave secreta](https://www.miniwebtool.com/django-secret-key-generator/) para o Django;
- `EMAIL_HOST_ACCOUNT`, que deve receber como valor uma conta de email para ser utilizada no [templated_email](https://djangopackages.org/packages/p/django-templated-email/);
- `EMAIL_HOST_PASSWORD`, que deve receber como valor a senha da conta de email. (se tiver problemas com email, veja [isso](http://citi.org.br/library/learning/3ipytWKuZJuB50WcJ3rp))

*Protip: Você pode colocar as variáveis em um arquivo `.env` e elas serão carregadas ao ativar o ambiente virtual*

e iniciar o servidor de desenvolvimento com 

```
python manage.py runserver
``` 
### PRs
Em inglês, segundo o seguinte padrão:
```markdown
# Additions
- add navbar
- add color mixins
# How to test?
Open `locahost:8000/test` and see the styles
```
## Populando o DB:
* Rode o projeto e vá para a url:
```
localhost:8000/activities/populate-db/
```
* Aguarde pois o processo demora. Quando o povoamento terminar, irá aparecer uma mensagem no browser.

## Realizando Deploy
### Heroku
Para realizar deploy na Heroku, basta criar um novo app, configurar as mesmas variáveis de ambiente na aba `settings`, colocando também a variável `DJANGO_SETTINGS_MODULE` com valor `clickcall.settings.production` e associar a este repositório na aba de `deploy`.

## Ferramentas de Build
* [Pipenv](https://github.com/pypa/pipenv) - Python Development Workflow for Humans
* [Django](https://www.djangoproject.com/) - The Web framework for perfectionists with deadlines
* [Heroku](https://www.heroku.com) - Cloud Application Platform

## Autores
* **Arthur Henrique** - *Gerente* - [ahtlc](https://github.com/ahtlc)
* **Júnior Mendes** - *Desenvolvimento* - [jrmmendes](https://github.com/jrmmendes)
* **Eulália Aires** - *Desenvolvimento* - [eulaliaaires](https://github.com/eulaliaaires)
* **Marco Santana** - *Desenvolvimento* - [marcoafsantana](https://github.com/marcoafsantana)
* **Eduarda Senna** - *Desenvolvimento* - [dudasenna](https://github.com/dudasenna)
* **Carolina Vieira** - *Mockup*

```markdown
Made with </> and love by CITi
```
