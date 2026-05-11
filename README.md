# Software FJ - Gestión Académica UNAD

Este proyecto nace como una solución práctica para apoyar la vida universitaria. Su propósito es facilitar el control de préstamos de salas, equipos de laboratorio y el agendamiento de asesorías académicas, ofreciendo una herramienta sencilla y confiable. Fue desarrollado como parte del curso de Programación Orientada a Objetos, integrando teoría y práctica en un entorno real.


## Especificaciones Técnicas

El sistema está construido en Python 3.x y utiliza Tkinter para la interfaz gráfica, lo que permite una experiencia visual amigable. Los datos se gestionan directamente en memoria durante la ejecución, y cada movimiento queda registrado en un archivo .log automático, garantizando transparencia y trazabilidad.


## Principios de POO aplicados

El desarrollo se fundamenta en los pilares de la programación orientada a objetos:

* Abstracción: Se definieron clases base que estructuran los servicios y entidades del sistema.
* Herencia y Polimorfismo: Las categorías (Sala, Equipo, Asesoría) heredan de una clase padre, pero cada una implementa su propia lógica de costos, incluyendo cálculos de IVA o descuentos.
* Encapsulamiento: Los datos sensibles de los usuarios se protegen mediante atributos privados y decoradores.
* Manejo de Excepciones: Se incorporó control de errores en tiempo real para evitar registros inválidos o inconsistencias en los tiempos.


## Funcionalidades principales

El programa ofrece herramientas que simplifican la gestión académica:

1. Registro de reservas validadas por correo electrónico.
2. Selección de tiempos mediante controles gráficos, reduciendo errores de escritura.
3. Panel de reportes con vista en tabla (Treeview).
4. Opciones para editar o eliminar registros, siempre con confirmación previa.
5. Historial de auditoría almacenado en un archivo externo.


## Ejecución

Para poner en marcha el sistema, basta con tener instalado Python y ejecutar el script con:

`python taller4.py`
