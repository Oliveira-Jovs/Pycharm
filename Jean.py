import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV

# Carregar os dados do arquivo Excel
base = pd.read_excel('C:/Users/Oliveira/Downloads/attualizade.xlsx')
print(base.shape)

# Remover a coluna 'Unnamed: 0'
base = base.drop('Unnamed: 0', axis=1)
print(base.shape)

# Dividir os dados em X e y
X = base.iloc[:, 1:14].values
y = base.iloc[:, 14].values

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Padronizar os dados de treino e teste
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# Definir os valores de hiperparâmetros para o modelo SVR
params = {'C': [1e5, 1, 1], 'gamma': [0.000001, 0.1, 1]}

# Treinar o modelo SVR com os dados de treino e os hiperparâmetros escolhidos
svr = SVR(kernel='rbf')
grid_search = GridSearchCV(svr, params, cv=5)
grid_search.fit(X_train_std, y_train)

# Avaliar o desempenho do modelo treinado usando os dados de teste
y_pred = grid_search.predict(X_test_std)
mse = mean_squared_error(y_test, y_pred)

# Imprimir os resultados
print('Score:', grid_search.score(X_test_std, y_test))
print('MSE:', mse)
print('Melhor valor de gamma:', grid_search.best_params_['gamma'])
print('Melhor valor de C:', grid_search.best_params_['C'])
