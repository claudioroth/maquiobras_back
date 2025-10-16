## Cambios al 1/10/2025

SUC1=GALICIA
SUC2=JUAN B JUSTO
SUC3=DEPOSITO



ABM USUARIOS - HABILITADO PARA: ADMINISTRADOR (FULL ACCESO) Y SEMI ADMINISTRADOR (SOLO PUEDE VER)  
- Ahora se puede asignar sucursal a cualquier de los 3 roles.
- Los headers de la tabla ahora están fijos, podes hacer scroll verticalmente y siempre vas a ver los headers.
- Si el usuario logueado es administrador no va a poder desactivar su propio usuario.
- Si el usuario logueado es administrador y se para sobre el botón de desactivar su usuario le va a salir un popup indicando que no puede desactivar el usuario de el mismo.
- Si el usuario logueado quiere modificar su rol, se le va abrir un popup indicando que si continua automáticamente se va a desloguear.
- Se agrego un store para manejar mejor los roles del usuario.

VENTAS
- El admin y el semi admin ahora pueden hacer ventas desde la sucursal que tengan asignada.
- Se modifico el carrito, ahora se puede escribir a mano la cantidad que se requiera del producto seleccionado y se va a descontar del stock
- En la ventana de Nueva venta ahora aparece el nombre de la sucursal desde la que estas vendiendo (la que tenga asignada el usuario en este momento)
- Se ordeno la tabla de ventas, ahora aparece siempre arriba la ultima venta.
- El usuario y el semi admin, ven solo las ventas de su sucursal, el admin ve las ventas de todas las sucursales.

ABM PROVEEDORES HABILITADO PARA: ADMINISTRADOR (FULL ACCESO), SEMI ADMINISTRADOR y USUARIO (SOLO PUEDEN VER)  
- Se Creo la tabla de proveedores con buscador
- Se Agrego la opción de crear proveedores
- Se Agrego la opción de modificar proveedores
- Se agrego una función para que no te deje usar un N de proveedor que ya esta en uso+

INGRESOS - HABILITADO PARA: ADMINISTRADOR (FULL ACCESO) Y SEMI ADMINISTRADOR (SOLO PUEDE VER)  
- Se modifico la tabla principal, ahora se muestra la columna productos en la que podes ver el listado de ingresos que hubo (presionar botón productos).
- Se modifico el orden de la tabla principal, ahora se ven siempre los últimos ingresos primero.
- Los encabezados de la tabla permanecen fijos al hacer scroll vertical.
- Se modifico el formulario de Ingresos, se agrego una lista de productos (con filtro) y un sistema de carrito.
- Ahora se puede generar un ingreso con varios productos arraigados a un mismo remito.
- En el carrito se pueden manipular las cantidades de los productos escribiendo el valor numerico.
- Se agregaron varias validaciones al formulario y se hicieron algunos ajustes estéticos.

ABM PRODUCTOS
- Se reacomodaron las columnas de la tabla principal
- Ahora solamente puede haber un IVA, en la tabla principal se muestra %21 o %10,5
- En el formulario de Nuevo Producto, se modifico el selector de proveedores, ahora los datos llegan directo desde la base datos.
- En el formulario de Nuevo Producto, se agrego un selector de IVA (%21 y %10.5)
- El campo de Importe sin IVA ahora es obligatorio y se calcula el Iva de acuerdo a lo que se elija en el selector.
- El campo Oferta sin IVA ahora se calculo multiplicando los campos Oferta Costo x Rentabilidad.
