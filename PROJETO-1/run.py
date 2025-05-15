import sys
sys.dont_write_bytecode = True
from app.app import create_app

app = create_app()
app.secret_key= '4892374792jfhsdjkhfsd'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)