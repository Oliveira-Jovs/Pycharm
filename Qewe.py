import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

base = pd.read_excel('C:/Users/Oliveira/Downloads/attualizade.xlsx')
print(base.shape)
base = base.drop('Unnamed: 0', axis=1)
print(base.shape)
x = base.iloc[:, 1:14].values
y = base.iloc[:, 14].values
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV


# Carregar seus dados em X e y
X = base.iloc[:, 1:14].values
y = base.iloc[:, 14].values

# Separar os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Padronizar os dados de treino e teste
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Escolher os valores de hiperparâmetros para o modelo SVR
params = {'C': [100000.0], 'gamma': [1e-06], 'kernel': ['linear', 'rbf']}

# Treinar o modelo SVR com os dados de treino e os hiperparâmetros escolhidos
svr = SVR()

grid_search = GridSearchCV(svr, params, cv=5)
grid_search.fit(X_train, y_train)

# Avaliar o desempenho do modelo treinado usando os dados de teste
X_test_scaled = scaler.transform(X_test)
score= grid_search.score(X_test_scaled, y_test)


print(score)