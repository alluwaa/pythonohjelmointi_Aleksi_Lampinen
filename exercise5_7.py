tuotetunnisteet = [
    "PHILIPS_Vedenkeitin_HD4646_2020_09_21_C_1",
    "KENWOOD_Yleiskone_KVL8300S_2015_09_22_C_3",
    "BOSCH_Tehosekoitin_MMB65G5M_2016_05_07_C_3",
    "WHIRLPOOL_Mikroaaltouuni_MCP345WH_2019_01_15_C_1",
    "ROSENLEW_Pakastin_RPP2330_2017_01_29_C_2",
    "ELECTROLUX_Jääkaappi_ERF4114AOW_2017_11_07_C_2"
]

kategoriat = ["Muut", "Pienlaitteet", "Kylmälaitteet", "Sekoittimet"]

for tunniste in tuotetunnisteet:
    osat = tunniste.split("_")
    valmistaja = osat[0]
    nimi = osat[1].replace(" ", "")
    malli = osat[2]
    vuosi = osat[3]
    kuukausi = osat[4]
    paiva = osat[5]
    kategoria_numero = int(osat[7])

    print("Valmistaja:", valmistaja)
    print("Nimi ja malli:", nimi + " (" + malli + ")")
    print("Kategoria:", kategoriat[kategoria_numero])
    print("Lisäyspäivämäärä:", paiva + "." + kuukausi + "." + vuosi)
    print("") 