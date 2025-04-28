Feature: Login
  Scenario: Login to the application with valid username and password
    Given the user is on the Login Page
    When the user enters "USERNAME" and "PASSWORD"
    Then the user should be able to log in to the application