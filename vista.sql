CREATE VIEW VistaDetallesEmpleados AS
SELECT 
    E.nombre_empleado, 
    E.salario, 
    P.nombre_puesto, 
    D.nombre_departamento
FROM 
    empleados E
INNER JOIN 
    puestos P ON E.puesto_id = P.puesto_id
INNER JOIN 
    departamentos D ON P.departamento_id = D.departamento_id;


SELECT * FROM VistaDetallesEmpleados;
