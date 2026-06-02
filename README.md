# Detalles del Proyecto: Sistema de Gestión de Inventario y Préstamos (MJ)

## Tabla de Contenido
1. [Descripción General del Software](#descripción-general-del-software)
2. [Objetivos del Proyecto](#objetivos-del-proyecto)
    * [Objetivo General](#objetivo-general)
    * [Objetivos Específicos](#objetivos-específicos)
3. [Beneficios del Sistema](#beneficios-del-sistema)
4. [Requisitos Funcionales (RF)](#requisitos-funcionales-rf)
    * [Módulo de Gestión de Usuarios y Artículos](#módulo-de-gestión-de-usuarios-y-artículos)
    * [Módulo de Transacciones (Préstamos y Devoluciones)](#módulo-de-transacciones-préstamos-y-devoluciones)
    * [Módulo de Alertas, Penalizaciones y Administración](#módulo-de-alertas-penalizaciones-y-administración)
5. [Requisitos No Funcionales (RNF)](#requisitos-no-funcionales-rnf)

---

## Descripción General del Software
El sistema consiste en una **aplicación de consola visualmente amigable**, desarrollada en **Python**, diseñada específicamente para solucionar los problemas de pérdida de inventario y olvido de préstamos de **Michael Jackson (MJ)**.

El software funciona como un ecosistema centralizado que permite:
* Registrar información básica de los adquirientes del préstamo.
* Categorizar y nomenclaturar de forma correcta los artículos a prestar (mediante identificadores únicos y lógica difusa para evaluar su estado).
* Gestionar todo el ciclo de vida de los préstamos.

La persistencia de los datos se realiza a través de **archivos planos**, lo que garantiza un almacenamiento ligero que posteriormente puede ser exportado a formatos estándar como **CSV** para un análisis estadístico detallado.

---

## Objetivos del Proyecto

### Objetivo General
Desarrollar un programa de consola interactivo y robusto en Python que gestione el inventario, préstamos, retornos y facturación de artículos, utilizando archivos planos para el almacenamiento de datos y permitiendo la exportación de resultados a CSV.

### Objetivos Específicos
* **Validación rigurosa de datos:** Implementar restricciones de longitud y tipo de caracteres para el registro de usuarios (nombres sin números, documentos puramente numéricos, correos con formato válido, etc.).
* **Control de tiempos y alertas:** Automatizar la detección de tiempos de préstamo para la generación de notificaciones de recuperación (a los 20 días) y la emisión de certificados de devolución en formato de texto plano (o PDF como bonificación).
* **Módulo de penalización y venta:** Ejecutar una lógica comercial automatizada que convierta los préstamos de más de 30 días en una venta obligatoria, calculando subtotales, totales y aplicando un *"impuesto por conchudez"* del **23%**.
* **Seguridad y Analítica de Administración:** Restringir el acceso mediante credenciales de administrador a un submenú de reportes estadísticos, permitiendo visualizar el total de préstamos, devoluciones, ventas y el comportamiento de los usuarios.

---

## Beneficios del Sistema
* **Eliminación del olvido:** Centraliza el registro de *"qué se prestó"* y *"a quién"*, evitando que MJ dependa de su memoria para recuperar sus pertenencias.
* **Mitigación de pérdidas económicas:** Al automatizar la generación de facturas de venta tras 30 días de incumplimiento, se asegura que MJ recupere el valor de adquisición de los artículos no devueltos.
* **Justicia financiera (Impuesto por Conchudez):** Desincentiva el acaparamiento de objetos prestados mediante una penalización monetaria del **23%** sobre el valor del artículo.
* **Operación ágil y organizada:** Permite una clasificación clara del inventario por categorías específicas (*Videojuegos, Libros, Herramientas*, etc.) y ofrece un módulo administrativo para auditar el flujo de caja y las devoluciones de manera inmediata.
* **Portabilidad de datos:** Al exportar a CSV y almacenar en archivos planos, los reportes se pueden abrir fácilmente en herramientas como Microsoft Excel para su posterior revisión.

---

## Requisitos Funcionales (RF)

### Módulo de Gestión de Usuarios y Artículos
* **RF-01: Registro de Usuarios con Validaciones**
  El sistema incluirá una función para registrar nuevos usuarios solicitando: *Nombre, Apellido, Documento, Correo electrónico y Tiempo de préstamo*.
  * El Nombre y el Apellido no deben contener números ni tener menos de 3 letras.
  * El Documento debe ser estrictamente numérico y tener una longitud de entre 3 y 15 dígitos.
  * El Correo electrónico debe incluir el carácter `@` y finalizar con `.com`.
  * El Tiempo de préstamo estará limitado estrictamente a las opciones de **5, 10, 15 y 30 días**.
* **RF-02: Registro y Clasificación de Ítems**
  El programa permitirá ingresar artículos al inventario registrando su *Nombre* (mínimo 3 letras, permite números), *Precio de compra* y el *Estado del ítem* mediante la aplicación de **lógica difusa** para evaluar su calidad.
* **RF-03: Codificación Única de Ítems (ID)**
  El software generará automáticamente un identificador alfanumérico único para cada artículo, vinculando su nomenclatura a la categoría seleccionada (*Videojuegos, Libros, Música y video, Herramientas, Dinero, Misceláneo y varios*).

### Módulo de Transacciones (Préstamos y Devoluciones)
* **RF-04: Control de Préstamos Activos**
  Permitirá asociar un ítem disponible (buscado por ID) a un usuario registrado. Si el usuario no existe, el programa bloqueará la transacción y solicitará su registro previo.
* **RF-05: Validación y Registro de Retornos**
  Se validará que solo se puedan registrar devoluciones asociadas a préstamos activos. Si el usuario no presenta deudas vigentes, se notificará que no es posible procesar el retorno.
* **RF-06: Generación de Certificados de Devolución**
  Si la devolución se ejecuta a tiempo, se generará un certificado en un documento de texto plano (o **PDF** como bonificación). El archivo se nombrará combinando: `nombre_del_prestador + fecha_devolucion + ID_item`.

### Módulo de Alertas, Penalizaciones y Administración
* **RF-07: Alertas de Recuperación**
  Identifica préstamos que superen los **20 días** desde su inicio para habilitar el envío de notificaciones de recuperación.
* **RF-08: Facturación de Ventas por Incumplimiento**
  Todo artículo que supere los **30 días** de préstamo se convertirá automáticamente en una venta obligatoria. Se calculará el subtotal basado en el precio de adquisición y se aplicará un **impuesto por conchudez del 23%**.
* **RF-09: Emisión de Recibos de Venta**
  Para cada venta por incumplimiento, se exportará un recibo en texto plano (o **PDF** como bonificación) detallando los motivos y el cálculo monetario. El archivo se guardará como: `nombre_usuario + ID_item`.
* **RF-10: Módulo de Autenticación de Administrador**
  Restringe el acceso al submenú de administración mediante usuario y contraseña validados contra un listado interno de seguridad.
* **RF-11: Consolidación de Reportes Estadísticos**
  El módulo administrativo incluirá reportes visuales en tiempo real de:
  * Total de préstamos registrados.
  * Total de ítems devueltos.
  * Total de ventas realizadas.
  * Total de pago realizado.
  * Lista completa de usuarios.
  * Identificación del usuario con mayor y menor cantidad de préstamos.

---

## Requisitos No Funcionales (RNF)

* **RNF-01: Interfaz de Usuario (Usabilidad)**
  Menú amigable e intuitivo basado estrictamente en **consola de comandos**, facilitando la navegación para gestionar ingresos, préstamos, retornos y facturación.
* **RNF-02: Persistencia y Almacenamiento**
  El almacenamiento de datos históricos se realizará a través de **archivos planos**, garantizando un sistema ligero sin dependencias de bases de datos externas.
* **RNF-03: Exportabilidad de Datos (Interoperabilidad)**
  Capacidad de exportar resultados y estadísticas generales a archivos con extensión **`.csv`** utilizando funciones nativas de Python.
* **RNF-04: Gestión de Versiones y Código (Estructura)**
  Código fuente organizado en un repositorio de **GitHub**. Los archivos de código irán estrictamente en la carpeta `src/` y los manuales de uso en la carpeta `doc/`.
* **RNF-05: Entorno Tecnológico y Lenguaje**
  Desarrollado en su totalidad en el lenguaje de programación **Python**, garantizando su ejecución en consola sin requerir interfaces gráficas.
