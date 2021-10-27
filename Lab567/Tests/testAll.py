from Tests.testCRUD import testAdaugaRezervare, testStergereRezervare, testModificaRezervarea
from Tests.testDomeniu import testRezervare
from Tests.testFunctionalitati import testTrecereaRezervarilorLaClasaSuperioara


def runAllTests():
    testRezervare()
    testAdaugaRezervare()
    testStergereRezervare()
    testModificaRezervarea()
    testTrecereaRezervarilorLaClasaSuperioara()