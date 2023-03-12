import pandas as pd
import matplotlib.pyplot as plt

try:
    # Leer archivo csv
    df = pd.read_csv('finanzas20202.csv')

    # Comprobar que el archivo tenga 12 columnas
    if len(df.columns) != 12:
        print(len(df.columns))
        raise ValueError('El archivo debe tener 12 columnas, una para cada mes del año')

    # Comprobar contenido en cada mes
    for col in df.columns[1:]:
        if df[col].isnull().all():
            raise ValueError(f'El mes {col} esta vacio')

    # Comprobar que todos los datos sean numéricos
    if not pd.to_numeric(df.iloc[:, 1:].stack(), errors='coerce').notnull().all():
        raise ValueError('Algunos datos no son numéricos')

except FileNotFoundError:
    print('El archivo no existe')

except ValueError as e:
    print(e)

else:
    # Realizar los cálculos solicitados
    suma_por_mes = df.sum()
    mes_gasto_maximo = suma_por_mes[suma_por_mes == suma_por_mes.min()].index[0]
    mes_ahorro_maximo = suma_por_mes[suma_por_mes == suma_por_mes.max()].index[0]
    media_anual = df.mean().mean()
    gastos_total_anual = df[df < 0].sum().sum()
    ingresos_total_anual = df[df > 0].sum().sum()

    # Grafico
    df[df > 0].sum().plot(label='Ingresos')
    df[df < 0].apply(lambda x: x.abs()).sum().plot(label='Gastos')
    plt.xlabel('Mes')
    plt.ylabel('Monto')
    plt.title('Evolución de ingresos y gastos por mes')
    plt.legend()
    plt.show()