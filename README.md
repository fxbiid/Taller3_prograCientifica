# Laboratorio 3 - API REST y Aplicación Streamlit
## Programación Científica

<br>

<table>
  <tr>
    <td><b>Integrantes</b></td>
    <td>Francisco Cortés · Fabián Díaz · Ignacia Peña</td>
  </tr>
  <tr>
    <td><b>Asignatura</b></td>
    <td>Programación Científica</td>
  </tr>
  <tr>
    <td><b>Profesor</b></td>
    <td>Cristhian Alberto Rabi Reyes</td>
  </tr>
  <tr>
    <td><b>Ayudante</b></td>
    <td>Roberto Javier Fernández Berrios</td>
  </tr>
  <tr>
    <td><b>Universidad</b></td>
    <td>Universidad Católica del Norte</td>
  </tr>
  <tr>
    <td><b>Sede</b></td>
    <td> Guayacan Coquimbo, Chile</td>
  </tr>
  <tr>
    <td><b>Fecha de entrega</b></td>
    <td>7 de julio de 2026</td>
  </tr>
</table>

<br>

---

# Descripción

Este laboratorio consiste en el desarrollo de una aplicación cliente-servidor para el análisis interactivo del corpus bíblico.

El sistema se divide en dos componentes principales:

- Una **API REST** desarrollada con **FastAPI**, encargada de realizar todo el procesamiento de los datos.
- Una aplicación desarrollada en **Streamlit**, encargada únicamente de consumir la API y visualizar los resultados.

Siguiendo los requerimientos del laboratorio, todas las operaciones de procesamiento, filtrado, búsqueda semántica, reducción de dimensionalidad y generación de texto son realizadas por la API, mientras que Streamlit actúa únicamente como interfaz gráfica.

---

# Objetivos

- Implementar una API REST para el procesamiento del corpus bíblico.
- Construir una aplicación interactiva utilizando Streamlit.
- Implementar un dashboard con filtros dinámicos.
- Implementar un buscador semántico utilizando TF-IDF.
- Visualizar representaciones vectoriales mediante PCA y Word2Vec.
- Implementar un generador de texto basado en modelos de N-Gramas.

---

# Tecnologías utilizadas

- Python 3
- FastAPI
- Uvicorn
- Streamlit
- Pandas
- NumPy
- Plotly
- WordCloud
- Scikit-Learn
- gensim
- Requests

---

# Estructura del proyecto

```
Taller3Progra
│
├── api
│   ├── routes
│   │   ├── dashboard.py
│   │   ├── search.py
│   │   ├── pca.py
│   │   └── generator.py
│   │
│   ├── cache.py
│   ├── services.py
│   └── main.py
│
├── codigo
│   ├── bibliaDataset.py
│   ├── buscadorSemantico.py
│   ├── generadorNGramas.py
│   ├── similitudDelCoseno.py
│   ├── textPreprocesamiento.py
│   ├── tfIdf.py
│   ├── visualizacionPca.py
│   └── word2vec.py
│
├── data
│   ├── key_english.csv
│   └── t_kjv.csv
│
├── streamlit
│   ├── Inicio.py
│   └── pages
│       ├── Dashboard.py
│       ├── Buscador.py
│       ├── Visualizador.py
│       └── Generador.py
│
└── requirements.txt
```

---

# Instalación

Clonar el repositorio

```bash
git clone https://github.com/fxbiid/Taller3_prograCientifica.git
```

Entrar al proyecto

```bash
cd Taller3_prograCientifica
```

Crear entorno virtual

```bash
python -m venv .venv
```

Activar entorno

Windows

```bash
.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecución

## Levantar la API

```bash
uvicorn api.main:Inicio --reload
```

La API estará disponible en

```
http://127.0.0.1:8000
```

Documentación Swagger

```
http://127.0.0.1:8000/docs
```

---

## Levantar Streamlit

En otra terminal

```bash
streamlit run streamlit/Inicio.py
```

La aplicación estará disponible en

```
http://localhost:8501
```

---

# Funcionalidades

## Dashboard

El dashboard permite visualizar información estadística del corpus bíblico.

Incluye:

- Cantidad de versículos.
- Cantidad de versículos por libro.
- Longitud promedio por libro.
- Top de palabras más frecuentes.
- Nube de palabras.

Además incorpora filtros por:

- Testamento
- Libro
- Capítulo

Todos los filtros son procesados por la API.

---

## Buscador Semántico

Permite ingresar una consulta de texto.

La API:

- Preprocesa la consulta.
- Calcula el vector TF-IDF.
- Calcula similitud del coseno.
- Devuelve los versículos más similares.

La aplicación Streamlit únicamente muestra la tabla con los resultados obtenidos.

---

## Visualizador PCA y Word2Vec

La aplicación permite visualizar la representación vectorial de los versículos.

Se puede seleccionar:

**Modelo**

- TF-IDF
- Word2Vec

**Dimensiones**

- 2D
- 3D

**Cantidad de versículos** a visualizar.

Toda la reducción de dimensionalidad es realizada por la API.

---

## Generador de Texto

Se implementó un generador de texto basado en modelos de N-Gramas.

El usuario puede ingresar un texto inicial y la API genera automáticamente la continuación utilizando el modelo entrenado sobre el corpus bíblico.

---

# Arquitectura

El proyecto sigue una arquitectura cliente-servidor.

```
                Usuario
                   │
                   ▼
             Streamlit (Frontend)
                   │
             Solicitudes HTTP
                   │
                   ▼
             FastAPI (Backend)
                   │
     ┌─────────────┼─────────────┐
     │             │             │
 Dashboard   Buscador      Generador
     │             │             │
     └─────────────┼─────────────┘
                   │
             Procesamiento NLP
                   │
                   ▼
            Corpus de la Biblia
```

---

# Organización del código

## api/

Contiene toda la lógica relacionada con FastAPI.

- Endpoints
- Caché
- Servicios
- Configuración de la API

---

## codigo/

Contiene la implementación de los algoritmos desarrollados durante los laboratorios.

Entre ellos:

- TF-IDF
- Similitud del coseno
- PCA
- Word2Vec
- Buscador semántico
- Generador mediante N-Gramas

---

## streamlit/

Implementa la interfaz gráfica.

Cada página consume directamente los endpoints de la API sin realizar procesamiento adicional.

---

# Resultados

La aplicación permite:

- Explorar el corpus bíblico mediante filtros.
- Buscar versículos utilizando similitud semántica.
- Visualizar representaciones vectoriales mediante PCA.
- Comparar representaciones TF-IDF y Word2Vec.
- Generar texto automáticamente utilizando modelos de N-Gramas.
- Consumir todos los servicios mediante una interfaz desarrollada en Streamlit.

---

# Conclusiones

Durante este laboratorio se implementó una arquitectura cliente-servidor donde la API concentra todo el procesamiento del lenguaje natural y Streamlit se utiliza únicamente como interfaz de visualización.

Esta separación permitió reutilizar los algoritmos desarrollados previamente e integrar nuevas funcionalidades como la búsqueda semántica, las visualizaciones mediante PCA y Word2Vec y la generación automática de texto, obteniendo una aplicación interactiva que cumple con los requerimientos del laboratorio.

---
