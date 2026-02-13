# Importando la librería Pandas
import pandas as pd

# Importando el archivo .csv llamado "customers" y convirtiendo a DataFrame
clientes_df = pd.read_csv('customers.csv')

# Examinando el nombre de las columnas y información básica 
clientes_df.info()

# Traduciendo el nombre de las columnas
clientes_df.rename(columns = {
    'customer_id' : 'Cliente ID',
    'signup_date' : 'Fecha de Registro',
    'country' : 'País',
    'age' : 'Edad',
    'gender' : 'Género',
    'loyalty_tier' : 'Nivel de Lealtad',
    'acquisition_channel' : 'Canal de Adquisición'
}, inplace = True)

# Creando un diccionario ampliable con los valores de las columnas a traducir 
c_traduccion = {
    'País' : {
        'AU' : 'Australia',
        'BR' : 'Brasil',
        'CA' : 'Canadá',
        'DE' : 'Alemania',
        'IN' : 'India',
        'UK' : 'Reino Unido',
        'US' : 'Estados Unidos' 
    },
    'Género' : {
        'Male' : 'Masculino',
        'Female' : 'Femenino'
    },
    'Nivel de Lealtad' : {
        'Bronze' : 'Bronce',
        'Silver': 'Plata',
        'Gold' : 'Oro'
    },
    'Canal de Adquisición' : {
        'Organic' : 'Orgánico',
        'Paid Search' : 'Búsqueda paga',
        'Referral' : 'Referencia'
    }
}

# Iterando el diccionario para asignar a cada columna, sus claves y valores
for col, dic in c_traduccion.items():
    clientes_df[col].replace(dic, inplace = True)
    
# Convirtiendo el DataFrame a un nuevo archivo .csv traducido
clientes_df.to_csv('Clientes.csv')
