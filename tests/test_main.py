from unittest.mock import patch

from main import run_chat



def test_run_chat_response():

    with patch(
        "main.ask",
        return_value="Tatiane Souza é desenvolvedora Front-End."
    ) as mock_ask:

        with patch(
            "builtins.input",
            side_effect=[
                "Quem é Tatiane Souza?",
                "sair"
            ]
        ):

            run_chat()


    mock_ask.assert_called_once_with(
        "Quem é Tatiane Souza?"
    )



def test_run_chat_empty_question():

    with patch(
        "main.ask"
    ) as mock_ask:

        with patch(
            "builtins.input",
            side_effect=[
                "",
                "sair"
            ]
        ):

            run_chat()


    mock_ask.assert_not_called()



def test_run_chat_exit():

    with patch(
        "builtins.input",
        side_effect=[
            "sair"
        ]
    ):

        run_chat()
