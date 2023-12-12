import os 
runProgram = True
todoList = []

#  Función para mostrar las opciones del menú
def showMenuOptions():
    print(" ")
    print(" ")
    print("Por favor seleccione una opción")
    print(" ")
    print(" ")
    print("1. Crear una tarea")
    print("2. Marcar como realizada una tarea")
    print("3. Borrar una terea")
    print("4. Salir")

# Función para mostrar todas las tareas
def showTodoList():
    global todoList
    print(" ")
    print(" ")
    print("******************************")
    for todo in todoList:
        print(f"{todoList.index(todo) + 1}. {todo}")
    print("******************************")
    print(" ")
    print(" ") 
    
# Función para guardar tareas en la variable todoList
def createTodo():
    os.system("cls")
    global todoList
    print(" Crear una nueva tarea")
    todo = input("Por favor ingrese el nombre de la tare: ")
    todoList.append(todo)
    # Mostrar la lista de tareas
    showTodoList()

# Fución para marcar una tarea como realizada
def updateTodo():
    global todoList
    print(" Actualizar una tarea")
    todoId = int(input("Ingrese el número de la tarea para marcar como lista: "))
    todoList[todoId - 1] = todoList[todoId - 1] + "✅"
    showTodoList()
    
# Función que nos permite borrar una tarea
def deleteTodo():
    global todoList
    print("Borrar una tarea")
    todoId = int(input("Ingrese el número de la tarea que quiere borrar: "))
    del todoList[todoId - 1]
    showTodoList()
    
def main():
    global runProgram
    print(".: WELCOME TO A PYTHON TO DO LIST:.")
    flag = True
    
    while runProgram:
        while flag:
            showMenuOptions() # Aqui invocamos la función para mostrar las opciones del menú
            option = int(input("Ingresa una opción: "))
        
            match option:
                case 1:
                    createTodo()
                    
                case 2:
                    updateTodo()
                    
                case 3: 
                    deleteTodo()
                
                case 4:
                    print("Saliendo...")
                    runProgram = False
                    flag = False
    
                case _:
                    print("Opción no válida")
        
if __name__ == "__main__":
    main()