# Parte 1: Implementacion listas simples y dobles

- [x] Clase nodo simple.
- [x] Clase nodo doble.
- [x] Clase lista simple.
- [x] Clase lista doble.

# Parte 2: Implementación de Pilas y Colas usando la Lista Simple

- [x] Clase Stack
- [x] Clase Queue

# Parte 3: Implementación sistema de mensajería empleando listas, pilas y colas

- [x] Leer 'empleados.txt'
- [x] Cargar en 'empleados.txt'
- [x] Login
- [x] Admin:
  - [x] Agregar usuario
  - [x] Cambiar contrasenas
  - [x] Eliminar empleado
  - [x] Guardar cambios en el archivo (al final)
- [ ] Enviar mensaje
- [x] Recibir mensaje
- [x] Guardar cambios en el archivo
- [x] Bandeja de entrada con mensajes **NO** leidos, al consultar por consola esta debe presentar la fecha de recepción, el titulo del mensaje y el nombre de la persona que lo envió. Adicionalmente, debe permitir seleccionar cual mensaje se desea leer (tip: se recomienda implementar la bandeja de entrada como una lista doble).
- [ ] Una vez se lee un mensaje se elimina de la bandeja de entrada y pasa a la de leidos, estos se pueden consultar de forma secuencial iniciando en el mas antiguo (Se recomienda usar colas)
- Cuando un usuario quiere redactar un nuevo mensaje, por consola, se debe pedir:
  - [x] Cedula del usuario al que se envía el mensaje
  - [x] Título del mensaje
  - [x] Mensaje
  - [x] Además de la información que redacta el usuario,
  - [x] Cada mensaje de forma automática se le asigna la fecha y hora de envió.
  - [ ] El empleado tiene las opciones de guardar como borrador, descartar o enviar el mensaje.
- [ ] Al almacenar como borrador se guarda en una carpeta donde solo se puede acceder al ultimo borrador.
- [ ] Al descartar un mensaje se elimina del sistema
- [ ] Al enviar un mensaje el sistema lo agrega a la bandeja de entrada del destinatario
- [x] Los mensajes en la bandeja de entrada, mensajes leidos y borradores de cada usuario se almacenan en archivos de text, denominados por el numero de cedula del empleado, seguido por las letras BA (bandeja de entrada), ML (mensajes leidos), B (borradores)

# Test Sugeridos:

1. Loggear como admin, crear y eliminar un usuario
2. Ingresar como empleado y consultar la BA
3. Crea un nuevo mensaje desde un empleado y guardarlo como B
4. Consultar los B de un empleado
5. Enviar un mensaje desde un B
6. Crear un nuevo mensaje desde un empleado y descartarlo
7. Crear un nuevo mensaje desde un empleado y enviarlo a otro usuario
8. Consular la BA de un empleado
9. Leer un mensaje
10. Consultar ML de un empleado
11. Revisar los archivos generados por el programa
