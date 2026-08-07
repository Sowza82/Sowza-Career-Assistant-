from src.rag_pipeline import ask


def run_chat():
    """
    Executa o chat no terminal.
    """

    print("\n🚀 Sowza Career Assistant")
    print("Digite 'sair' para encerrar.\n")

    while True:

        question = input("Pergunta: ")

        if question.lower().strip() == "sair":
            print("Encerrando assistente...")
            break

        if not question.strip():
            print("Digite uma pergunta válida.")
            continue

        try:
            response = ask(question)

            print("\nResposta:")
            print(response)
            print("-" * 50)

        except Exception as error:

            error_message = str(error)

            if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:
                print(
                    "\n⚠️ Limite da API Gemini atingido. "
                    "Aguarde alguns minutos ou verifique sua cota.\n"
                )

            else:
                print(
                    f"\nErro ao processar pergunta: {error}\n"
                )


def main():
    run_chat()


if __name__ == "__main__":
    main()
