import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from abc import ABC, abstractmethod

# ==============================
# ✅ Configuração inicial
# ==============================
EMAIL       = ""
PASSWORD    = ""
LANG        = "pt"  # Defina "en" para inglês, "es" para espanhol





TRANSLATIONS = {
    "pt": {
        "login_url": "https://www.linkedin.com/login",
        "search_url": "https://www.linkedin.com/search/results/people/?activelyHiringForJobTitles=%5B%22-100%22%5D&geoUrn=%5B%22106057199%22%5D&keywords=it%20recruiter&origin=FACETED_SEARCH&sid=d!b&page={}",
        "no_results": "Nenhum resultado encontrado",
        "add_note": "Adicionar nota",
        "send_invite": "Enviar convite",
        "follow": "Seguir",
        "message": "Olá! Adoraria me conectar com você! Acredito que boas conexões sempre agregam e são ótimas experiências. Desde já, obrigado! Abraço!",
        "email_confirmation_text": "Para confirmar que este usuário é seu conhecido, insira o endereço de e-mail do mesmo para se conectar.",
        "weekly_limit_reached_text": "Você alcançou o limite semanal de convites",
        "print_start": "🚀 Iniciando LinkedIn Bot...",
        "print_login": "🔑 Realizando login...",
        "print_login_success": "✅ Login efetuado com sucesso!",
        "print_no_results": "🚨 Nenhum resultado encontrado. Encerrando o bot...",
        "print_connecting": "🔹 Buscando pessoas para conectar...",
        "print_clicking": "📩 Enviando convite para: {}",
        "print_following": "👤 Seguindo usuário: {}",
        "print_invite_sent": "✅ Convite enviado com sucesso!",
        "print_email_required": "❌ Email obrigatório para conexão. Pulando usuário...",
        "print_error": "⚠️ Erro encontrado: {}",
        "print_done": "🎉 Processo concluído! Finalizando o bot...",
        "print_detecting_pages": "🔍 Detectando número total de páginas...",
        "print_total_pages": "📄 Número total de páginas encontrado: {}",
    },
    "en": {
        "login_url": "https://www.linkedin.com/login",
        "search_url": "https://www.linkedin.com/search/results/people/?activelyHiringForJobTitles=%5B%22-100%22%5D&geoUrn=%5B%22106057199%22%5D&keywords=it%20recruiter&origin=FACETED_SEARCH&sid=d!b&page={}",
        "no_results": "No results found",
        "add_note": "Add note",
        "send_invite": "Send invitation",
        "follow": "Follow",
        "message": "Hello! I would love to connect with you! I believe good connections always add value and bring great experiences. Thanks in advance! Best regards!",
        "email_confirmation_text": "To confirm you know this user, enter their email address to connect.",
        "weekly_limit_reached_text": "You have reached the weekly invitation limit",
        "print_start": "🚀 Starting LinkedIn Bot...",
        "print_login": "🔑 Logging in...",
        "print_login_success": "✅ Login successful!",
        "print_no_results": "🚨 No results found. Closing the bot...",
        "print_connecting": "🔹 Searching for people to connect...",
        "print_clicking": "📩 Sending invitation to: {}",
        "print_following": "👤 Following user: {}",
        "print_invite_sent": "✅ Invitation sent successfully!",
        "print_email_required": "❌ Email required for connection. Skipping user...",
        "print_error": "⚠️ Error encountered: {}",
        "print_done": "🎉 Process completed! Closing the bot...",
        "print_detecting_pages": "🔍 Detecting total number of pages...",
        "print_total_pages": "📄 Total number of pages found: {}",
    },
    "es": {
        "login_url": "https://www.linkedin.com/login",
        "search_url": "https://www.linkedin.com/search/results/people/?activelyHiringForJobTitles=%5B%22-100%22%5D&geoUrn=%5B%22106057199%22%5D&keywords=it%20recruiter&origin=FACETED_SEARCH&sid=d!b&page={}",
        "no_results": "No se encontraron resultados",
        "add_note": "Agregar nota",
        "send_invite": "Enviar invitación",
        "follow": "Seguir",
        "message": "¡Hola! Me encantaría conectarme contigo. Creo que las buenas conexiones siempre agregan valor y brindan grandes experiencias. ¡Gracias de antemano! Saludos!",
        "email_confirmation_text": "Para confirmar que conoces a este usuario, ingresa su dirección de correo electrónico para conectarte.",
        "weekly_limit_reached_text": "Has alcanzado el límite semanal de invitaciones",
        "print_start": "🚀 Iniciando LinkedIn Bot...",
        "print_login": "🔑 Iniciando sesión...",
        "print_login_success": "✅ ¡Inicio de sesión exitoso!",
        "print_no_results": "🚨 No se encontraron resultados. Cerrando el bot...",
        "print_connecting": "🔹 Buscando personas para conectar...",
        "print_clicking": "📩 Enviando invitación a: {}",
        "print_following": "👤 Siguiendo usuario: {}",
        "print_invite_sent": "✅ ¡Invitación enviada con éxito!",
        "print_email_required": "❌ Se requiere correo electrónico para la conexión. Omitiendo usuario...",
        "print_error": "⚠️ Error encontrado: {}",
        "print_done": "🎉 ¡Proceso completado! Cerrando el bot...",
        "print_detecting_pages": "🔍 Detectando número total de páginas...",
        "print_total_pages": "📄 Número total de páginas encontrado: {}",
    }
}

TEXTS = TRANSLATIONS.get(LANG, TRANSLATIONS)  # Corrigido para garantir um idioma válido




class WebDriverFactory:
    """ Factory Pattern para gerenciar a instância do WebDriver """
    _instance = None

    @classmethod
    def get_driver(cls):
        if cls._instance is None:
            chrome_options = Options()
            chrome_options.add_argument("--force-device-scale-factor=0.5")
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument('--ignore-ssl-errors')
            cls._instance = webdriver.Chrome(
                executable_path="chromedriver-win64/chromedriver.exe",
                options=chrome_options
            )
        return cls._instance





class BotBase(ABC):
    def __init__(self):
        self.driver = WebDriverFactory.get_driver()

    @abstractmethod
    def run(self):
        pass

    def open_page(self, url):
        """ Abre uma página no navegador """
        self.driver.get(url)
        time.sleep(5)

    def quit(self):
        """ Encerra o WebDriver """
        print(TEXTS["print_done"])
        self.driver.quit()





class LinkedInBot(BotBase):
    def __init__(self, email, password):
        super().__init__()
        self.email = email
        self.password = password

    def login(self):
        """ Realiza login no LinkedIn """
        print(TEXTS["print_login"])
        self.open_page(TEXTS["login_url"])
        self.driver.find_element_by_name("session_key").send_keys(self.email)
        self.driver.find_element_by_name("session_password").send_keys(self.password)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(5)
        print(TEXTS["print_login_success"])

    
    def check_weekly_limit(self):
        """ Verifica se o limite semanal de convites foi atingido e encerra o bot se necessário """
        try:
            modal = self.driver.find_element("xpath", "//div[@aria-labelledby='ip-fuse-limit-alert__header']")
            modal_text = modal.text

            if TEXTS["weekly_limit_reached_text"] in modal_text:
                print(TEXTS["print_weekly_limit_reached"])
                self.driver.quit()
                quit()

        except:
            pass  # Se o modal não for encontrado, continua normalmente

    def check_no_results(self):
        """ Verifica se a página retornou 'Nenhum resultado encontrado' """
        try:
            self.driver.find_element_by_xpath(f"//h2[contains(text(), '{TEXTS['no_results']}')]")
            print(TEXTS["print_no_results"])
            self.quit()
            quit()
        except:
            pass

    def get_total_pages(self):
        """ Obtém o número total de páginas da pesquisa """
        print(TEXTS["print_detecting_pages"])
        try:
            pagination_buttons = self.driver.find_elements_by_xpath("//li[@data-test-pagination-page-btn]")
            if pagination_buttons:
                last_page_number = max([int(btn.text.strip()) for btn in pagination_buttons if btn.text.strip().isdigit()])
                print(TEXTS["print_total_pages"].format(last_page_number))
                return last_page_number
        except Exception as e:
            print(TEXTS["print_error"].format(e))

        return 1  # Se não conseguir detectar, assume 1 página

    def check_email_requirement(self):
        """ Verifica se o LinkedIn exige um e-mail para conexão """
        try:
            modal = self.driver.find_element_by_class_name("send-invite")
            modal_text = modal.text

            if TEXTS["email_confirmation_text"] in modal_text:
                print(TEXTS["print_email_required"])
                close_button = modal.find_element_by_xpath("//button[@aria-label='Fechar']")
                self.driver.execute_script("arguments[0].click();", close_button)
                time.sleep(2)
                return True  # Email obrigatório, pulando usuário
            
        except:
            return False  # Nenhum modal encontrado, pode continuar normalmente
        
        return False

    def process_button(self, btn):
        """ Decide se deve seguir ou conectar com o usuário """
        btn_text = btn.text.strip()

        if btn_text.startswith(TEXTS["follow"]):
            print(TEXTS["print_following"].format(btn_text))
            self.driver.execute_script("arguments[0].click();", btn)
            time.sleep(3)
            return  # Apenas segue o usuário e continua
        
        self.send_invite(btn)  # Se não for "Seguir", tenta enviar o convite

    def send_invite(self, btn):
        """ Envia o convite com mensagem personalizada """
        try:          
            print(TEXTS["print_clicking"].format(btn.text))
            self.driver.execute_script("arguments[0].click();", btn)
            time.sleep(5)

            # Verifica se precisa de email antes de continuar
            if self.check_email_requirement():
                return  # Se o email for necessário, sai da função

            add_note_button = self.driver.find_element_by_xpath(f"//button[@aria-label='{TEXTS['add_note']}']")
            self.driver.execute_script("arguments[0].click();", add_note_button)
            time.sleep(2)

            textarea = self.driver.find_element_by_id("custom-message")
            for char in TEXTS["message"]:
                textarea.send_keys(char)
            time.sleep(2)

            send_button = self.driver.find_element_by_xpath(f"//button[@aria-label='{TEXTS['send_invite']}']")
            self.driver.execute_script("arguments[0].click();", send_button)
            time.sleep(5)

            self.check_weekly_limit()  # Verifica limite antes de continuar

            print(TEXTS["print_invite_sent"])
        except Exception as e:
            print(TEXTS["print_error"].format(e))

    def connect_people(self):
        """ Percorre todas as páginas e adiciona conexões """
        print(TEXTS["print_connecting"])
        self.open_page(TEXTS["search_url"].format(1))
        total_pages = self.get_total_pages()

        for page in range(1, total_pages + 1):
            self.open_page(TEXTS["search_url"].format(page))
            time.sleep(10)
            self.check_no_results()

            buttons = self.driver.find_elements_by_xpath("//button[contains(@aria-label, 'Convidar') or contains(@aria-label, 'Seguir')]")
            for btn in buttons:
                self.process_button(btn)

    def run(self):
        """ Inicia o bot """
        print(TEXTS["print_start"])
        self.login()
        self.connect_people()


if __name__ == "__main__":
    bot = LinkedInBot(EMAIL, PASSWORD)
    bot.run()
