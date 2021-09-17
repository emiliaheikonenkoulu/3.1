import http_pyynto


def etsi_toimipaikka(postinumero):
    postinumerot = http_pyynto.hae_postinumerot()

    if postinumero in postinumerot:
        return postinumerot[postinumero]
    else:
        return 'Tuntematon'

# jäsennetään postinumeroaineisto uudenlaiseksi tietorakenteeksi


def ryhmittele_toimipaikkoihin(postinumerot):
    toimipaikat = {}
    for numero, paikka in postinumerot.items():
        if paikka in toimipaikat:
            toimipaikat[paikka].append(numero)
        else:
            toimipaikat[paikka] = [numero]

    return toimipaikat

# haetaan kaikki postitoimipaikan postinumerot sekä ei huomioida syöttäjän syöttämää kirjainkokoa, smart post == smartpost


def haeNumerot(nimi, toimipaikat):
    isolla = nimi.strip().upper().replace("SMART POST", "SMARTPOST")
    if isolla in toimipaikat:
        return toimipaikat[isolla]
    else:
        return []


def main():
    postinumerot = http_pyynto.hae_postinumerot()

    toimipaikat = ryhmittele_toimipaikkoihin(postinumerot)

    etsittava = input('Kirjoita postitoimipaikka: ')

    numerot = haeNumerot(etsittava, toimipaikat)

    print('Postinumerot: ' + ', '.join(numerot))


if __name__ == '__main__':
    main()
