def summa(platums, garums, augstums, materiala_cena, teksts):
    darba_samaksa=15
    PVN=21
    produkta_cena=(teksts)*1.2+(platums/100*garums/100*augstums/100)/3*materiala_cena
    PVN_summa=(produkta_cena + darba_samaksa)*PVN/100
    rekinu_summa=(produkta_cena+darba_samaksa)+PVN_summa
    return rekinu_summa
