import sys

def main():
    print("=== TABUADA INTELIGENTE ===")
    print("1 - Modo Terminal")
    print("2 - Modo Interface Gráfica (PyQt5)")
    escolha = input("Escolha o modo: ")

    if escolha == "1":
        try:
            from modo_terminal.tabuada_terminal import (
                mostrar_menu,
                escolher_numero,
                tabuada_completa,
                conta_especifica,
                soma_repetida,
                dica_memorizacao,
                modo_desafio,
            )
            while True:
                mostrar_menu()
                opcao = input("Escolha uma opção: ")
                if opcao == "1":
                    num = escolher_numero()
                    tabuada_completa(num)
                elif opcao == "2":
                    num = escolher_numero()
                    conta_especifica(num)
                elif opcao == "3":
                    num = escolher_numero()
                    soma_repetida(num)
                elif opcao == "4":
                    num = escolher_numero()
                    dica_memorizacao(num)
                elif opcao == "5":
                    modo_desafio()
                elif opcao == "0":
                    print("👋 Saindo do programa. Até mais!")
                    break
                else:
                    print("⚠️ Opção inválida. Tente novamente.")
        except ImportError as e:
            print(f"❌ Erro ao carregar modo terminal: {e}")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
    elif escolha == "2":
        try:
            from modo_interface.tabuada_interface import TabuadaApp
            from PyQt5.QtWidgets import QApplication
            app = QApplication(sys.argv)
            janela = TabuadaApp()
            janela.show()
            sys.exit(app.exec_())
        except ImportError as e:
            print(f"❌ Erro ao carregar interface gráfica: {e}")
            print("💡 Certifique-se de que o PyQt5 está instalado: pip install PyQt5")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
    else:
        print("⚠️ Escolha inválida.")

if __name__ == "__main__":
    main()