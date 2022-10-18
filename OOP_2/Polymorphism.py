"""
Polimorfism - poli - mai multe; morfi - forme
Care poate lua mai multe forme
Mai multe functii cu acelasi nume, dar comportament sau parametri diferiti

"""

class Romania:

    def language(self):
        return "ro"

class Franta:

    def language(self):
        return "fr"

inst_ro = Romania()
inst_fr = Franta()

inst_ro.language()
inst_fr.language()