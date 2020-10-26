# Mini-project
Hangman game

Este es un documento explicando cómo se ha programado el juego "Hangman":

Partimos de la creación de una lista que contiene series de Netflix.
Necesitamos importar la libreria "random" y utilizar la funcion random.choice para que computer elija un elemento aleatorio (una serie en este caso) de esa lista que será la que el jugador tendrá que adivinar.

El numero maximo de fallos permitido será igual a 7. Partiremos con el contador a 0 en la variable fails_count. El juego terminará si el usuario comete 7 fallos antes de averiguar la serie.

Creamos la funcion greetings para que muestre un saludo al iniciarse el juego. 

Se inicia el juego:

La serie que ha escogido la formula random.choice se muestra toda ella con underscores "_ _ _ _ _"
Para ello hemos definimos la funcion generate_word_hits con strings como argumento. Creamos una lista vacia "hits" e iteramos sobre el string de la serie en cuestión. Mediante boleanos, buscamos que la condicion " " (espacio) se cumpla para pasar como True los espacios, e inicialmente pasamos como False todas las letras de ese string. Asi llenaremos esa lista previamente vacia con boleanos True or False y será de la misma longitud que el string serie. A medida que el jugador adivine letras, esos boleanos pasaran a ser True y se descubrirá esa letra en la posicion que le pertenece. Esto ultimo lo explicaremos un poco mas adelante.

El siguiente paso es crear la función print_gaps que muestra la serie con underscores pero se actualizará si hay algun acierto. Esta funcion recibe los valores "serie" y "hits" como argumentos. Creamos un string vacío que se irá rellenando de la siguiente manera:
    Iteramos sobre el rango de la longitud de esa serie.
    Si el valor X de la "serie" en esa iteracion no es " " (espacio) y el valor boleano que le corresponde de la lista "hits" es False, significa que todavia no se ha averiguado la letra, por lo que pasará a ese string vacio el valor "_". La 2a condicion de ese condicional es puramente estetico, convertirá los espacios " " como 3 espacios "   " . El resto de casos, cuando el boleano es True, añadira el valor que corresponda de la serie a ese string vacio y en la posicion que le corresponda, ya que estamos iterando sobre el rango de la longitud de esa "serie".  

Acto seguido creamos la funcion ask_character pidiendo un input al jugador. El jugador tendrá que devolver una letra, que deberá estar contenida en la variable "alphabet". Si no está contenida no avanzaremos a la siguiente pantalla y el juego nos volverá a pedir una letra hasta que lo hagamos correctamente.
La siguiente funcion que aparecerá en el juego sera la función user_succeed con los parametros serie, hits y character.
Partimos de la base de que no ha acertado ninguna letra, e iteramos sobre la longitud de la serie. Si el valor del indice de la serie es igual a la letra que nos ha pasado el jugador, el valor boleano en la posicion de hits pasará a ser True y actualizaremos la palabra "hits" en la posicion que ha acertado, y ademas se marca internamente para saber si en esta jugada concreta ha acertado o no. Dependiendo de si ha sido un acierto o un error, mostraremos el nuevo estado de hits -con las letras acertadas- o mostraremos el hangman con un nuevo error.

El juego repetirá las funciones print gaps, ask_character y user succeed hasta que o bien el jugador acierte la palabra o se alcance el número de errores 7.

Al final del juego, revelará la pelicula que queríamos adivinar.
