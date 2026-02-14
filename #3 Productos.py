# Importando el archivo .csv llamado "products" y convirtiendo a DataFrame
productos_df = pd.read_csv('products.csv')

# Examinando el nombre de las columnas y información básica
productos_df.info()

# Traduciendo el nombre de las columnas
productos_df.rename(columns = {
    'product_id' : 'Producto ID',
    'category' : 'Categoría',
    'brand' : 'Marca',
    'base_price' : 'Precio Base',
    'launch_date' : 'Fecha de Lanzamiento',
    'is_premium' : 'Es Premium'
}, inplace = True)

# Creando un diccionario ampliable con los valores de las columnas que se puedan traducir de esta forma

# Si bien el valor binario de la columna "Es Premium" no necesariamente debía traducirse, lo hice para
# que sea más amigable para el consumo humano.
p_traduccion = {
    'Categoría' : { 
        'Grocery' : 'Comestibles',
        'Fashion' : 'Moda',
        'Electronics' : 'Electrónica',
        'Sports' : 'Deportes',
        'Beauty' : 'Belleza',
        'Home' : 'Hogar'
    },
    'Es Premium' : {
        0 : 'No Premium',
        1 : 'Premium'
    }
}

# Iterando el diccionario para asignar a cada columna, sus claves y valores
for col, dic in p_traduccion.items():
    productos_df[col].replace(dic, inplace = True)

# Traduciendo valores de la columna "Marca"

# Debido a que esta columna contenía como valores la palabra "Brand_" seguido del número identificador
# de la marca, esta necesitaba traducirse utilizando el método ".replace()" con el parámetro "regex = True".
productos_df['Marca'].replace('Brand_', 'Marca ', regex = True, inplace = True)

# Convirtiendo el DataFrame a un nuevo archivo .csv traducido
productos_df.to_csv('Productos.csv')
