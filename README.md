# Inventário App - API Django REST

## Descrição
Sistema de inventário gamificado com elementos RPG desenvolvido em Django REST Framework. Permite gerenciar usuários, perfis de jogadores, itens, inventários, missões e conquistas.

## Funcionalidades
- **Gestão de Usuários**: Cadastro e gerenciamento de usuários
- **Perfis de Jogadores**: Sistema de níveis e experiência
- **Sistema de Itens**: Catálogo de itens com raridade e uploads de mídia
- **Inventários**: Gestão de inventários com capacidade limitada
- **Sistema de Missões**: Missões com recompensas de XP
- **Conquistas**: Sistema de pontuação e badges

## Tecnologias
- Python 3.13
- Django 5.2
- Django REST Framework
- Oracle Database
- django-filter
- python-decouple
- CORS Headers

## Estrutura da API

### Endpoints Principais
- users - Gerenciamento de usuários
- `/playerprofiles/` - Perfis de jogadores
- `/items/` - Catálogo de itens
- `/inventories/` - Inventários dos jogadores
- `/inventoryitems/` - Itens nos inventários
- `/quests/` - Missões disponíveis
- `/completedquests/` - Histórico de missões
- `/achievements/` - Sistema de conquistas

### Configuração do Ambiente
Crie um arquivo .env na raiz do projeto:
```
SECRET_KEY=sua_chave_secreta_aqui
DEBUG=True
DB_NAME=nome_do_banco
DB_USER=usuario_oracle
DB_PASSWORD=senha_oracle
```

## Instalação
1. Clone o repositório
2. Instale as dependências: `pip install -r requirements.txt`
3. Configure o arquivo .env
4. Execute as migrações: `python manage.py migrate`
5. Crie um superusuário: `python manage.py createsuperuser`
6. Inicie o servidor: `python manage.py runserver`

## Uso
A API estará disponível em `http://localhost:8000/`
Admin panel disponível em `http://localhost:8000/admin/`

## CORS
O projeto está configurado para aceitar requisições de qualquer origem, ideal para desenvolvimento com frontend React/Vue.js.
