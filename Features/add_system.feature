Feature: Add a Local Network Device in Uptime Infrastructure Monitor

  Scenario: Successfully add a local network device
    Given the user is on the Uptime Infrastructure Monitor dashboard
    When the user navigates to My Infrastructure
    And the user clicks Add System button
    And the user switches to the new window
    And the user fills in the system details with display name "nagesh Localhost", description "description", and hostname "Localhost"
    And the user clicks Save
    And the user switches back to the original window
    Then the system "nagesh Localhost" should be added successfully