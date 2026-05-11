# Software FJ - Sistema de Gestión Académica (UNAD)

Este proyecto es una aplicación de escritorio desarrollada en Python utilizando la librería `Tkinter`. Su objetivo es gestionar las reservas de salas de cómputo, alquiler de equipos de laboratorio y asesorías académicas especializadas.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.x
* **Interfaz Gráfica:** Tkinter (Customized UI)
* **Persistencia:** Sistema de Logs (logging) y Memoria Volátil.

## 🧬 Conceptos de Programación Orientada a Objetos (POO) Aplicados
El software cumple con los requisitos académicos de la UNAD implementando:
* **Clases Abstractas:** Definición de moldes base para Entidades y Servicios.
* **Herencia:** Las clases `Sala`, `Equipo` y `Asesoria` heredan de la clase base `Servicio`.
* **Polimorfismo:** Cada tipo de servicio calcula su costo de manera diferente (descuentos para equipos e IVA para asesorías).
* **Encapsulamiento:** El atributo `email` del cliente está protegido y se valida mediante decoradores `@property`.
* **Manejo de Excepciones:** Validaciones estrictas para evitar correos inválidos o registros con tiempo en cero.

## 🚀 Funcionalidades
1. **Registro de Reservas:** Selección por listas desplegables (UX mejorada).
2. **Validación de Parámetros:** Impide el registro de 0 días y 0 horas.
3. **Módulo de Reportes:** Visualización en tiempo real mediante un `Treeview`.
4. **Modificación y Borrado:** Gestión completa de los registros con confirmación de seguridad.
5. **Auditoría:** Generación automática de un archivo `.log` con los movimientos del sistema.

## 📋 Requisitos para ejecución
Solo necesitas tener instalado Python. Ejecuta el programa con:
```bash
python nombre_de_tu_archivo.py
