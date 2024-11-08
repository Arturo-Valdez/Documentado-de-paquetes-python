"""
Esta es el modulo que incluye la clase de 
reproductor de musica
"""

class Player:
    """
    Esta clase crea un reproductor de musica
    """

    def play(self, song):
        """
        Reproduce la cancion que recibio como parametro

        Parameter:
        song(str) : Este es un string con el Path de la cancion

        Return:
        int: Devuelve 1 en caso de exito, sino devuelve  0
        """
        print(f"Reproduciendo cancion...{song}")

    def stop(self):
        print("Stoping")