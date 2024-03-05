from flask import Flask,request,render_template
import re
app = Flask(__name__)



################################
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/results", methods=['POST'])
def results():
    regex_pattern = request.form['regex']
    test_string = request.form['testString']
    matched_strings = re.findall(regex_pattern,test_string)
    return render_template('results.html', matched_strings=matched_strings)
    
@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    is_valid = validate_email_regex(email)
    return render_template('validate_email.html', email=email, is_valid=is_valid)

# Function to validate email using regex
def validate_email_regex(email):
    regex_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(regex_pattern, email))








#####################################

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")


