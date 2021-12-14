module SavingsAccount
    def self.interest_rate(balance)
      if balance < 0
        interest_rate = -3.213
      elsif balance >= 0 && balance < 1000
        interest_rate = 0.5
      elsif balance >= 1000 && balance < 5000
        interest_rate = 1.621
      elsif balance >= 5000
        interest_rate = 2.475
      end
      return interest_rate 
    end
  
    def self.annual_balance_update(balance)
      interest = (self.interest_rate(balance)/100) * balance
      if balance < 0
        interest = -interest
      end
      new_balance = interest + balance
      return new_balance
      
    end
  
    def self.years_before_desired_balance(current_balance, desired_balance)
      current = current_balance
      num_years = 0
  
      while current < desired_balance
        current = self.annual_balance_update(current)
        num_years += 1
      end
      return num_years
    end
  end
  