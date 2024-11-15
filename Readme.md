# Boletín 2.

Crear o formulario que permita pasar de un elemento de QStackedLayout a outro mediante:
Botóns (QPushButton).
QRadioButton.
QCheckBox.
Os elementos terán unha cor de fondo que será a que se seleccione nos botóns, RadioButton ou Checkbox.

Modificar o programa anterior para que se permita o cambio de forma exclusiva, é dicir que só se poda seleccionar un elemento cando se pulse o QRadioButton, mostrando o color de fondo seleccionado. Pola contra, cando se pulsen os controis QCheckBox, os cales poden seleccionarse algún, algúns, ningún ou todos, o programa comporarase de forma que:
O haber un seleccionado mostrará a cor especificada no check.
O haber dous, se mostrará unha cor que sexa a combinación resultante.
O non ter seleccionado ningúnha cor, mostraráse branco.
O ter tódalas cores seleccionadas mostrarase o fondo de cor negro. 

Modificar o programa do punto 1 para que cando se cambie de elemento QStackedLayout, independentemente de como fora accionado (botón, radiobutton ou checkbox) manteña cooherencia na selección. É dicir, si se pulsa o botón verde, o elemento terá a cor de fondo verde, o radiobutton marcara a cor verde e tamén o checkbox. Esta coherencia tamén se respetará si se utiliza o checkbox ou o radiobutton como elemento que desencadena a acción. Cando o usuario modifique a selección, independentemente do medio, o resto dos elementos reaccionarán para adecuarse a modificación.   


