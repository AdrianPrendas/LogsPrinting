# LogsPrinting

## Trazabilidad de transacciones con los Redo logs de Oracle

#### Se ha propuesto un proyecto de trazabilidad de transacciones para detectar anomalias en la base de datos Oracle

##### El siguiente ejemplo utiliza los archive de oracle, sin embargo  tambien se pueden observar los redolog online

###### Paso a paso

Nos conectamos como sysdba

![1](https://user-images.githubusercontent.com/20632410/48394804-8eedac80-e6da-11e8-9125-e75892503e72.PNG)

Esta es la base de datos que se utilizo para este ejemplo

![2](https://user-images.githubusercontent.com/20632410/48395186-0cfe8300-e6dc-11e8-9d22-1927ce8a9ad1.PNG)

La base de datos tiene que estar en modo archive

![3_1](https://user-images.githubusercontent.com/20632410/48395274-68307580-e6dc-11e8-9a29-f2a51bab118a.PNG)

Estos son los Redo-Log que estan en linea, se puede apreciar que existen 3 grupos y que no estan multiplexados <br>
la secuencia es 13, el estado current nos dice que en este Redo-Log se estan escribiendo las transacciones

![4](https://user-images.githubusercontent.com/20632410/48395622-6dda8b00-e6dd-11e8-9de0-6985dfc8157f.PNG)

En la siguiente imagen podemos apreciar los archives que estan en disco

![5](https://user-images.githubusercontent.com/20632410/48395662-99f60c00-e6dd-11e8-9b92-f637f34cd150.PNG)

Procedemos a hacer una transaccion

![8](https://user-images.githubusercontent.com/20632410/48395817-0d981900-e6de-11e8-913e-54897c2e1766.PNG)

Enseguida revisamos los Redo-Log <br>
provocamos un checkpoin para que LGWR, el programa responsable de escribir en los Redo-Log files, pase del Buffer a disco <br>
provacamos un switch para que todos los Redo-Log en disco pasen a ser un nuevo Archive <br>
volvemos a revisar los Redo-Los y podemos apreciar como la secuencia cambio, ahora se esta escribiendo en el siguiente Redo-Log <br>

![9](https://user-images.githubusercontent.com/20632410/48396388-d6c30280-e6df-11e8-8644-4fc2714e7cda.PNG)

Observamos que se creo un nuevo Archive, aqui es donde esta la transaccion que realizamos

![10](https://user-images.githubusercontent.com/20632410/48396559-78e2ea80-e6e0-11e8-9377-e23d7efc9a05.PNG)




