class Instructor:
    def __init__(self):
        self.numero_empleado = 0
        self.nombre = ""
        self.fecha_nacimiento = ""
        self.numero_certificacion = ""

    def registrarInstructor(self):
        print("----------- Registrar instructor -----------")
        self.numero_empleado = input("Capture el numero de empleado: ")
        self.nombre = input("Capture el nombre del empleado: ")
        self.fecha_nacimiento = input("Capture la fecha de nacimiento: ")
        self.numero_certificacion = input("Capture el numero de certificacion: ")

class Curso:
    def __init__(self):
        self.fecha_inicio = ""
        self.fecha_fin = ""
        self.nombre_curso = ""
        self.instructor = None

    def registrarCurso(self):
        print("----------- Registro curso ----------")
        self.fecha_inicio = input("Capture la fecha de inicio: ")
        self.fecha_fin = input("Capture la fecha de fin: ")
        self.nombre_curso = input("Capture el nombre del curso: ")

    def imprimirInformacion(self):
        print("Curso: ",self.nombre_curso)
        print("Fecha de inicio: ", self.fecha_inicio)
        print("Fecha de fin: ", self.fecha_fin)
        print("Numero de empleado: ",self.instructor.numero_empleado)
        print("Nombre del instructor: ",self.instructor.nombre)

    def agregarInstructor(self, InstructorPorAsignar):
        self.instructor = InstructorPorAsignar

o_instructor = Instructor()
o_instructor.registrarInstructor()

objeto = Curso()
objeto.registrarCurso()
objeto.agregarInstructor(o_instructor)

print("---------- Informacion del curso ----------")
objeto.imprimirInformacion()

input()