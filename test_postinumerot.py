import postinumerot


ERIKOISTAPAUKSET = {
    "43800": "KIVIJÄRVI",
    "91150": "YLI-OLHAVA",
    "65374": "SMART POST",
    "12345": "EI OLEMASSA",
    "74704": "SMARTPOST",
    "96204": "SMART-POST"
}


def test_postitoimipaikan_nimella_yksi_postinumero():
    tulos = {
        "TARTTILA": ["37770"]
    }
    assert postinumerot.haeNumerot("TARTTILA", tulos) == ["37770"]


def test_postitoimipaikan_nimella_loytyy_useampi_postinumero():
    tulos = {
        "ESPOO": ["02250", "02240"]
    }
    assert postinumerot.haeNumerot("ESPOO", tulos) == ["02250", "02240"]


def test_postinumerolla_yksi_postitoimipaikka():
    tulos = postinumerot.etsi_toimipaikka('37770')
    assert tulos == "TARTTILA"


def test_ryhmittele_yksi_toimipaikka():
    tulos = {"91740": "JAALANKA"}
    toimipaikat = postinumerot.ryhmittele_toimipaikkoihin(tulos)
    assert toimipaikat == {"JAALANKA": ["91740"]}


def test_etsi_toimipaikat_erilaisilla_kirjoitusasuilla():
    tulos = {
        "JAALANKA": ["91740"]
    }

    assert postinumerot.haeNumerot(
        "JAALANKA", tulos) == ["91740"]
    assert postinumerot.haeNumerot(
        "Jaalanka", tulos) == ["91740"]
    assert postinumerot.haeNumerot(
        "jaalanka", tulos) == ["91740"]
    assert postinumerot.haeNumerot(
        "jaaLAnka", tulos) == ["91740"]


def test_postinumerot_omalla_datalla(mocker):
    oma_data = ERIKOISTAPAUKSET
    mocker.patch('http_pyynto.hae_postinumerot', return_value=oma_data)
    tulos = postinumerot.etsi_toimipaikka('12345')

    assert tulos == 'EI OLEMASSA'


# testataan toimivaa ratkaisua smart post bugiin


def test_toimiva_ratkaisu_smartpost_smart_post_bugiin():
    tulos = {
        "SMARTPOST": ["74704"]
    }

    assert postinumerot.haeNumerot(
        "SMART POST", tulos) == ["74704"]
