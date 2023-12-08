# django-rest-framework
>Projeto Django REST Framework - Criação de API com django.
>Uso de container docker para o database.
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
- [Insomnia Rest](https://insomnia.rest/download)
- [Postman](https://www.postman.com/downloads/)
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

    - Instalação do `Django LTS 3.2.23` e `psycopg2-binary` 
        ```bash
        sudo apt update
        pip install django==3.2.23
        pip install psycopg2-binary
        ```

    - Criando `.env` variáveis de ambiente
        Instalação `dotenv`
        ```bash
        pip install python-dotenv
        ```
        .env
        ```python
        'SENHA_POSTGRESQL'='senha_postgresql'
        'USUARIO_POSTGRESQL'='username'
        'SECRET_SETTINGS'='secret_django'
        'POSTGRESQL_DB_NAME'='databasename'
        'HOST'='Host'
        ```

    - Inclusão `dotenv` em settings.py
        ```python
        from dotenv import load_dotenv
        load_dotenv()
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
                ```
    
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

4. <span style="color:383E42"><b>Criação dos Models e Inclusão ao Painel Admin</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    - Models em `models.py`
        ```python
        from django.db import models

        # Create your models here.
        class Base(models.Model):
            criacao = models.DateTimeField(auto_now_add=True)
            atualizacao = models.DateTimeField(auto_now=True)
            ativo = models.BooleanField(default=True)

            class Meta:
                abstract = True

        class Curso(Base):
            titulo = models.CharField(max_length=255)
            url = models.URLField(unique=True)

            class Meta:
                verbose_name = 'Curso'
                verbose_name_plural = 'Cursos'

            def __str__(self):
                return self.titulo
            
        class Avaliacao(Base):
            curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
            nome = models.CharField(max_length=255)
            email = models.EmailField()
            comentario = models.TextField(blank=True, default='')
            avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

            class Meta:
                verbose_name = 'Avaliação'
                verbose_name_plural = 'Avaliações'
                unique_together = ['email', 'curso'] # Somente 1 avaliação com mesmo curso e email

            def __str__(self):
                return f'{self.nome} avaliou o curso {self.curso} com nota {self.avaliacao}'
        ```

    - Models em `admin.py`
        ```python
        from django.contrib import admin

        from .models import Curso, Avaliacao


        @admin.register(Curso)
        class CursoAdmin(admin.ModelAdmin):
            list_display = ('titulo', 'url', 'criacao', 'atualizacao', 'ativo')

        @admin.register(Avaliacao)
        class AvaliacaoAdmin(admin.ModelAdmin):
            list_display = ('curso', 'nome', 'email', 'avaliacao', 'criacao', 'atualizacao', 'ativo')
        ```
    
    - Executar migração para criação das tabelas no banco de dados
        Gera os arquivos para migração/criação das tabelas
        ```bash
        python3 manage.py makemigrations
        ```

        Executar migração
        ```bash
        python3 manage.py migrate
        ```

    </p>

    </details> 

    ---

5. <span style="color:383E42"><b>Criar SuperUser Django e Instalar o DjangoRESTFramework, Markdown e django-filter</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    ```bash
    python3 manage.py createsuperuser
    ```

    - Testar
        ```bash
        python3 manage.py runserver
        ```

    - Cadastrar alguns cursos via painel admin
        `http://127.0.0.1:8000/admin/`
        Curoso:
        `Criação de APIs REST com Django REST Framework`
        `Programação para web com Django Framework`
        `Programação com JavaScript`
    
    - Criar avalições

    - Instalação djangorestframework
        ```bash
        pip install djangorestframework markdown django-filter
        ```

    - Criação arquivo requirements
    Contém informaçẽos sobre todas as bibliotecas utilizadas no projeto. Para atualizar o arquivo, basta executar o comando novamente após instalar outras bibliotecas.
        ```sh
        pip freeze > requirements.txt
        ```

    - Incluir rest_framework e django_filters ao settings.py
        ```python
        INSTALLED_APPS = [
            #...

            'django_filters',
            'rest_framework',

            'cursos',
        ]

        #...
        #...
        # DRF
        REST_FRAMEWORK = {
            'DEFAULT_AUTHENTICATION_CLASSES': (
                'rest_framework.authentication.SessionAuthentication',
            ),
            'DEFAULT_PERMISSION_CLASSES': (
                'rest_framework.permissions.IsAuthenticatedOrReadOnly',
            )
        }
        ```

    - Incluir url padrão do `djangorestframework` em `urls.py` do projeto escola e testar
        ```python
        #...
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('auth/', include('rest_framework.urls')),
        ]    
        ```
        Testar
        ```bash
        python3 manage.py runserver
        ```
        Login:
        `http://127.0.0.1:8000/auth/login`

        Logout:
        `http://127.0.0.1:8000/auth/logout`



    </p>

    </details> 

    ---

6. <span style="color:383E42"><b>Model Serializers</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    - Code
        ```python
        """
            O serializer pega os objetos python e transforma em json
            Também transforma json em objetos python
        """
        from rest_framework import serializers
        from django.db.models import Avg

        from .models import Curso, Avaliacao


        # Nome padronizado: Nome do Objeto + Serializer
        class AvaliacaoSerializer(serializers.ModelSerializer):  # Herda ModelSerializer

            class Meta:
                # Indica que o email não será apresentado ao consultar avaliações
                # Somente escrita/gravação
                extra_kwargs = {
                    'email': {'write_only': True}
                }
                model = Avaliacao  # Modelo que será serializado
                # Campos do modelo que serão apresentados
                fields = (
                    'id',
                    'curso',
                    'nome',
                    'email',
                    'comentario',
                    'avaliacao',
                    'criacao',
                    'ativo'
                )


        class CursoSerializer(serializers.ModelSerializer):
            # Nested Relationship - Somente viável em caso de poucos dados a trafegar
            # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

            # HyperLinked Related Field - a view_name = avaliacao-detail deve ser escrita assim, pois é o padrão
            # Pois a rota foi criada automaticamente
            # Retorna um link para cada avaliação referente ao curso
            # avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

            # Primary Key Related Field - Retorna todos ids da
            avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

            media_avaliacoes = serializers.SerializerMethodField()

            class Meta:
                model = Curso
                fields = (
                    'id',
                    'titulo',
                    'url',
                    'criacao',
                    'ativo',
                    'avaliacoes',
                    'media_avaliacoes'
                )

        ```



    </p>

    </details> 

    ---

7. <span style="color:383E42"><b>APIView para HTTP GET e POST</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    - HTTP GET e POST
        ```python
        from rest_framework.views import APIView
        from rest_framework.response import Response
        from rest_framework import status

        from .models import Curso, Avaliacao
        from .serializers import CursoSerializer, AvaliacaoSerializer


        class CursoAPIView(APIView):
            """
            API de Cursos da Geek University
            """
            def get(self, request):
                cursos = Curso.objects.all()
                serilizer = CursoSerializer(cursos, many=True)
                return Response(serilizer.data)

            def post(self, request):
                serializer = CursoSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)


        class AvaliacaoAPIView(APIView):
            """
            API de Avaliações da Geek
            """
            def get(self, request):
                avaliacoes = Avaliacao.objects.all()
                serializer = AvaliacaoSerializer(avaliacoes, many=True)
                return Response(serializer.data)

            def post(self, request):
                serializer = AvaliacaoSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
      
        ```

    - Criação de arquivo de rotas `urls.py` no app cursos
        ```python
        from django.urls import path

        from .views import CursoAPIView, AvaliacaoAPIView


        urlpatterns = [
            path('cursos/', CursoAPIView.as_view(), name='cursos'),
            path('avaliacoes/', AvaliacaoAPIView.as_view(), name='avaliacoes'),
        ]
        ```

    - Incluir url em `urls.py` do projeto escola que aponta para o urls.py do app `cursos`
        ```python
        #...
        urlpatterns = [
            path('api/v1/', include('cursos.urls')),
        #...
        ]
        ```

    - Testar
        `http://127.0.0.1:8000/api/v1/cursos/`
        `http://127.0.0.1:8000/api/v1/avaliacoes/`


    </p>

    </details> 

    ---

8. <span style="color:383E42"><b>Alterando APIView para uso de Generics</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    [Generics](https://www.django-rest-framework.org/api-guide/generic-views/)

    - APIViews
        ```python
        from rest_framework import generics

        from .models import Curso, Avaliacao
        from .serializers import CursoSerializer, AvaliacaoSerializer

        class CursosAPIView(generics.ListCreateAPIView):
            queryset = Curso.objects.all()
            serializer_class = CursoSerializer

        # Busca curso, edita e deleta
        class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
            queryset = Curso.objects.all()
            serializer_class = CursoSerializer


        class AvaliacoesAPIView(generics.ListCreateAPIView):
            queryset = Avaliacao.objects.all()
            serializer_class = AvaliacaoSerializer

        # Busca avaliacoes, edita e deleta
        class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
            queryset = Avaliacao.objects.all()
            serializer_class = AvaliacaoSerializer
        ```

    - Incluir urls para retorno por id em `cursos/urls.py`
        ```python
        from django.urls import path

        from .views import CursoAPIView, CursosAPIView, AvaliacaoAPIView, AvaliacoesAPIView


        urlpatterns = [
            path('cursos/', CursosAPIView.as_view(), name='cursos'),
            path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
            path('cursos/<int:pk>', CursoAPIView.as_view(), name='curso'),
            path('avaliacoes/<int:pk>', AvaliacaoAPIView.as_view(), name='avaliacao')
        ]
        ```

    - Testar
        `http://127.0.0.1:8000/api/v1/cursos/1`

    </p>

    </details> 

    ---

9. <span style="color:383E42"><b>API v2 e Sobrescrevendo métodos genéricos - Uso ViewSets e Routers</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    - Editar e incluir rotas em `cursos/urls.py`
        ```python
        from django.urls import path

        from rest_framework.routers import SimpleRouter

        from .views import (
            CursoAPIView,
            CursosAPIView,
            AvaliacaoAPIView,
            AvaliacoesAPIView,
            CursoViewSet,
            AvaliacaoViewSet
            )


        router = SimpleRouter()
        router.register('cursos', CursoViewSet)
        router.register('avaliacoes', AvaliacaoViewSet)


        urlpatterns = [
            path('cursos/', CursosAPIView.as_view(), name='cursos'),
            path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
            path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),
            path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='curso_avaliacao'),

            path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
            path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
        ]
        ```

    - Incluir as novas rotas em `escola/urls.py`
        ```python
        from django.contrib import admin
        from django.urls import path, include

        from cursos.urls import router

        urlpatterns = [
            path('api/v1/', include('cursos.urls')),
            path('api/v2/', include(router.urls)),
            path('admin/', admin.site.urls),
            path('api-auth/', include('rest_framework.urls')),
        ]
        ```

    - Inclusão/sobrescrita dos métodos genéricos em `cursos/views.py`
        ```python
        from rest_framework import generics
        from rest_framework.generics import get_object_or_404

        from rest_framework import viewsets
        from rest_framework.decorators import action
        from rest_framework.response import Response
        from rest_framework import mixins

        from .models import Curso, Avaliacao
        from .serializers import CursoSerializer, AvaliacaoSerializer

        """
        API V1
        """
        class CursosAPIView(generics.ListCreateAPIView):
            queryset = Curso.objects.all()
            serializer_class = CursoSerializer

        # Busca curso, edita e deleta
        class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
            queryset = Curso.objects.all()
            serializer_class = CursoSerializer

        class AvaliacoesAPIView(generics.ListCreateAPIView):
            queryset = Avaliacao.objects.all()
            serializer_class = AvaliacaoSerializer

            def get_queryset(self):
                if self.kwargs.get('curso_pk'):
                    return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
                return self.queryset.all()

        # Busca avaliacoes, edita e deleta
        class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
            queryset = Avaliacao.objects.all()
            serializer_class = AvaliacaoSerializer

            def get_object(self):
                if self.kwargs.get('curso_pk'):
                    return get_object_or_404(self.get_queryset(),
                                            curso_id=self.kwargs.get('curso_pk'),
                                            pk=self.kwargs.get('avaliacao_pk'))
                return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))


        """
        API V2
        """


        class CursoViewSet(viewsets.ModelViewSet):
            queryset = Curso.objects.all()
            serializer_class = CursoSerializer

            @action(detail=True, methods=['get'])
            def avaliacoes(self, request, pk=None):
                curso = self.get_object()
                serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
                return Response(serializer.data)

        class AvaliacaoViewSet(viewsets.ModelViewSet):
            queryset = Avaliacao.objects.all()
            serializer_class = AvaliacaoSerializer
        
        ```

    - Testar
        `http://127.0.0.1:8000/api/v1/avaliacoes/2/`

    </p>

    </details> 

    ---


10. <span style="color:383E42"><b>Customizando as ViewSets</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    Caso não queira alguma das ações disponíveis, basta comentar/remover
    - `cursos/views.py`
        ```python
        #...
        class AvaliacaoViewSet(
            mixins.ListModelMixin,
            mixins.CreateModelMixin,
            mixins.RetrieveModelMixin,
            mixins.UpdateModelMixin,
            mixins.DestroyModelMixin,
            viewsets.GenericViewSet
        ):
            queryset = Avaliacao.objects.all()
            serializer_class = AvaliacaoSerializer
        ```



    </p>

    </details> 

    ---

11. <span style="color:383E42"><b>Utilizando Relações com Django REST</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    - `cursos/serializers.py`
        ```python
        class CursoSerializer(serializers.ModelSerializer):
        # Nested Relationship - Somente viável em caso de poucos dados a trafegar
        # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

        # HyperLinked Related Field - a view_name = avaliacao-detail deve ser escrita assim, pois é o padrão
        # Pois a rota foi criada automaticamente
        # Retorna um link para cada avaliação referente ao curso
        # avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

        # Primary Key Related Field - Retorna todos ids das avaliacoes
        avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

        media_avaliacoes = serializers.SerializerMethodField()

        class Meta:
            model = Curso
            fields = (
                'id',
                'titulo',
                'url',
                'criacao',
                'ativo',
                'avaliacoes',
                'media_avaliacoes'
            )
        ```

    </p>

    </details> 

    ---

12. <span style="color:383E42"><b>Incluindo Paginação e Ordenação</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    - Em `escola/settings.py`
        ```python
        #...
        # DRF
        REST_FRAMEWORK = {
            'DEFAULT_AUTHENTICATION_CLASSES': (
                'rest_framework.authentication.SessionAuthentication',
            ),
            'DEFAULT_PERMISSION_CLASSES': (
                'rest_framework.permissions.IsAuthenticatedOrReadOnly',
            ),
            'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
            'PAGE_SIZE': 2 # Define quantidade de elementos por página
        }
        #...
        ```

    - Incluir ordenação aos modelos
        ```python
        from django.db import models

        # Create your models here.
        class Base(models.Model):
            criacao = models.DateTimeField(auto_now_add=True)
            atualizacao = models.DateTimeField(auto_now=True)
            ativo = models.BooleanField(default=True)

            class Meta:
                abstract = True

        class Curso(Base):
            titulo = models.CharField(max_length=255)
            url = models.URLField(unique=True)

            class Meta:
                verbose_name = 'Curso'
                verbose_name_plural = 'Cursos'
                ordering = ['id']  # Ordenação por id

            def __str__(self):
                return self.titulo
            
        class Avaliacao(Base):
            curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
            nome = models.CharField(max_length=255)
            email = models.EmailField()
            comentario = models.TextField(blank=True, default='')
            avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

            class Meta:
                verbose_name = 'Avaliação'
                verbose_name_plural = 'Avaliações'
                unique_together = ['email', 'curso'] # Somente 1 avaliação com mesmo curso e email
                ordering = ['id']  # Ordena o modelo pelo id, caso queira ordem inversa (decrescente)
                # ordering = ['-id']  # Ordena o modelo pelo id, ordem inversa (decrescente)

            def __str__(self):
                return f'{self.nome} avaliou o curso {self.curso} com nota {self.avaliacao}'
        ```
    
    - Paginação em método criado ou sobrescrito em `cursos/views.py`
        ```python
        #...
        class CursoViewSet(viewsets.ModelViewSet):
        queryset = Curso.objects.all()
        serializer_class = CursoSerializer

        @action(detail=True, methods=['get'])
        def avaliacoes(self, request, pk=None):
            self.pagination_class.page_size = 1
            avaliacoes = Avaliacao.objects.filter(curso_id=pk)
            page = self.paginate_queryset(avaliacoes)

            if page is not None:
                serializer = AvaliacaoSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
        
            serializer = AvaliacaoSerializer(avaliacoes, many=True)
            return Response(serializer.data)
        #...
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