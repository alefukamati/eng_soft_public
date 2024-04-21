from flask import Flask,render_template, request, redirect, url_for, flash, session
from ml_model import predictStroke 
#from db import saveCadast, saveQuest, validateCredentials
from txt import saveCadast, saveResult, validateCredentials, searchResult

#funcao predictStroke(lista) recebe o argumento lista com a lista dos valores coletados no questiionario
#ela vai retornar o resultado da classificacao

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("homepage.html")


#@app.route('/login', methods=['GET']) #talvez nao precise
#def login():
 #   return render_template('login.html')

@app.route('/login', methods=['GET', 'POST']) #talvez nao precise
def login():
    if request.method == 'GET': 
        return render_template('login.html')
    elif request.method == 'POST':
        email, password = request.form['emailLogin'], request.form['senhaLogin'] #recebe email e senha
        valid = validateCredentials(email,password)
        if valid == True: 
            result = searchResult(email)
            if result == None: return redirect(url_for('quest'))
            return redirect(url_for('results', result = result))
        if valid == False:
            error = "Login e/ou senha incorretos!" 
            return render_template('login.html', error = error)
        

@app.route('/resultados', methods=['GET'])
def results():
    result = request.args['result']
    saveResult(result)
    result = str(result)[0]
    return render_template('resultados.html', result = result)


@app.route('/sendRegister', methods=['GET','POST'])
def sendRegister():
    name = request.form['nome']
    email = request.form['email']
    password = request.form['senha'] 
    password_confirm = request.form['confirmarSenha'] #recebe email e senha
    if password != password_confirm:
        return render_template('login.html', error = 'Erro de confirmação de senha!')
    else: 
        #id = saveCadast(name, email, password)
        saveCadast(name, email, password)
        return redirect(url_for('quest'))
    

@app.route('/questionario', methods=['GET', 'POST'])
def quest():
    if request.method == 'GET': return render_template('questionario.html')
    elif request.method == 'POST':
       # id = request.args['id']
        genero = request.form['genero']
        idade = request.form['input-idade']
        imc = request.form['input-imc']
        glicose = request.form['glicose']
        fumante = request.form['status-fumante']
        hipertensao = request.form['hipertensao']
        cardio = request.form['cardiovascular']
        data = [genero, idade, hipertensao, cardio, glicose,imc, fumante]
        result = predictStroke(data)
      #  saveQuest(id, genero, idade, imc, glicose, fumante, hipertensao, cardio)
        return redirect(url_for('results',
                                        result = result))



if __name__ == "__main__":
    app.run(debug=True)
