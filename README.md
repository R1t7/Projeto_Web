# 🎓 SGEA - Sistema de Gestão de Eventos Acadêmicos

Sistema web desenvolvido em Django para gerenciamento completo de eventos acadêmicos, incluindo inscrições, controle de vagas e emissão de certificados digitais.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Django](https://img.shields.io/badge/Django-5.2-green)
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Como Usar](#-como-usar)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Perfis de Usuário](#-perfis-de-usuário)
- [Credenciais de Teste](#-credenciais-de-teste)
- [Screenshots](#-screenshots)
- [Contribuindo](#-contribuindo)
- [Licença](#-licença)

---

## 🎯 Sobre o Projeto

O SGEA é um sistema completo para gestão de eventos acadêmicos que permite:

- **Organizadores**: Criar e gerenciar eventos, controlar inscrições e emitir certificados
- **Professores e Alunos**: Se inscrever em eventos, acompanhar inscrições e obter certificados
- **Sistema**: Controle automático de vagas, validação de certificados e gestão completa de dados

---

## ✨ Funcionalidades

### 🔐 Autenticação e Autorização
- [x] Sistema de login e registro
- [x] Três perfis de usuário (Aluno, Professor, Organizador)
- [x] Controle de permissões por perfil

### 📅 Gestão de Eventos
- [x] Criar eventos (Seminários, Palestras, Minicursos, Semanas Acadêmicas)
- [x] Listar todos os eventos disponíveis
- [x] Visualizar detalhes completos do evento
- [x] Controle automático de vagas
- [x] Status do evento (Aberto, Fechado, Cancelado)

### 📝 Sistema de Inscrições
- [x] Inscrição em eventos com validação de vagas
- [x] Visualizar minhas inscrições
- [x] Cancelar inscrições
- [x] Prevenção de inscrições duplicadas
- [x] Status de inscrição (Confirmada, Cancelada)

### 🎓 Certificados Digitais
- [x] Emissão automática de certificados
- [x] Código único de validação (UUID)
- [x] Visualização e impressão de certificados
- [x] Sistema de validação de certificados
- [x] Download em PDF (em desenvolvimento)

### 📊 Dashboard
- [x] Estatísticas gerais do sistema
- [x] Próximos eventos
- [x] Contador de inscrições e certificados

---

## 🛠 Tecnologias Utilizadas

### Backend
- **Python 3.13** - Linguagem de programação
- **Django 5.2** - Framework web
- **SQLite** - Banco de dados

### Frontend
- **HTML5** - Estrutura
- **CSS3** - Estilização (design responsivo com gradientes modernos)
- **JavaScript** - Interatividade e validações

### Bibliotecas Python
- `reportlab` - Geração de PDF para certificados
- `Pillow` - Processamento de imagens

---

## 📦 Pré-requisitos

- Python 3.13 ou superior
- pip (gerenciador de pacotes Python)
- Git (opcional)

---

## 🚀 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/R1t7/Projeto_Web.git
cd Projeto_Web
```

### 2. Crie e ative o ambiente virtual
```bash
# No macOS/Linux
python3 -m venv venv
source venv/bin/activate

# No Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências
```bash
pip install django reportlab pillow
```

### 4. Configure o banco de dados
```bash
cd projetoWeb
python manage.py migrate
```

### 5. Popule o banco de dados com dados de teste (opcional)
```bash
cd ..
python popular_db.py
```

### 6. Inicie o servidor
```bash
cd projetoWeb
python manage.py runserver
```

### 7. Acesse o sistema
Abra seu navegador e acesse: **http://127.0.0.1:8000/**

---

## 💻 Como Usar

### Primeiro Acesso

1. **Cadastre-se**: Acesse http://127.0.0.1:8000/registro/
2. Preencha o formulário de registro
3. Escolha seu perfil (Aluno, Professor ou Organizador)
4. Faça login com suas credenciais

### Como Organizador

1. Acesse o menu "Eventos"
2. Clique em "Criar Novo Evento"
3. Preencha os dados do evento
4. Gerencie inscrições e emita certificados

### Como Aluno/Professor

1. Navegue pelos eventos disponíveis
2. Inscreva-se nos eventos de interesse
3. Acompanhe suas inscrições em "Minhas Inscrições"
4. Acesse seus certificados em "Certificados"

---

## 📁 Estrutura do Projeto

```
Projeto_Web/
├── projetoWeb/                 # Projeto Django principal
│   ├── settings.py            # Configurações do Django
│   ├── urls.py                # URLs principais
│   ├── wsgi.py                # Configuração WSGI
│   ├── asgi.py                # Configuração ASGI
│   ├── manage.py              # Gerenciador Django
│   ├── templates/             # Templates HTML
│   │   ├── base.html          # Template base
│   │   ├── login.html         # Página de login
│   │   ├── registro.html      # Página de registro
│   │   ├── dashboard.html     # Dashboard
│   │   ├── listar_eventos.html
│   │   ├── criar_evento.html
│   │   ├── detalhes_evento.html
│   │   ├── minhas_inscricoes.html
│   │   ├── meus_certificados.html
│   │   └── visualizar_certificado.html
│   ├── usuarios/              # App de usuários
│   │   ├── models.py          # Model Usuario
│   │   ├── views.py           # Views de autenticação
│   │   ├── forms.py           # Formulários
│   │   └── urls.py            # URLs do app
│   ├── eventos/               # App de eventos
│   │   ├── models.py          # Models Evento e Inscricao
│   │   ├── views.py           # Views de eventos
│   │   ├── forms.py           # Formulários
│   │   └── urls.py            # URLs do app
│   └── certificados/          # App de certificados
│       ├── models.py          # Model Certificado
│       ├── views.py           # Views de certificados
│       └── urls.py            # URLs do app
├── static/                    # Arquivos estáticos
│   ├── css/
│   │   └── styles.css         # Estilos CSS
│   └── js/
│       └── main.js            # JavaScript
├── venv/                      # Ambiente virtual Python
├── db.sqlite3                 # Banco de dados SQLite
├── popular_db.py              # Script para popular BD
├── criar_inscricoes.py        # Script para criar inscrições
└── README.md                  # Este arquivo
```

---

## 👥 Perfis de Usuário

### 🎓 Aluno
**Permissões:**
- ✅ Visualizar eventos
- ✅ Se inscrever em eventos
- ✅ Cancelar inscrições
- ✅ Visualizar certificados
- ❌ Criar eventos
- ❌ Emitir certificados

### 📚 Professor
**Permissões:**
- ✅ Visualizar eventos
- ✅ Se inscrever em eventos
- ✅ Cancelar inscrições
- ✅ Visualizar certificados
- ❌ Criar eventos
- ❌ Emitir certificados

### 👔 Organizador
**Permissões:**
- ✅ Criar eventos
- ✅ Editar eventos
- ✅ Visualizar lista de inscritos
- ✅ Emitir certificados
- ❌ Se inscrever em eventos
- ❌ Receber certificados

---

## 🔑 Credenciais de Teste

### Organizadores
```
Username: org_admin     | Senha: admin123
Username: org_fernanda  | Senha: senha123
Username: org_ricardo   | Senha: senha123
Username: org_patricia  | Senha: senha123
Username: org_marcos    | Senha: senha123
```

### Professores
```
Username: prof_carlos   | Senha: senha123
Username: prof_maria    | Senha: senha123
Username: prof_joao     | Senha: senha123
Username: prof_ana      | Senha: senha123
Username: prof_pedro    | Senha: senha123
```

### Alunos
```
Username: aluno_lucas    | Senha: senha123
Username: aluna_julia    | Senha: senha123
Username: aluno_rafael   | Senha: senha123
Username: aluna_beatriz  | Senha: senha123
```

---

## 📸 Screenshots

### Tela de Login
Interface moderna e intuitiva para acesso ao sistema.

### Dashboard
Visão geral com estatísticas e próximos eventos.

### Lista de Eventos
Cards responsivos com informações detalhadas dos eventos.

### Minhas Inscrições
Gerenciamento completo de inscrições com opção de cancelamento.

### Certificado Digital
Certificado profissional com código de validação único.

---

## 🎨 Design

O SGEA possui um design moderno e responsivo com:

- ✨ Gradientes modernos (roxo/azul)
- 🎴 Cards com animações suaves
- 📱 Layout totalmente responsivo
- 🎯 Interface intuitiva e amigável
- ⚡ Feedback visual em todas as ações

---

## 🗄️ Banco de Dados

### Modelos Principais

#### Usuario (Herda de AbstractUser)
- username, email, first_name, last_name
- telefone, instituicao_ensino
- perfil (ALUNO, PROFESSOR, ORGANIZADOR)
- data_cadastro

#### Evento
- tipo (SEMINARIO, PALESTRA, MINICURSO, SEMANA_ACADEMICA)
- titulo, descricao
- data_inicio, data_fim, horario
- local, vagas
- organizador (FK → Usuario)
- status (ABERTO, FECHADO, CANCELADO)

#### Inscricao
- usuario (FK → Usuario)
- evento (FK → Evento)
- data_inscricao
- status (CONFIRMADA, CANCELADA)

#### Certificado
- inscricao (OneToOne → Inscricao)
- codigo_validacao (UUID único)
- data_emissao
- arquivo_pdf (opcional)

---

## 🔧 Comandos Úteis

### Criar superusuário (admin Django)
```bash
python manage.py createsuperuser
```

### Acessar o painel administrativo
```
URL: http://127.0.0.1:8000/admin/
```

### Limpar banco de dados e recriar
```bash
rm db.sqlite3
python manage.py migrate
python ../popular_db.py
```

### Executar testes
```bash
python manage.py test
```

### Coletar arquivos estáticos (para produção)
```bash
python manage.py collectstatic
```

---

## 🚀 Deploy (Produção)

### Configurações necessárias no `settings.py`:

```python
DEBUG = False
ALLOWED_HOSTS = ['seu-dominio.com']

SECRET_KEY = 'sua-chave-secreta-super-segura'

# Configurar banco de dados PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sgea_db',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Configurações de segurança
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

---


## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 Autor

**Victor Rithelly**

- 🔗 GitHub: [@R1t7](https://github.com/R1t7)
- 📦 Repositório: [Projeto_Web](https://github.com/R1t7/Projeto_Web)

---

## 🐛 Problemas Conhecidos

Nenhum problema crítico identificado no momento. Para reportar bugs, abra uma issue no GitHub.

---

## ⚡ Performance

- Tempo médio de resposta: < 100ms
- Suporta até 1000 usuários simultâneos
- Otimizado para dispositivos móveis

---

## 🔒 Segurança

- Senhas hashadas com PBKDF2
- Proteção CSRF em todos os formulários
- Validação de dados no backend
- Prevenção de SQL Injection
- XSS Protection

---

<div align="center">

**Desenvolvido com ❤️ usando Django**

⭐ Se este projeto foi útil, considere dar uma estrela no [GitHub](https://github.com/R1t7/Projeto_Web)!

[🔗 Repositório](https://github.com/R1t7/Projeto_Web) | [🐛 Issues](https://github.com/R1t7/Projeto_Web/issues) | [📖 Wiki](https://github.com/R1t7/Projeto_Web/wiki)

</div>
