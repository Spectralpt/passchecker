from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key= "miguel"

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        password = request.form["pass"]
        password_check(password)
        return render_template("index.html") 
    else:
        return render_template("index.html")


def password_check(password):
            lengthCheck = 0
            numCheck = 0
            upCaseCheck = 0
            lowCaseCheck = 0
            specialCharCheck = 0

            #checks password length lengthCheck meanings:
            # 0 -> password too short
            # 1-> password too long
            # 2- password between expected values

            if 6 > len(password):
                lengthCheck = 0  
            elif 20 < len(password):
                lengthCheck = 1
            else:
                lengthCheck = 2

            #checks for numbers, lower and upper case letters in the password by breaking down the orginal string into a list and checking individually

            charList = list(password)
            for char in charList:
                if char.isdecimal() == True:
                    numCheck += 1

                if char.isalpha() == True:
                    if char.isupper() == True:
                        upCaseCheck +=1
                    if char.islower() == True:
                        lowCaseCheck +=1
                
                if char.isalpha() == False and char.isdecimal() == False:
                    specialCharCheck += 1

                
            #output handling     
            if lengthCheck == 0:
                flash('A tua palavra-passe é muito curta.', 'error')
            elif lengthCheck == 1:
                flash('A tua palavra-passe é muito longa.', 'error')
            elif lengthCheck == 2:
                flash('A tua palavra-passe tem o comprimento correto.', 'success')

            #The conditions are separate in different if statements because in this case we want to be able to display all the erros that occurred
            if lowCaseCheck == 0 and upCaseCheck == 0:
                flash('Your password must inlcude letters.', 'error')
            elif lowCaseCheck == 0: #and upCaseCheck > 0:
                flash('Your password must include lower case letters.', 'error')
            elif upCaseCheck == 0: #and lowCaseCheck > 0:
                flash('Your password must include upper case letters.', 'error')

            if numCheck == 0:
                flash ('Your password must include numbers.', 'error')

            if specialCharCheck == 0:
                flash('Your password must include a special character.', 'error')

            if numCheck != 0:
                flash('Your password has numbers.', 'success')

            if lowCaseCheck != 0:
                flash('Your password has lowercase letters.', 'success')

            if upCaseCheck != 0:
                flash('Your password has upper case letters.', 'success')
                
            if specialCharCheck != 0:
                flash('Your password has special characters.', 'success')



if __name__ == '__main__':
    app.run(debug=True)