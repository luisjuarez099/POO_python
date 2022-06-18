class Lavadora:

    def __init__(self) -> None:
        pass
    def lavar(self,temperatura='tibio'):
        self._llenar_tanque_agua=(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_agua(self,temperatura):
        print(f"Llenando tanque de agua: {temperatura}")

    def _anadir_jabon(self):
        print("Anadir jabon")

    def _lavar(self):
        print("Lavando la ropa")

    def _centrifugar(self):
        print("centrifugar la ropa")

if __name__=="__main__":
    lavadora=Lavadora()
    lavadora.lavar()

''' la abstracción se enfoca en ocultar las implementaciones internas de un proceso o método del usuario. Así, el usuario sabe lo que está haciendo, pero no sabe cómo se está haciendo el trabajo.'''