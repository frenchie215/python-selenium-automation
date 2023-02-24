# Created by Svetlana at 4/4/19 - Test Cases
  #BDD behavior driven development
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    #condition = given
    Given Open Google page
    #action = when. and (copies the word above it), but
    When Input Desk into search field
    And Click on search icon
    #verification = then
    Then Product results for Desk are shown
