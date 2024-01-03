Feature: To-Do List Manager


  @addtasktolist
  Scenario: Agregar una tarea con descripción a la lista
  Given la lista de tareas está vacía
  When el usuario agrega una tarea "Comprar víveres" con la descripción "Ir al supermercado y comprar lo necesario para la semana"
  Then la lista de tareas debería contener la tarea "Comprar víveres" con la descripción "Ir al supermercado y comprar lo necesario para la semana"

  @importatdutty
  Scenario: Marcar una tarea importante como completada
  Given la lista de tareas contiene las siguientes tareas:
    | Tarea                 | Estado  | Importante |
    | Revisar informe       | Pendiente | Sí        |
    | Llamar al cliente     | Pendiente | No        |
  When el usuario marca la tarea "Revisar informe" como completada
  Then la lista de tareas debería mostrar la tarea "Revisar informe" como completada

  







