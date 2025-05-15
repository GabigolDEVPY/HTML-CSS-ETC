import sys
sys.dont_write_bytecode = True
from app.app import createAPP

app = createAPP()

if __name__ == "__main__":
    app.run(debug=True, host=('0.0.0.0'), port=6000)