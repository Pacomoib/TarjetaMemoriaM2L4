# Importa constantes básicas (alineaciones, etc.)
from PyQt5.QtCore import Qt

# Importa todos los widgets de PyQt5
from PyQt5.QtWidgets import *

# Importa shuffle (aunque todavía no se usa)
from random import shuffle


# ---------------------------
# Inicialización de la app
# ---------------------------
app = QApplication([])

# Ventana principal
window = QWidget()
window.setWindowTitle('Tarjeta de Memoria')


# ---------------------------
# Widgets principales
# ---------------------------

# Botón para enviar la respuesta
btn_OK = QPushButton('Responder')

# Etiqueta con la pregunta
lb_Question = QLabel('¿Qué es Python?')


# ---------------------------
# Grupo de opciones (respuestas)
# ---------------------------

# Caja que contiene los radio buttons
RadioGroupBox = QGroupBox('Opciones de respuesta')

# Opciones de respuesta
rbtn_1 = QRadioButton('Lenguaje de español')
rbtn_2 = QRadioButton('Lenguaje desperunizador')
rbtn_3 = QRadioButton('Lenguaje de máquinas')
rbtn_4 = QRadioButton('Lenguaje de programación')


# ---------------------------
# Agrupación de RadioButtons
# (para que solo uno pueda seleccionarse)
# ---------------------------
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


# ---------------------------
# Layout interno de respuestas
# ---------------------------

# Dos columnas verticales para los botones
VLine_1 = QVBoxLayout()
VLine_2 = QVBoxLayout()

# Layout horizontal que contiene ambas columnas
HLine = QHBoxLayout()

# Añadir botones a la primera columna
VLine_1.addWidget(rbtn_1)
VLine_1.addWidget(rbtn_2)

# Añadir botones a la segunda columna
VLine_2.addWidget(rbtn_3)
VLine_2.addWidget(rbtn_4)

# Añadir columnas al layout horizontal
HLine.addLayout(VLine_1)
HLine.addLayout(VLine_2)

# Asignar el layout al grupo de respuestas
RadioGroupBox.setLayout(HLine)


# ---------------------------
# Layouts principales
# ---------------------------

# Layouts horizontales
HLine_Pregunta   = QHBoxLayout()  # Pregunta
HLine_Respuesta  = QHBoxLayout()  # Respuestas
HLine_Boton      = QHBoxLayout()  # Botón

# Layout vertical principal
VLine_Principal  = QVBoxLayout()


# Añadir pregunta centrada
HLine_Pregunta.addWidget(
    lb_Question,
    alignment=(Qt.AlignHCenter | Qt.AlignVCenter)
)

# Añadir grupo de respuestas
HLine_Respuesta.addWidget(RadioGroupBox)

# Centrar el botón usando espacios
HLine_Boton.addStretch(1)
HLine_Boton.addWidget(btn_OK, stretch=2)
HLine_Boton.addStretch(1)

# Añadir layouts al layout principal
VLine_Principal.addLayout(HLine_Pregunta, stretch=2)
VLine_Principal.addLayout(HLine_Respuesta, stretch=8)
VLine_Principal.addLayout(HLine_Boton, stretch=1)


# ---------------------------
# Panel de resultados
# ---------------------------

# Caja de resultados
AnsGroupBox = QGroupBox('Resultados')

# Etiquetas de resultado
lb_Result = QLabel('¿Es Correcto o no?')
Lb_Correct = QLabel('Aquí estará la respuesta')

# Layout vertical para resultados
VLine_Ans = QVBoxLayout()
VLine_Ans.addWidget(
    lb_Result,
    alignment=(Qt.AlignHCenter | Qt.AlignVCenter)
)
VLine_Ans.addWidget(
    Lb_Correct,
    alignment=Qt.AlignHCenter,
    stretch=2
)

AnsGroupBox.setLayout(VLine_Ans)

# (Actualmente no se muestra)
# HLine_Respuesta.addWidget(AnsGroupBox)
# RadioGroupBox.hide()


# ---------------------------
# Mostrar ventana
# ---------------------------

window.setLayout(VLine_Principal)
window.show()

# Ejecutar aplicación
app.exec()
