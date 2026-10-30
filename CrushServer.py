from http.server import BaseHTTPRequestHandler


class CrushServer(BaseHTTPRequestHandler):
    """ класс, который отвечает за обработку входящих запросов от клиентов """

    with open('contacts_page.html', 'r') as f:
        message = f.read()

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(self.message.encode('utf-8'))  # Тело ответа

    def do_POST(self):
        """ метод для обработки входящих POST - запросов """
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        print(body)
        self.send_response(200)
        self.end_headers()
