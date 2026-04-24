class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.libros_prestados = []

    def solicitar_prestamo(self, libro):
        self.libros_prestados.append(libro)
        return f"{self.nombre} ha solicitado el préstamo del libro: {libro}"

class Estudiante(Usuario):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.limite_prestamos = 3
        self.carrera = carrera

    def solicitar_prestamo(self, libro):
        if len(self.libros_prestados) < self.limite_prestamos:
            return super().solicitar_prestamo(libro)
        else:
            return f"{self.nombre} ha alcanzado el límite de préstamos."
        
    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            return f"{self.nombre} ha devuelto el libro: {libro}"
        else:
            return f"{self.nombre} no tiene el libro: {libro} prestado."

class Profesor(Usuario):
    def __init__(self, nombre, edad, departamento):
        super().__init__(nombre, edad)
        self.limite_prestamos = 10
        self.departamento = departamento

    def solicitar_prestamo(self, libro):
        if len(self.libros_prestados) < self.limite_prestamos:
            return super().solicitar_prestamo(libro)
        else:
            return f"{self.nombre} ha alcanzado el límite de préstamos."
    
    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            return f"{self.nombre} ha devuelto el libro: {libro}"
        else:
            return f"{self.nombre} no tiene el libro: {libro} prestado."
        
if __name__ == "__main__":
    estudiante1 = Estudiante("Ana", 20, "Ingeniería")
    profesor1 = Profesor("Dr. Smith", 45, "Física")

    print(estudiante1.solicitar_prestamo("Cálculo"))
    print(estudiante1.solicitar_prestamo("Física"))
    print(estudiante1.solicitar_prestamo("Química"))
    print(estudiante1.solicitar_prestamo("Biología"))  # Debería alcanzar el límite

    print(profesor1.solicitar_prestamo("Física Cuántica"))
    print(profesor1.solicitar_prestamo("Relatividad"))
    
    print(estudiante1.devolver_libro("Cálculo"))
    print(estudiante1.devolver_libro("Historia"))  # No tiene este libro prestado