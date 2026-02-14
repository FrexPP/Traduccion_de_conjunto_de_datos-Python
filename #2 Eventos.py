# Importando el archivo .csv llamado "events" y convirtiendo a DataFrame
eventos_df = pd.read_csv('events.csv')

# Eliminando columnas irrelevantes

# Debido a que esta tabla contiene unas columnas irrelevantes para este proyecto, se eliminan.
eventos_df.drop(columns = ['campaign_id', 'experiment_group'], axis = 1, inplace = True)

# Examinando el nombre de las columnas y información básica 
eventos_df.info()

# Traduciendo el nombre de las columnas
eventos_df.rename(columns = {
    'event_id' : 'Evento ID',
    'timestamp' : 'Marca de Tiempo',
    'customer_id' : 'Cliente ID',
    'session_id' : 'Sesión ID',
    'event_type' : 'Tipo de Evento',
    'product_id' : 'Producto ID',
    'device_type' : 'Tipo de Dispositivo',
    'traffic_source' : 'Tipo de Tráfico',
    'page_category' : 'Categoría de Página',
    'session_duration_sec' : 'Duración de Sesión (seg)'
}, inplace = True)

# Creando un diccionario ampliable con los valores de las columnas a traducir

# La columna "Tipo de Tráfico" contenía valores con inicial mayúscula y otras de mayúsculas sostenidas
# que significaban lo mismo. Estos valores se normalizaron.
e_traduccion = {
    'Tipo de Evento' : {
        'view' : 'Vista',
        'add_to_cart' : 'Agregar al carrito',
        'purchase' : 'Compra',
        'click' : 'Click',
        'bounce' : 'Rebote'
    },
    'Tipo de Dispositivo' : {
        'desktop' : 'Computadora',
        'mobile' : 'Móvil',
        'tablet' : 'Tablet'
    },
    'Tipo de Tráfico' : {
        'Organic' : 'Orgánico',
        'ORGANIC' : 'Orgánico',
        'Paid Search' : 'Búsqueda paga',
        'PAID SEARCH': 'Búsqueda paga',
        'Direct' : 'Directo',
        'DIRECT' :'Directo',
        'EMAIL' : 'Email',
        'SOCIAL' : 'Social'
    },
    'Categoría de Página' : {
        'Home' : 'Inicio',
        'PLP' : 'Página listado de productos',
        'PDP' : 'Página detalle de producto',
        'Cart' : 'Carrito',
        'Checkout' : 'Proceso de pago'
    }
}

# Iterando el diccionario para asignar a cada columna, sus claves y valores
for col, dic in e_traduccion.items():
    eventos_df[col].replace(dic, inplace = True)
    
# Como noté que algunos valores eran nulos, busqué el porcentaje de valores nulos por columna
(eventos_df.isna().mean()) * 100
# La columna "Producto ID" contenía un 10% de valores nulos, esto no es un error debido a que no todas
# las categorías de página cuentan con un producto específico.
# La columna "Tipo de Dispositivo" contenía un 2% de valores nulos, esto sí podría ser un problema y decidí remarcarlo.

# Reemplazando los valores nulos de "Tipo de Dispositivo" para remarcarlos
eventos_df['Tipo de Dispositivo'].fillna('Desconocido', inplace = True)

# Convirtiendo el DataFrame a un nuevo archivo .csv traducido
eventos_df.to_csv('Eventos.csv')
