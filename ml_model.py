import pandas  as pd


from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split

from sklearn.svm import SVC


df = pd.read_csv('healthcare-dataset-stroke-data.csv')


df['bmi'] = df['bmi'].fillna(df['bmi'].mean())
ordinal_encoder = OrdinalEncoder()
columns_to_encode = ('gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status')
for column in columns_to_encode:
    df_column_encoded = ordinal_encoder.fit_transform(df[[column]])
    df[[column]] = df_column_encoded


X = df.drop(columns=['stroke', 'ever_married', 'work_type', 'Residence_type', 'id'])
Y = df['stroke']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.25)

keys = list(X.keys())



svc = SVC()
svc.fit(x_train,y_train)

def predictStroke(data):
    global svc
    df = dataToDf(data)
    result = svc.predict(df)
    print(result[0])
    return result[0]

def dataToDf(data):
 #  saveQuest(id, genero, idade, imc, glicose, fumante, hipertensao, cardio)
    global keys
    dictio = {}
    for i in range(len(data)):
        dictio[keys[i]] = data[i]
    print(dictio)
    df = pd.DataFrame(dictio, index=[0])
    return df