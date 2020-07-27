from juntos import app
import os

app.secret_key = os.urandom(12)
if __name__ == '__main__':
    app.run()


