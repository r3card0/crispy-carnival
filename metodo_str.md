# Método .str en pandas

En pandas, el método `.str` permite accesara submetodos usado como herramientas para modificar o buscar cadenas de textos en las columnas de pandas. A continuacion se presenta una tabla de los submétodos mas comunes:

Claro, aquí tienes una tabla clara y útil con algunos de los **métodos más comunes de `.str` en pandas**, con su **descripción** y un **ejemplo de uso** para cada uno:

---

### 🧾 Tabla de Métodos `.str` en pandas

| Método `.str`            | Descripción                                                  | Ejemplo de uso                            |
| ------------------------ | ------------------------------------------------------------ | ----------------------------------------- |
| `.str.lower()`           | Convierte todo el texto a minúsculas                         | `df['columna'].str.lower()`               |
| `.str.upper()`           | Convierte todo el texto a mayúsculas                         | `df['columna'].str.upper()`               |
| `.str.title()`           | Convierte a formato título (inicial en mayúscula)            | `df['columna'].str.title()`               |
| `.str.strip()`           | Elimina espacios al inicio y final                           | `df['columna'].str.strip()`               |
| `.str.len()`             | Devuelve la longitud (número de caracteres)                  | `df['columna'].str.len()`                 |
| `.str.replace(pat, rep)` | Reemplaza un patrón por otro                                 | `df['columna'].str.replace('a', 'x')`     |
| `.str.contains(pat)`     | Retorna `True/False` si encuentra el patrón                  | `df['columna'].str.contains('mx')`        |
| `.str.startswith(pat)`   | Retorna `True` si comienza con el patrón                     | `df['columna'].str.startswith('abc')`     |
| `.str.endswith(pat)`     | Retorna `True` si termina con el patrón                      | `df['columna'].str.endswith('xyz')`       |
| `.str.split(sep)`        | Divide el string usando un separador                         | `df['columna'].str.split('_')`            |
| `.str.extract(regex)`    | Extrae partes del texto usando una expresión regular (regex) | `df['columna'].str.extract(r'(\d+)')`     |
| `.str.get(i)`            | Obtiene el elemento en la posición `i` (después de `split`)  | `df['columna'].str.split('_').str.get(1)` |
| `.str.find(sub)`         | Retorna la posición donde aparece un substring               | `df['columna'].str.find('mx')`            |
| `.str.match(regex)`      | Verifica si el texto **empieza** con una expresión regular   | `df['columna'].str.match(r'^[a-z]+')`     |
| `.str.zfill(width)`      | Rellena con ceros a la izquierda hasta alcanzar un ancho     | `df['columna'].str.zfill(5)`              |

---

### 🧪 Ejemplo de contexto práctico:

```python
import pandas as pd

df = pd.DataFrame({
    'texto': ['  Hola Mundo  ', 'python_es_genial', 'MX_24xn0']
})

df['minusculas'] = df['texto'].str.lower()
df['sin_espacios'] = df['texto'].str.strip()
df['extraido'] = df['texto'].str.extract(r'(\d+)')
```
