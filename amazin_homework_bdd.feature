# Created by francesgibson at 2/23/23
Feature: Amazon log in page


  Scenario: User can see Amazon sign in page after clicking on returns and orders
    Given Open Amazon page
    When Click Returns and Orders button
    Then Verify Sign in page opened: Sign In header is visible, email input field is present