# LogsPrinting

## Trazabilidad de transacciones con los Redo logs de Oracle

#### Se ha propuesto un proyecto de trazabilidad de transacciones para detectar anomalias en la base de datos Oracle

##### El siguiente ejemplo utiliza los archive de oracle, sin embargo  tambien se pueden observar los redolog online

###### Paso a paso

1. Nos conectamos como sysdba

![1](https://user-images.githubusercontent.com/20632410/48394804-8eedac80-e6da-11e8-9125-e75892503e72.PNG)

Esta es la base de datos que se utilizo para este ejemplo

![2](https://user-images.githubusercontent.com/20632410/48395186-0cfe8300-e6dc-11e8-9d22-1927ce8a9ad1.PNG)

2. La base de datos tiene que estar en modo archive

![3_1](https://user-images.githubusercontent.com/20632410/48395274-68307580-e6dc-11e8-9a29-f2a51bab118a.PNG)

3. Estos son los "Redo Log" que estan en linea, se puede apreciar que existen 3 grupos y que no estan multiplexados <br>
la secuencia es 13, el estado current nos dice que en este "Redo Log" se estan escribiendo las transacciones

![4](https://user-images.githubusercontent.com/20632410/48395622-6dda8b00-e6dd-11e8-9de0-6985dfc8157f.PNG)

En la siguiente imagen podemos apreciar los archive que estan en disco

![5](https://user-images.githubusercontent.com/20632410/48395662-99f60c00-e6dd-11e8-9b92-f637f34cd150.PNG)


