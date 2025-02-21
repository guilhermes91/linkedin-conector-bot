# 🚀 LinkedIn Auto Connect Bot

Um bot automático para se conectar com recrutadores no LinkedIn.  
Ele pode **seguir usuários** e **enviar solicitações de conexão** automaticamente.

---

## 🛠️ Instalação e Configuração

### 1️⃣ **Instalar Dependências**
Execute o seguinte comando no terminal para instalar as dependências necessárias:
```bash
#pip install selenium
pip install -r requirements.txt
```

---

### 2️⃣ **Baixar e Instalar WebDriver**
1. Acesse: [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/)
2. Baixe a versão compatível com seu navegador Chrome.
3. Extraia e copie o **chromedriver.exe** para a pasta do projeto.

---

### 3️⃣ **Configurar Credenciais**
Edite o código `linkedin.py` e insira seu **e-mail** e **senha** do LinkedIn:

```python
EMAIL = "seu_email@exemplo.com"
PASSWORD = "sua_senha"
```

---

### 4️⃣ **Definir Idioma**
O bot suporta vários idiomas. No código, altere `LANG` para um dos idiomas disponíveis:

```python
LANG = "pt"  # Opções: "en", "es", "pl", "ja", "ru"
```

---

## 🚀 **Como Executar**
Após configurar tudo, rode o seguinte comando no terminal:
```bash
python linkedin.py
```

---

## ⚠️ **Limite de Conexões**
O LinkedIn permite **apenas 100 conexões por semana**.  
O bot respeita esse limite automaticamente para evitar bloqueios.

---

## 🛠️ **Dependências**
Este bot requer as seguintes bibliotecas Python:

- `selenium`
- `webdriver-manager`

Para instalar manualmente, execute:
```bash
pip install selenium webdriver-manager
```

---

## 📜 **Licença**
Este projeto é **open-source** e pode ser usado livremente.

---

### 🚀 **Resumo das Melhorias**
✅ **Agora o bot suporta múltiplos idiomas** (Português, Inglês, Espanhol, Polonês, Japonês e Russo).  
✅ **Readme pronto para o GitHub** explicando como instalar e configurar.  
✅ **Passo a passo para instalar o WebDriver** via **[Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/)**.  
✅ **Limite de 100 conexões por semana para evitar bloqueios**.  

Agora é só rodar e começar a se conectar automaticamente no LinkedIn! 🚀🔥

