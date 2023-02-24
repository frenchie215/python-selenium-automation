# Created by francesgibson at 2/23/23
Feature: Amazon search tests

  Scenario: User can search for a product on Amazon
    Given Open Amazon page
    When Input text matcha
    When Click on search button
    Then Verify that text "matcha" is shown