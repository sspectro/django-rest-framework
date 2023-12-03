# django-rest-framework
>Projeto Django REST Framework - Criação de API com django.
> 
>>Projeto desenvolvido no curso da Geek University - Udemy [Crie APIs REST com Python e Django REST Framework: Essencial](https://www.udemy.com/course/criando-apis-rest-com-django-rest-framework-essencial/)

## Ambiente de Desenvolvimento
Linux, Visual Studio Code, Docker e PostgreSQL

## Documentação
- [DJango](https://www.djangoproject.com/)
- [Django Versões](https://www.djangoproject.com/download/)
- Dica postgreSQL [vivaolinux](https://www.vivaolinux.com.br/artigo/psql-Conheca-o-basico)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Posgres dockerhub](https://hub.docker.com/_/postgres)

## Desenvolvimento

1. <span style="color:383E42"><b>Preparando ambiente</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    - Criar repositório no github com `gitignore` e `README.md`
    - Editar `README` e colocar estrutura básica
    - Criar diretório `readmeImages` e colocar imagens para uso no `README.md`
    - Editar `gitignore` e colocar configuração para `python, django, vscode/visualstudio code`
        >Use o site [gitignore.io](https://www.toptal.com/developers/gitignore/)

    - Criar e ativar ambiente virtual
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

    - Instalação do `Django LTS 3.2.23`
        ```bash
        pip install django==3.2.23
        ```




    </p>

    </details> 

    ---

2. <span style="color:383E42"><b>Criar container django-rest usando `POSTGRESQL` do `dockerhub`</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    - [Documentação dockerhub](https://hub.docker.com/_/postgres)
        - Baixar imagem POSTGRESQL
            ```bash
            docker pull postgres
            ```
        - Cria container 
        Nomeando `--name django-rest` 
        Adiciono informação da porta `-p 5432:5432`
        Informo a senha `POSTGRES_PASSWORD=suasenha`
        ```bash
        docker run -p 5432:5432 --name django-rest -e POSTGRES_PASSWORD=suasenha -d postgres

        ```

        - Iniciar container
            ```bash
            docker start django-rest
            ```
        - Verificar `id` container e `ip` do container
            ```bash
            sudo docker ps
            sudo docker container inspect idcontainer
            ```

        - Acessar container no modo interativo - Criação `database` - container em execução
            >Criação database e usuário
            ```bash
            sudo docker exec -it idcontainer bash
            ```
            - Acessando postgres `database` com usuário `postgres`
                ```bash
                psql -U postgres
                ```
            - Criar database
                ```bash
                create database "django-rest-db";
                ```
            -  Criar usuário no postgres
                ```bash
                create user cristiano superuser inherit createdb createrole password 'surasenha';
                ```

            - Saindo do postgres
                ```bash
                \q
                ```
            - Acessando database `django-rest-db`. Use o  `ip` do container
                >Comandos válidos
                ```bash
                psql -U postgres -d django-rest-db
                psql ipcontainer -U postgres -d django-rest-db

                psql -h ipcontainer -U postgres -d django-rest-db
                ```
            - Listando database
                ```bash
                \l
                ```
            - Sair do container
                ```bash
                exit
    
    </p>

    </details> 

    ---

3. <span style="color:383E42"><b>Criação Projeto `escola` e app `cursos` </b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    - Criação Projeto `escola` e app `cursos`
        ```bash
        django-admin startproject escola .
        django-admin startapp cursos
        ```
    
    - Inclusão do app `cursos`, timezone e configuração arquivos estáticos no arquivo settings.py
        App
        ```python
        INSTALLED_APPS = [
            #...
            'django.contrib.staticfiles',

            'cursos',
        ]
        ```

        Timezone
        ```python
        # Internationalization
        # https://docs.djangoproject.com/en/3.2/topics/i18n/

        LANGUAGE_CODE = 'pt-br'

        TIME_ZONE = 'America/Sao_Paulo'

        USE_I18N = True

        USE_L10N = True

        USE_TZ = True
        ```

        Arquivos estáticos
        ```python
        # Static files (CSS, JavaScript, Images)
        # https://docs.djangoproject.com/en/3.1/howto/static-files/

        STATIC_URL = '/static/'
        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
        MEDIA_URL = 'media/'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        ```

    </p>

    </details> 

    ---


## Meta
><span style="color:383E42"><b>Cristiano Mendonça Gueivara</b> </span>
>
>>[<img src="readmeImages/githubIcon.png">](https://github.com/sspectro "Meu perfil no github")
>
>><a href="https://linkedin.com/in/cristiano-m-gueivara/"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> 
>
>>[<img src="https://sspectro.github.io/images/cristiano.jpg" height="25" width="25"> - Minha Página Github](https://sspectro.github.io/#home "Minha Página no github")<br>



><span style="color:383E42"><b>Licença:</b> </span> Distribuído sobre a licença `Software Livre`. Veja Licença **[MIT](https://opensource.org/license/mit/)**.