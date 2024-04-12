## Creación de una Aplicación Web a partir de un Fichero JSON

Vamos a crear una aplicación web a partir de un fichero JSON (puedes utilizar el mismo que empleaste en tu proyecto) con las siguientes características:

- La aplicación debe tener una hoja de estilo. Para ello, lo mejor es que busques una plantilla HTML/CSS.
- Las plantillas que uses en la aplicación se heredarán de la plantilla `base.html` (esta plantilla la puedes crear a partir de la plantilla HTML que has buscado).
- La plantilla base tendrá al menos dos bloques: uno para indicar el título y otro para poner el contenido.
- La página principal tendrá una imagen con el logotipo; al pulsar sobre esta imagen nos llevará a una página `/xxxs`.
- La página `/xxxs` nos mostrará un buscador. Para ello, pon un formulario con un cuadro de texto donde puedas poner el nombre de un xxx que quieres buscar. Cuando pulses el botón de buscar, enviará la información a la página `/listaxxxs`. El formulario enviará los datos con el método POST.
- En la página `/listaxxxs` (que solo se puede acceder por el método POST) aparecerán los xxxs cuyo nombre empiece por la cadena que hemos añadido al formulario. Si no hemos indicado ninguna cadena, mostrará todos los xxxs.
- La página `/listaxxxs` mostrará una tabla generada dinámicamente a partir de los datos de vuestro fichero JSON y la búsqueda que se haya realizado.
- La tabla tendrá al menos tres columnas: en la primera aparecerá el nombre, en la segunda otra información relevante y en la tercera habrá un enlace con la palabra “Detalle” que nos llevará a la página del xxx con la ruta `/xxx/<identificador>` o `/xxx?id=xxxxxxxxxx`.
- Estamos utilizando el patrón de diseño: Lista - detalle. La lista está en la página `/listaxxx` y el detalle está en la página `/xxx/<identificador>` o `/xxx?id=xxxxxxx`, donde aparecerán todos los datos del xxx que tenga ese identificador. Si el identificador no existe, devolverá un 404. Tendrá un enlace que nos devuelve a la página `/xxxs`.
- Debes buscar una Plataforma como Servicio (PaaS) basada en la nube que sea gratuita (Railway, Dokku, etc.) y desplegar vuestra aplicación en ella. Debes indicar el proceso de despliegue.

### Mejoras Propuestas:

1. Realizar la búsqueda utilizando una sola ruta: Es decir, que en la página `/xxxs` esté el formulario de búsqueda y la lista de xxxs seleccionados. La información del formulario se enviará a la misma página. No existirá la página `/listaxxxs`.
2. Modificar el programa para que aparezca en el formulario la cadena que habías introducido en la búsqueda.
3. Añadir otro criterio de búsqueda. Para buscar por ese segundo criterio, generarás dinámicamente una lista desplegable (elemento select) en el formulario con los valores de los xxx.
4. Programar la lista desplegable para que recuerde la opción elegida en la búsqueda.

### Entrega:

1. La URL del repositorio GitHub donde has desarrollado el programa. Recuerda que debes hacer el programa poco a poco y que los cambios los tienes que ir guardando con distintos commits.
2. La URL de la aplicación funcionando en la plataforma PaaS seleccionada.
3. Capturas de pantalla de las páginas de la aplicación desplegada en la plataforma como servicio elegida donde se vean todos los elementos que se han solicitado.
4. Indica qué mejoras has desarrollado.
