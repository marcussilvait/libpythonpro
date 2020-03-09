import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['', 'vnc_vinicius92']
)
def test_remetente(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        resultado = enviador.enviar(
            remetente,
            'vnctm10@gmail.com',
            'Cursos Python Pro',
            'Terceira turma Python Pro Bruno Rocha'
        )
        assert 'vnctm10@gmail.com' in resultado


@pytest.mark.parametrize(
    'destinatario',
    ['vnc_vinicius92@hotmail.com', 'foo@bar.com.br']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'vnctm10@gmail.com',
        'Cursos Python Pro',
        'Terceira turma Python Pro Bruno Rocha'
    )
    assert destinatario in resultado
