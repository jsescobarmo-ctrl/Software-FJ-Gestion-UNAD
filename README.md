# Software FJ - Gestión Académica UNAD

Sistema práctico para el control de préstamos de salas, equipos de laboratorio y agendamiento de asesorías académicas. Desarrollado como proyecto para el curso de Programación Orientada a Objetos.

## Especificaciones Técnicas
El proyecto corre sobre Python 3.x y utiliza Tkinter para la interfaz gráfica. Los datos se gestionan en memoria durante la ejecución y se genera un archivo .log automático para auditar los movimientos del sistema.

## Implementación de POO
Para este desarrollo se aplicaron los pilares fundamentales de la programación orientada a objetos:
- **Abstracción:** Uso de clases base para definir la estructura de servicios y entidades.
- **Herencia y Polimorfismo:** Las categorías (Sala, Equipo, Asesoría) heredan de una clase padre pero implementan su propia lógica de costos (cálculo de IVA o descuentos según el caso).
- **Encapsulamiento:** Protección de datos sensibles del usuario mediante el uso de atributos privados y decoradores.
- **Lógica de Excepciones:** Control de errores en tiempo real para evitar registros inválidos o con tiempos en cero.

## Qué hace el programa
1. Permite registrar reservas validadas por correo.
2. Gestión de tiempos mediante selectores (evita errores de escritura).
3. Panel de reportes con vista de tabla (Treeview).
4. Herramientas para editar o eliminar registros con avisos de confirmación.
5. Historial de auditoría en archivo externo.

## Ejecución
Asegúrate de tener Python instalado y lanza el script con:
`python taller4.py`
