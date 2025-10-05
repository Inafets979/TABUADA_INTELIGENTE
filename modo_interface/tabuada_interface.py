from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QTextEdit, QMessageBox, QComboBox, QInputDialog
)
import random

class TabuadaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tabuada Inteligente")
        self.setFixedSize(500, 500)
        self.erros = {}
        self.init_ui()

    def init_ui(self):
        titulo = QLabel("🧮 Tabuada Inteligente")
        titulo.setStyleSheet("font-size: 20px; font-weight: bold;")

        self.combo_numero = QComboBox()
        self.combo_numero.addItems([str(i) for i in range(1, 11)])

        self.combo_multiplicador = QComboBox()
        self.combo_multiplicador.addItems([str(i) for i in range(1, 11)])

        btn_completa = QPushButton("Ver tabuada completa")
        btn_especifica = QPushButton("Ver conta específica")
        btn_somas = QPushButton("Ver como soma repetida")
        btn_dica = QPushButton("Ver dica de memorização")
        btn_quiz = QPushButton("Modo desafio")
        btn_sair = QPushButton("🚪 Sair")

        btn_completa.clicked.connect(self.mostrar_tabuada_completa)
        btn_especifica.clicked.connect(self.mostrar_conta_especifica)
        btn_somas.clicked.connect(self.mostrar_soma_repetida)
        btn_dica.clicked.connect(self.mostrar_dica)
        btn_quiz.clicked.connect(self.modo_desafio)
        btn_sair.clicked.connect(self.fechar_aplicacao)

        self.resultado = QTextEdit()
        self.resultado.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(titulo)

        h1 = QHBoxLayout()
        h1.addWidget(QLabel("Número:"))
        h1.addWidget(self.combo_numero)
        layout.addLayout(h1)

        h2 = QHBoxLayout()
        h2.addWidget(QLabel("Multiplicador:"))
        h2.addWidget(self.combo_multiplicador)
        layout.addLayout(h2)

        layout.addWidget(btn_completa)
        layout.addWidget(btn_especifica)
        layout.addWidget(btn_somas)
        layout.addWidget(btn_dica)
        layout.addWidget(btn_quiz)
        layout.addWidget(btn_sair)
        layout.addWidget(self.resultado)

        self.setLayout(layout)

    def mostrar_tabuada_completa(self):
        numero = int(self.combo_numero.currentText())
        texto = f"📘 Tabuada do {numero}:\n"
        for i in range(1, 11):
            texto += f"{numero} x {i} = {numero * i}\n"
        self.resultado.setText(texto)

    def mostrar_conta_especifica(self):
        numero = int(self.combo_numero.currentText())
        multiplicador = int(self.combo_multiplicador.currentText())
        resultado = numero * multiplicador
        texto = f"🔍 Resultado:\n{numero} x {multiplicador} = {resultado}"
        self.resultado.setText(texto)

    def mostrar_soma_repetida(self):
        numero = int(self.combo_numero.currentText())
        multiplicador = int(self.combo_multiplicador.currentText())
        soma = " + ".join([str(numero)] * multiplicador)
        resultado = numero * multiplicador
        texto = f"🧠 Soma repetida:\n{numero} x {multiplicador} = {soma} = {resultado}"
        self.resultado.setText(texto)

    def mostrar_dica(self):
        numero = int(self.combo_numero.currentText())
        dicas = {
            1: "🎯 Tabuada do 1: Qualquer número × 1 = o próprio número!\n💡 Dica: É como não fazer nada, o número fica igual.",
            2: "🎯 Tabuada do 2: É dobrar o número!\n💡 Dica: 2×3 = 3+3 = 6. Sempre some o número com ele mesmo.\n🔢 Padrão: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20",
            3: "🎯 Tabuada do 3: Use os dedos para contar!\n💡 Dica: 3×4 = conte 3, 6, 9, 12 (pule de 3 em 3).\n🔢 Padrão: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30",
            4: "🎯 Tabuada do 4: É dobrar duas vezes!\n💡 Dica: 4×3 = (2×3) + (2×3) = 6 + 6 = 12\n🔢 Padrão: 4, 8, 12, 16, 20, 24, 28, 32, 36, 40",
            5: "🎯 Tabuada do 5: Termina sempre em 0 ou 5!\n💡 Dica: 5×4 = 20, 5×7 = 35. Conte de 5 em 5!\n🔢 Padrão: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50",
            6: "🎯 Tabuada do 6: Use a tabuada do 3 e dobre!\n💡 Dica: 6×4 = (3×4) × 2 = 12 × 2 = 24\n🔢 Padrão: 6, 12, 18, 24, 30, 36, 42, 48, 54, 60",
            7: "🎯 Tabuada do 7: A mais difícil, mas tem truques!\n💡 Dica: 7×2 = 14, 7×3 = 21. Use os dedos para contar!\n🔢 Padrão: 7, 14, 21, 28, 35, 42, 49, 56, 63, 70",
            8: "🎯 Tabuada do 8: É dobrar 3 vezes!\n💡 Dica: 8×3 = (4×3) × 2 = 12 × 2 = 24\n🔢 Padrão: 8, 16, 24, 32, 40, 48, 56, 64, 72, 80",
            9: "🎯 Tabuada do 9: Truque dos dedos!\n💡 Dica: 9×3 = 27. A soma dos dígitos (2+7) = 9!\n🔢 Padrão: 9, 18, 27, 36, 45, 54, 63, 72, 81, 90",
            10: "🎯 Tabuada do 10: Só adicionar um zero!\n💡 Dica: 10×4 = 40. É o número original + 0 no final!\n🔢 Padrão: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100"
        }
        texto = dicas.get(numero, "Essa tabuada não tem uma dica especial.")
        self.resultado.setText(f"💡 Dicas para o {numero}:\n{texto}")

    def modo_desafio(self):
        numero = random.randint(1, 10)
        multiplicador = random.randint(1, 10)
        resposta, ok = QInputDialog.getText(self, "Desafio", f"Quanto é {numero} x {multiplicador}?")
        if ok:
            try:
                resposta_int = int(resposta)
                correto = numero * multiplicador
                if resposta_int == correto:
                    QMessageBox.information(self, "✅ Acertou!", f"Parabéns! {numero} x {multiplicador} = {correto}")
                else:
                    QMessageBox.warning(self, "❌ Errou", f"Resposta correta: {numero} x {multiplicador} = {correto}")
                    self.erros[(numero, multiplicador)] = self.erros.get((numero, multiplicador), 0) + 1
                    self.sugerir_treino()
            except ValueError:
                QMessageBox.warning(self, "Erro", "Digite um número válido.")

    def sugerir_treino(self):
        if self.erros:
            mais_errado = max(self.erros, key=self.erros.get)
            numero, multiplicador = mais_errado
            self.resultado.setText(f"📌 Sugestão de treino:\nVocê errou bastante {numero} x {multiplicador}. Que tal praticar essa conta?")
    
    def fechar_aplicacao(self):
        """Fecha a aplicação com confirmação"""
        from PyQt5.QtWidgets import QMessageBox
        resposta = QMessageBox.question(
            self, 
            "Sair", 
            "Tem certeza que deseja sair da aplicação?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if resposta == QMessageBox.Yes:
            self.close()