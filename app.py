from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Docker + Flask Demo</title>
            <style>
                body { font-family: Arial; background-color: #f2f2f2; text-align: center; padding: 50px; }
                h1 { color: #333; }
                p { color: #666; }
            </style>
        </head>
        <body>
            <h1>Hello from Flask inside Docker! 🚀</h1>
            <p>This is a demonstration of a Flask app running in a Docker container.</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
