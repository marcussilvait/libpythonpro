import pytest

from libpythonpro.spam.enviador_de_email import Enviador
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
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'vnc_vinicius92@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Marcus', email='vnc_vinicius92@hotmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'vnctm10@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert enviador.parametros_de_envio == (
        'vnctm10@hotmail.com',
        'vnc_vinicius92@hotmail.com'
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
