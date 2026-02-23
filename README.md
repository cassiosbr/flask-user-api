# Flask User API

API REST para cadastro e consulta de usuários, construída com Flask, SQLAlchemy e arquitetura modular.

## Funcionalidades
- Cadastro de usuário
- Listagem de usuários
- Consulta de usuário por ID
- Validações de negócio (nome, email único)

## Estrutura do Projeto
```
flask-user-api/
├── app/
│   ├── __init__.py           # Factory do app Flask
│   ├── core/                 # Config e extensões (SQLAlchemy)
│   ├── model/                # Modelos ORM
│   ├── repositories/         # Repositórios (acesso a dados)
│   ├── services/             # Serviços (regras de negócio)
│   └── routes/               # Blueprints (rotas)
├── run.py                    # Entry point
├── requirements.txt          # Dependências
└── tests/                    # Testes unitários
```

## Padrões de Arquitetura
- **Service Layer**: regras de negócio ficam em `services/`, separando lógica do acesso a dados.
- **Repository Pattern**: repositórios em `repositories/` encapsulam queries e persistência.
- **Blueprints**: rotas organizadas por módulo.
- **Injeção de dependência**: `UserService` aceita repositório customizado (facilita testes).

## Como executar (desenvolvimento)
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o app:
   ```bash
   python run.py
   ```
   O servidor estará em `http://localhost:5000`.

## Execução em produção
- Use um WSGI server como Gunicorn:
  ```bash
  gunicorn 'app:create_app()'
  ```
- Configure variáveis de ambiente (ex: `FLASK_ENV=production`, configs de banco).
- Não use `run.py` em produção.

## Testes
- Os testes estão em `tests/`.
- Execute com:
  ```bash
  pytest
  ```
- Os serviços são testados com mocks/fakes, sem acessar o banco real.

## Exemplos de uso
- Cadastro:
  ```http
  POST /users/
  Content-Type: application/json
  {
    "name": "Fulano",
    "email": "fulano@email.com"
  }
  ```
- Listagem:
  ```http
  GET /users/
  ```

## Observações
- O projeto segue boas práticas de separação de responsabilidades.
- Validações de negócio ficam no service, validações de request (Content-Type, JSON) nas rotas.
- Fácil de expandir para autenticação, outros módulos, etc.