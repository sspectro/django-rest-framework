# django-rest-framework
>Projeto Django REST Framework - Criação de API com django.
> 
>>Projeto desenvolvido no curso da Geek University - Udemy [Crie APIs REST com Python e Django REST Framework: Essencial](https://www.udemy.com/course/criando-apis-rest-com-django-rest-framework-essencial/)

## Ambiente de Desenvolvimento
Linux, Visual Studio Code, Docker e PostgreSQL

## Documentação
- [DJango](https://www.djangoproject.com/)
- Dica postgreSQL [vivaolinux](https://www.vivaolinux.com.br/artigo/psql-Conheca-o-basico)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Posgres dockerhub](https://hub.docker.com/_/postgres)

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



    </p>

    </details> 

    ---

2. <span style="color:383E42"><b>Criar container fusion-postgres usando `POSTGRESQL` do `dockerhub`</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    - [Documentação dockerhub](https://hub.docker.com/_/postgres)
        - Baixar imagem POSTGRESQL
            ```bash
            docker pull postgres
            ```
        - Cria container 
        Nomeando `--name fusion-postgres` 
        Adiciono informação da porta `-p 5432:5432`
        Informo a senha `POSTGRES_PASSWORD=suasenha`
        ```bash
        docker run -p 5432:5432 --name django-rest -e POSTGRES_PASSWORD=suasenha -d postgres

        ```

        - Iniciar container
            ```bash
            docker start fusion-postgres
            ```
        - Verificar `id` container e `ip` do container
            ```bash
            sudo docker ps
            sudo docker container inspect idcontainer
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