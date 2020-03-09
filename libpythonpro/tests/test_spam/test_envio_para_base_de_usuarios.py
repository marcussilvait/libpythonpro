from unittest.mock import Mock

import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Marcus', email='vnc_vinicius92@hotmail.com'),
            Usuario(nome='Luciano', email='vnc_vinicius92@hotmail.com')
        ],
        [
            Usuario(nome='Marcus', email='vnc_vinicius92@hotmail.com'),
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'vnc_vinicius92@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Marcus', email='vnc_vinicius92@hotmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'vnctm10@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.assert_called_once_with == (
        'vnctm10@hotmail.com',
        'vnc_vinicius92@hotmail.com'
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
