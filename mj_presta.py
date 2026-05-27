"""
Sistema MJ PRESTA - Gestor de Préstamos
Aplicación de consola para administrar el registro de usuarios, 
préstamos, devoluciones y consultas.
"""

import os
import sys


class MJPresta:
    """Clase principal del sistema MJ PRESTA"""
    
    def __init__(self):
        """Inicializa el sistema"""
        self.ejecutando = True
    
    def limpiar_pantalla(self):
        """Limpia la pantalla de la consola"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_encabezado(self):
        """Muestra el encabezado ASCII art del sistema"""
        encabezado = """
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

    ███╗   ███╗     ██╗     ██████╗ ██████╗ ███████╗███████╗████████╗ █████╗ 
    ████╗ ████║     ██║     ██╔══██╗██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗
    ██╔████╔██║     ██║     ██████╔╝██████╔╝█████╗  ███████╗   ██║   ███████║
    ██║╚██╔╝██║     ██║     ██╔═══╝ ██╔══██╗██╔══╝  ╚════██║   ██║   ██╔══██║
    ██║ ╚═╝ ██║     ███████╗██║     ██║  ██║███████╗███████║   ██║   ██║  ██║
    ╚═╝     ╚═╝     ╚══════╝╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝

╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

                    ¡Bienvenido a MJ Presta!

╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
        """
        print(encabezado)
    
    def mostrar_menu(self):
        """Muestra el menú principal de opciones"""
        menu = """
    ┌──────────────────────────────────────┐
    │          MENÚ PRINCIPAL              │
    ├──────────────────────────────────────┤
    │  1. Registrar Usuario                │
    │  2. Registrar Préstamo               │
    │  3. Registrar Devolución             │
    │  4. Consultar Ítems con más de 30 d. │
    │  5. Consultar Artículos Prestados    │
    │  6. Administrador                    │
    │  7. Salir                            │
    └──────────────────────────────────────┘
        """
        print(menu)
    
    def obtener_opcion_usuario(self):
        """
        Obtiene la opción del usuario con validación
        
        Returns:
            int: Opción válida seleccionada por el usuario (1-7)
            None: Si la entrada no es válida
        """
        try:
            opcion = input("    Ingrese su opción (1-7): ").strip()
            
            if not opcion:
                self.mostrar_error("Por favor, ingrese una opción válida.")
                return None
            
            opcion_int = int(opcion)
            
            if opcion_int < 1 or opcion_int > 7:
                self.mostrar_error(f"La opción '{opcion_int}' está fuera del rango permitido (1-7).")
                return None
            
            return opcion_int
        
        except ValueError:
            self.mostrar_error(f"'{opcion}' no es un número válido. Ingrese un número del 1 al 7.")
            return None
    
    def mostrar_error(self, mensaje):
        """Muestra un mensaje de error en pantalla"""
        print(f"\n    ❌ ERROR: {mensaje}\n")
    
    def mostrar_mensaje(self, mensaje):
        """Muestra un mensaje informativo"""
        print(f"\n    ℹ️  {mensaje}\n")
    
    def pausar(self):
        """Pausa la ejecución hasta que el usuario presione una tecla"""
        input("    Presione ENTER para regresar al menú principal...")
    
    # ==================== FUNCIONES DE MENÚ ====================
    
    def registrar_usuario(self):
        """Opción 1: Registrar Usuario"""
        self.limpiar_pantalla()
        print("╌" * 50)
        print("                   REGISTRAR USUARIO")
        print("╌" * 50)
        self.mostrar_mensaje("Ha seleccionado la opción 1: Registrar Usuario")
        # Función vacía para programar lógica posterior
        self.pausar()
    
    def registrar_prestamo(self):
        """Opción 2: Registrar Préstamo"""
        self.limpiar_pantalla()
        print("╌" * 50)
        print("                   REGISTRAR PRÉSTAMO")
        print("╌" * 50)
        self.mostrar_mensaje("Ha seleccionado la opción 2: Registrar Préstamo")
        # Función vacía para programar lógica posterior
        self.pausar()
    
    def registrar_devolucion(self):
        """Opción 3: Registrar Devolución"""
        self.limpiar_pantalla()
        print("╌" * 50)
        print("                   REGISTRAR DEVOLUCIÓN")
        print("╌" * 50)
        self.mostrar_mensaje("Ha seleccionado la opción 3: Registrar Devolución")
        # Función vacía para programar lógica posterior
        self.pausar()
    
    def consultar_items_vencidos(self):
        """Opción 4: Consultar Ítems con más de 30 días"""
        self.limpiar_pantalla()
        print("╌" * 50)
        print("            CONSULTAR ÍTEMS CON MÁS DE 30 DÍAS")
        print("╌" * 50)
        self.mostrar_mensaje("Ha seleccionado la opción 4: Consultar Ítems con más de 30 días")
        # Función vacía para programar lógica posterior
        self.pausar()
    
    def consultar_articulos_prestados(self):
        """Opción 5: Consultar Artículos Prestados"""
        self.limpiar_pantalla()
        print("╌" * 50)
        print("              CONSULTAR ARTÍCULOS PRESTADOS")
        print("╌" * 50)
        self.mostrar_mensaje("Ha seleccionado la opción 5: Consultar Artículos Prestados")
        # Función vacía para programar lógica posterior
        self.pausar()
    
    def administrador(self):
        """Opción 6: Administrador"""
        self.limpiar_pantalla()
        print("╌" * 50)
        print("                   ADMINISTRADOR")
        print("╌" * 50)
        self.mostrar_mensaje("Ha seleccionado la opción 6: Administrador")
        # Función vacía para programar lógica posterior
        self.pausar()
    
    def salir(self):
        """Opción 7: Salir del programa"""
        self.limpiar_pantalla()
        print("╌" * 50)
        print("                   SALIENDO...")
        print("╌" * 50)
        despedida = """
    ╔════════════════════════════════════════╗
    ║  ¡Gracias por usar MJ Presta!          ║
    ║  Hasta luego...                        ║
    ╚════════════════════════════════════════╝
        """
        print(despedida)
        self.ejecutando = False
    
    def procesar_opcion(self, opcion):
        """
        Procesa la opción seleccionada por el usuario
        
        Args:
            opcion (int): Número de opción (1-7)
        """
        opciones_acciones = {
            1: self.registrar_usuario,
            2: self.registrar_prestamo,
            3: self.registrar_devolucion,
            4: self.consultar_items_vencidos,
            5: self.consultar_articulos_prestados,
            6: self.administrador,
            7: self.salir
        }
        
        accion = opciones_acciones.get(opcion)
        if accion:
            accion()
    
    def ejecutar(self):
        """Ejecuta el bucle principal del programa"""
        while self.ejecutando:
            self.limpiar_pantalla()
            self.mostrar_encabezado()
            self.mostrar_menu()
            
            opcion = self.obtener_opcion_usuario()
            
            if opcion is not None:
                self.procesar_opcion(opcion)
            else:
                # Si la opción no es válida, espera a que presione una tecla
                input("\n    Presione ENTER para intentar de nuevo...")


def main():
    """Función principal que inicia la aplicación"""
    sistema = MJPresta()
    sistema.ejecutar()


if __name__ == "__main__":
    main()
