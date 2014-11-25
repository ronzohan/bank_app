Feature: Bank web application to retrieve
		 and update customer accounts
		 As a customer I wish to be able to view my balance
	     and update my balance
		 and withdraw from my balance

		 @finished
		 Scenario: Retrieve customer balance
		 Given I create account "1111" with balance of "50"
		 And I visit the homepage
		 When I enter the account number "1111"
		 Then I see a balance of "50"
		 
		 @finished
		 Scenario Outline: Retrieve customer balance
		 Given I create account "<account_number>" with balance of "<balance>"
		 And I visit the homepage
		 When I enter the account number "<account_number>"
		 Then I see a balance of "<balance>"
		 
		 Examples:
		 |account_number|balance|
		 |1111          |50     |
		 |2222          |50     |
		 |3333          |50     |
		 |4444          |50     |
		 
		 Scenario Outline: Retrieve customer balance
		 Given I create the following account:
		 |account_number|balance|
		 |1111          |50     |
		 And I visit the homepage
		 When I enter the account number "1111"
		 Then I see a balance of "50"
				 		 