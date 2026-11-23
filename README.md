# Planificador de Capacitaciones

Aplicación de consola (CLI) desarrollada en Python para calcular, desglosar y evaluar financieramente los costes de una capacitación empresarial frente a un presupuesto asignado, aplicando diseño modular mediante funciones.

---

## Objetivo de aprendizaje

Consolidar el **Principio 3: Funciones, parámetros y alcance de variables**:
- Descomposición de un problema de negocio en funciones pequeñas con una única responsabilidad.
- Transmisión explícita de información mediante **parámetros** y **valores de retorno** (`return`), eliminando la dependencia de variables globales.
- Uso combinado de **argumentos posicionales**, **argumentos por nombre** (*keyword arguments*) y **parámetros con valores predeterminados**.
- Aplicación de **composición de funciones**, encadenando el resultado devuelto por una función como entrada de la siguiente.
- Gestión estricta del **alcance local** (*local scope*) de las variables dentro de cada función.

---

## Mapa de Principios de la Saga Python 2026

- [X] **Principio 1. Fundamentos del lenguaje Python**
- [X] **Principio 2. Control de flujo y estructuras de datos básicas**
- [X] **Principio 3. Funciones, parámetros y alcance de variables**
- [ ] Principio 4. Manejo de errores y excepciones
- [ ] Principio 5. Comprensiones y código idiomático de Python
- [ ] Principio 6. Calidad del código y convenciones profesionales
- [ ] Principio 7. Programación Orientada a Objetos (POO)
- [ ] Principio 8. Complejidad algorítmica y análisis de eficiencia
- [ ] Principio 9. Módulos, paquetes y reutilización de código
- [ ] Principio 10. PIP, entornos virtuales y dependencias
- [ ] Principio 11. Aplicaciones CRUD y persistencia de datos
- [ ] Principio 12. Testing y validación automatizada
- [ ] Principio 13. Estadística computacional, simulación y programación dinámica
- [ ] Principio 14. Arquitectura de proyectos y distribución de paquetes
- [ ] Principio 15. Principios SOLID y patrones de diseño

---

## Funcionalidades principales

1. **Validación de entradas:** Control de importes positivos, cantidad entera de participantes y rango porcentual `[0, 100]`.
2. **Cálculo financiero modular:** Obtención independiente del coste bruto, descuento aplicado, coste final y coste unitario final por participante.
3. **Evaluación presupuestaria:** Comparación del coste final contra el presupuesto disponible para determinar si está dentro del presupuesto, utilizado al 100 % o en exceso.
4. **Resumen estructurado:** Presentación clara en consola con redondeo a dos decimales.

---

## Estructura del repositorio

```text
2026_11_P03_R02_planificador-capacitaciones/
├── .gitignore
├── main.py
└── README.md