from http.server import HTTPServer, BaseHTTPRequestHandler

taskList = ['Task 1','Task 2', 'Task 3', 'Task 4']
class onHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        #self.wfile.write('Hello World by Dev36'.encode())
        #self.wfile.write(self.path[1:].encode())
        self.wfile.write('./index.html'.encode())
        """
        output = ''
        output += '<html><body>'
        output += '<h1>Task List</h1>'
        for i in taskList:
            output += task
            output += '</br>'
        output += '</body></html>'
        self.wfile.write(output.encode())
        """

def main():
    PORT = 8000
    server = HTTPServer(('', PORT), onHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()