from flask import Flask, render_template_string
import requests


app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <h1>ColorPAR Test - VSCode Working</h1>
    <button onclick="testPico()">Test Pico2W Connection</button>
    <div id="result"></div>
    
    <script>
    function testPico() {
        fetch('/test_pico')
        .then(r => r.json())
        .then(data => document.getElementById('result').innerHTML = 
            '<pre>' + JSON.stringify(data, null, 2) + '</pre>')
    }
    </script>
    ''')

@app.route('/test_pico')
def test_pico():
    try:
        response = requests.get('http://192.168.1.100/data', timeout=3)
        return {'status': 'success', 'data': response.json()}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
