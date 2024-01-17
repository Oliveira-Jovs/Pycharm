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

# Carregar seus dados em X e y
X = base.iloc[:, 1:14].values
y = base.iloc[:, 14].values
from sklearn.model_selection import GridSearchCV


# Separar os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Padronizar os dados de treino e teste
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# Escolher os valores de hiperparâmetros para o modelo SVR
params = {'C': [1e5, 1, 1], 'gamma': [0.000001, 0.1, 1]}

# Treinar o modelo SVR com os dados de treino e os hiperparâmetros escolhidos
svr = SVR(kernel='rbf')
grid_search = GridSearchCV(svr, params, cv=5)
t = grid_search.fit(X_train_std, y_train)

# Avaliar o desempenho do modelo treinado usando os dados de teste
y_pred = grid_search.predict(X_test_std)
mse = mean_squared_error(y_test, y_pred)


print('t.score(X_test_std, y_test)', t.score(X_test_std, y_test))

print('mse',mse)

print('grid_search.best_params_[gamma]',grid_search.best_params_['gamma'])

print('grid_search.best_params_[C]',grid_search.best_params_['C'])