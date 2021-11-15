from Tests.testCRUD import testAdaugaRezervare, testStergereRezervare, testModificaRezervarea, testGetById
from Tests.testDomeniu import testRezervare
from Tests.testFunctionalitati import testTrecereaRezervarilorLaClasaSuperioara, \
    testIeftinireaRezervarilorCuCheckinCuUnProcentaj, testPretulMaximPentruFiecareClasa, \
    testOrdonareDescrescatorDupaPret, testSumePreturiPerNume


def runAllTests():
    testRezervare()
    testAdaugaRezervare()
    testStergereRezervare()
    testModificaRezervarea()
    testTrecereaRezervarilorLaClasaSuperioara()
    testIeftinireaRezervarilorCuCheckinCuUnProcentaj()
    testPretulMaximPentruFiecareClasa()
    testGetById()
    testOrdonareDescrescatorDupaPret()
    testSumePreturiPerNume()