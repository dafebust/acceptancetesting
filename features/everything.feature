Feature: To-Do List Manager

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task          |
      | Buy Groceries |
      | Pay bills     |
    When the user lists all tasks
    Then the output should contain:
      | Task          |
      | Buy Groceries |
      | Pay bills     |

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Task          | Status  |
      | Buy groceries | Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: Attempt to mark a non-existent task as completed
    Given the to-do list is empty
    When the user attempts to mark a task "Non-existent task" as completed
    Then the to-do list should still be empty

  Scenario: Clear the to-do list when it is already empty
    Given the to-do list is empty
    When the user clears the to-do list
    Then the to-do list should remain empty

  Scenario: Edit a task in the to-do list
    Given the to-do list contains tasks:
      | Task          | Status  |
      | Buy groceries | Pending |
      | Pay bills     | Pending |
    When the user edits the task "Buy groceries" to "Buy weekly groceries"
    Then the to-do list should contain:
      | Task                 | Status  |
      | Buy weekly groceries | Pending |
      | Pay bills            | Pending |

  Scenario: Remove a task from the to-do list
    Given the to-do list contains tasks:
      | Task          | Status  |
      | Buy groceries | Pending |
      | Pay bills     | Pending |
    When the user removes the task "Buy groceries"
    Then the to-do list should contain:
      | Task      | Status  |
      | Pay bills | Pending |

  Scenario: List all tasks when the to-do list is empty
    Given the to-do list is empty
    When the user lists all tasks
    Then the output should be empty

  @addtasktolist
  Scenario: Add a task with description to the list
    Given the to-do list is empty
    When the user adds a task "Buy groceries" with the description "Go to the supermarket and buy necessary items for the week"
    Then the to-do list should contain the task "Buy groceries" with the description "Go to the supermarket and buy necessary items for the week"

  @markimportantcompleted
  Scenario: Mark an important task as completed
    Given the to-do list contains tasks:
      | Task               | Status   | Important |
      | Review report      | Pending  | Yes       |
      | Call the client    | Pending  | No        |
    When the user marks the task "Review report" as completed
    Then the to-do list should show the task "Review report" as completed
