import psycopg2

def saveCadast(name, email,password):
    #funcao para salvar coisas no db
    conn = psycopg2.connect(user="fwwfeyeq", password="ig8jueP3mYT6uWQKXPKvNFHBJcln4NPg", host="isilo.db.elephantsql.com", port="5432")
    try:
        cur = conn.cursor() 
        cur.execute( '''INSERT INTO usuário 
        (nome, email, senha) VALUES (%s, %s, %s)''', 
        (name, email, password)) 
        #Salvar mudanças
        conn.commit() 
        cur.execute("SELECT * FROM usuário WHERE email='" + email + "'")
        row = cur.fetchone()
        if row:
            id_to_use = row[0]
        conn.commit() 
        cur.close() 
        conn.close()
        return id_to_use
    except psycopg2.Error as e:
        pass

def saveQuest(id_to_use, genero, idade, imc, glicose, fumante, hipertensao, cardio):
    conn = psycopg2.connect(user="fwwfeyeq", password="ig8jueP3mYT6uWQKXPKvNFHBJcln4NPg", host="isilo.db.elephantsql.com", port="5432")
    try:
        cur = conn.cursor() 
        cur.execute('''INSERT INTO public."questionário"(
	    id, genero, idade, hipertensao, doenca_cardiovascular, indice_glicose, imc, condicao_fumante) VALUES (%s, %s, %s,%s, %s, %s, %s, %s);''', (id_to_use, genero, idade, hipertensao, cardio, glicose, imc, fumante))
        conn.commit() 
        cur.close() 
        conn.close()
    except psycopg2.Error as e:
        pass

def validateCredentials(email,senha):
    #validar login e senha no banco de dados
    conn = psycopg2.connect(user="fwwfeyeq", password="ig8jueP3mYT6uWQKXPKvNFHBJcln4NPg", host="isilo.db.elephantsql.com", port="5432")
    try:
        cur = conn.cursor()
        cur.execute("SELECT (email, senha) FROM usuário WHERE email='" + email + "' and senha= '" + senha + "'")
        value = cur.fetchone()
        if value != None:
            return True
        else:
            return False
    except:
        pass


def searchResult(email,senha):
    pass