from nose.tools import assert_true
import requests

BASE_URL = "https://sveonline.herokuapp.com"


class NewUUID():

    def __init__(self, value):
        self.value = value


def test_request_login():
    response = requests.get('%s/login' % BASE_URL)
    assert_true(response.ok)


def test_request_logout():
    response = requests.get(
        '%s/logout' % BASE_URL)
    assert_true(response.ok)


def test_get_inicio():
    response = requests.get(
        '%s/inicio' % BASE_URL)
    assert_true(response.ok)


def test_get_me():
    response = requests.get(
        '%s/inicio/musculoEsqueletico' % BASE_URL)
    assert_true(response.ok)


def test_get_test():
    response = requests.get(
        '%s/inicio/musculoEsqueletico/testME/iniciarTestMEPiloto' % BASE_URL)
    assert_true(response.ok)


def test_get_test_enviado():
    response = requests.get(
        '%s/inicio/musculoEsqueletico/testME/enviado' % BASE_URL)
    assert_true(response.ok)


def test_get_administrar():
    response = requests.get(
        '%s/inicio/administrarSVE' % BASE_URL)
    assert_true(response.ok)


def test_get_admin_poblacion():
    response = requests.get(
        '%s/inicio/administrarSVE/poblacionSVE' % BASE_URL)
    assert_true(response.ok)


def test_get_admin_enfermedad():
    response = requests.get(
        '%s/inicio/musculoEsqueletico/enfermedadesME' % BASE_URL)
    assert_true(response.ok)


def test_get_enfermedad():
    response = requests.get(
        '%s/inicio/administrarSVE/enfermedades' % BASE_URL)
    assert_true(response.ok)


def test_get_aggDefEnf():
    response = requests.get(
        '%s/inicio/administrarSVE/aggDefEnfermedades' % BASE_URL)
    assert_true(response.ok)


def test_get_aggEnf():
    response = requests.get(
        '%s/inicio/administrarSVE/aggenfermedad' % BASE_URL)
    assert_true(response.ok)


def test_get_editEnf():
    response = requests.get(
        '%s/inicio/administrarSVE/aggenfermedad/editar/1' % BASE_URL)
    assert_true(response.ok)


def test_get_notificaciones():
    response = requests.get(
        '%s/inicio/notificaciones' % BASE_URL)
    assert_true(response.ok)


def test_get_delEnf():
    response = requests.get(
        '%s/inicio/administrarSVE/aggenfermedad/eliminar/1' % BASE_URL)
    assert_true(response.ok)


def test_get_editInfoEnf():
    response = requests.get(
        '%s/inicio/administrarSVE/aggenfermedad/informacionEnf/1' % BASE_URL)
    assert_true(response.ok)


def test_get_delInfoEnf():
    response = requests.get(
        '%s/inicio/administrarSVE/aggenfermedad/defEnfMEEliminar/1' % BASE_URL)
    assert_true(response.ok)


def test_get_aggRecomendaciones():
    response = requests.get(
        '%s/inicio/administrarSVE/aggRecomendaciones' % BASE_URL)
    assert_true(response.ok)


def test_get_listRecomendaciones():
    response = requests.get(
        '%s/inicio/administrarSVE/listaRecomendaciones' % BASE_URL)
    assert_true(response.ok)


def test_get_editRecomendaciones():
    response = requests.get(
        '%s/inicio/administrarSVE/recomendaciones/Editar/1' % BASE_URL)
    assert_true(response.ok)


def test_get_delRecomendaciones():
    response = requests.get(
        '%s/inicio/administrarSVE/recomendaciones/eliminar/1' % BASE_URL)
    assert_true(response.ok)


def test_get_listPoblacion():
    response = requests.get(
        '%s/inicio/administrarSVE/poblacionSVE/lista' % BASE_URL)
    assert_true(response.ok)


def test_get_sendMail():
    response = requests.get(
        '%s/inicio/administrarSVE/poblacionSVE/lista/correos' % BASE_URL)
    assert_true(response.ok)


def test_get_editPoblacion():
    response = requests.get(
        '%s/inicio/administrarSVE/poblacionSVE/editar/1' % BASE_URL)
    assert_true(response.ok)


def test_get_delPoblacion():
    response = requests.get(
        '%s/inicio/administrarSVE/poblacionSVE/eliminar/1' % BASE_URL)
    assert_true(response.ok)


def test_get_individual_request_404():
    response = requests.get('%s/request/an_incorrect_id' % BASE_URL)
    assert_true(response.status_code == 404)
