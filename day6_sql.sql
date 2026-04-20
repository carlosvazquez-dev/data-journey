--Día 6: práctica de SQL

-- Ver todos los datos
SELECT * FROM ventas;

--Filtrar precios mayores a 200
SELECT * FROM ventas WHERE precio > 200;

-- Ordenar precios de mayor a menor
SELECT * FROM ventas ORDER BY precio DESC;

--Unidade vendidas por producto
SELECT producto, sum(cantidad)
FROM ventas
GROUP BY producto;

-- Precio promedio por producto
SELECT producto, avg(precio)
FROM ventas
GROUP BY producto;

-- Precio promedio por ciudad
SELECT ciudad, avg(precio)
FROM ventas
GROUP BY ciudad;
