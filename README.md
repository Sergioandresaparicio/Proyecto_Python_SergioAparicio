---

# 📊 Simulador de Gasto Diario – Análisis Estructurado

## 📌 Problema

Muchos usuarios desean llevar un registro de sus gastos, pero las aplicaciones de gestión financiera completas pueden ser complicadas y requieren configuraciones avanzadas. Este proyecto ofrece una solución simple y accesible para quienes buscan hacer un seguimiento básico de sus gastos en un formato amigable y sin demasiadas complejidades.

El **Simulador de Gasto Diario** permite:
- Registrar y monitorear gastos diarios en distintas categorías (comida, transporte, entretenimiento, etc.).
- Obtener resúmenes por período (diario, semanal, mensual) y por categoría.
- Mantener un historial persistente entre sesiones mediante un archivo **JSON**. tarea 1 mirar como anidar diccionarios en .json

---

## 🎯 Objetivo

Desarrollar una **aplicación de consola en Python** que permita a los usuarios:
- Registrar nuevos gastos con categoría, monto y descripción opcional(if).
- Consultar y filtrar su historial de gastos print(con coordenadas).
- Calcular totales por período y categoría.
- Generar reportes claros y útiles.
- Guardar y cargar datos automáticamente usando un archivo `gastos.json`.

---

## 🧩 Variables del Sistema

| Nombre          | Descripción                                            | Tipo de dato          | Entrada/Salida                               |
| --------------- | ------------------------------------------------------ | --------------------- | -------------------------------------------- |
| `fecha`         | Fecha del gasto (`YYYY-MM-DD`)                         | Cadena                | Entrada (I) Tomada por el sistema datetime() |
| `monto`         | Cantidad gastada (valor positivo)                      | Real                  | Entrada (I) USUARIO input()                  |
| `categoria`     | Tipo de gasto (ej. comida, transporte)                 | Cadena                | Entrada (I) USUARIO CATEGORÍAS PREDEFINIDAS  |
| `descripcion`   | Nota opcional sobre el gasto                           | Cadena                | Entrada (I, opcional)                        |
| `gastos`        | Lista de todos los gastos registrados                  | Lista de diccionarios | Interno                                      |
| `total_diario`  | Suma de gastos del día actual                          | Real                  | Salida (O)                                   |
| `total_semanal` | Suma de gastos de los últimos 7 días                   | Real                  | Salida (O)                                   |
| `total_mensual` | Suma de gastos del mes actual                          | Real                  | Salida (O)                                   |
| `reporte`       | Resumen estructurado de gastos por período y categoría | Diccionario           | Salida (O)                                   |

```python
from datetime import date
hoy=date.today()
print(hoy)
```



---

## 📏 Reglas de Negocio

1. **Registro de gasto**:
   - El `monto` debe ser **mayor que 0**.
   - La `fecha` puede ingresarse manualmente o tomarse como la fecha actual si no se especifica.
   - La `categoria` es obligatoria; la `descripcion` es opcional.

2. **Categorías sugeridas** (no restrictivas):
   - Comida
   - Transporte
   - Entretenimiento
   - Servicios
   - Salud
   - Otros

3. **Cálculo de períodos**:
   - **Diario**: gastos con fecha igual a hoy.
   - **Semanal**: gastos desde hace 7 días hasta hoy (inclusive).
   - **Mensual**: gastos cuya fecha coincide en año y mes con el mes actual.

4. **Reporte**:
   - Debe incluir:
     - Total general acumulado.
     - Totales por período (diario, semanal, mensual).
     - Desglose por categoría.
   - Puede mostrarse en consola o guardarse en un archivo `reporte.json`.

---

## ⚠️ Restricciones y Validaciones

- No se permiten montos ≤ 0.
- Las fechas deben seguir el formato `YYYY-MM-DD`. Si no se proporcionan, se usa la fecha del sistema.
- El archivo `gastos.json`:
  - Se crea automáticamente si no existe.
  - Se carga al iniciar el programa.
  - Se sobrescribe cada vez que se registra un nuevo gasto.
- En esta versión **no se implementa edición ni eliminación** de gastos (solo registro y consulta).

---

## 🔧 Funcionalidades Principales

### 1. **Registrar Gasto**
- Solicita: monto, categoría, descripción (opcional), fecha (opcional).
- Valida los datos.
- Agrega el gasto a la lista interna y guarda en `gastos.json`.

### 2. **Listar Gastos**
- Muestra todos los gastos con sus detalles.
- Opciones de filtro:
  - Por categoría (ej. `"transporte"`).
  - Por rango de fechas (ej. del `2026-01-01` al `2026-01-21`).

### 3. **Calcular Totales**
- Calcula y muestra:
  - Gasto total acumulado.
  - Gasto diario, semanal y mensual.
  - Desglose por categoría (ej. `"Comida: $85.000"`).

### 4. **Generar Reporte**
- Crea un resumen estructurado como:
  ```json
  {
    "fecha_reporte": "2026-01-21",
    "total_general": 210000.0,
    "periodos": {
      "diario": 25000.0,
      "semanal": 95000.0,
      "mensual": 210000.0
    },
    "por_categoria": {
      "comida": 70000.0,
      "transporte": 45000.0,
      "entretenimiento": 95000.0
    }
  }
  ```
- Opción: mostrar en pantalla o guardar en `reporte.json`.

### 5. **Guardar y Cargar Datos**
- Al iniciar: carga `gastos.json` si existe.
- Al registrar: actualiza `gastos.json` inmediatamente.

---

## 💾 Estructura de Datos (Ejemplo)

**Archivo:** `gastos.json`
```json
[
  {
    "fecha": "2026-01-20",
    "monto": 15000.0,
    "categoria": "comida",
    "descripcion": "Almuerzo en restaurante"
  },
  {
    "fecha": "2026-01-21",
    "monto": 8000.0,
    "categoria": "transporte",
    "descripcion": "Pasaje de bus"
  }
]
```

---

## 🛠️ Requisitos Técnicos

- **Lenguaje**: Python 3.x
- **Módulos estándar utilizados**:
  - `json`: para persistencia de datos.
  - `datetime`: para manejo de fechas.
  - `os`: para verificar existencia de archivos.
- **Arquitectura modular recomendada**:
  ```
  simulador_gasto/
  ├── main.py          # Menú principal
  ├── registro.py      # Registrar nuevos gastos
  ├── consulta.py      # Listar y filtrar gastos
  ├── reporte.py       # Calcular y generar reportes
  └── archivo.py       # Guardar/cargar JSON
  ```

---

## 📤 Entregables Esperados

1. Repositorio en GitHub llamado:  
   `SimuladorGastoDiario_ApellidoNombre`  
   (ej. `SimuladorGastoDiario_AparicioSergio`)
2. Archivos incluidos:
   - Código fuente modularizado en Python.
   - `gastos.json` (generado al usar la app).
   - `README.md` con instrucciones de ejecución.
3. Funcionalidades completas según este análisis.

---

¿Te gustaría que ahora generemos el código base en Python siguiendo esta estructura? Podemos empezar con el menú y el registro de gastos.