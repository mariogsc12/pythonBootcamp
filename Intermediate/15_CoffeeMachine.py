# DAY 15 FINAL PROJECT - COFFEE MACHINE

import art

class CoffeeMachine:
    def __init__(self):
        self.status = True
        self.resources = {"water":          # Amount of water [ml]
                            {"value":300,
                            "unit":"ml"},     
                        "milk":             # Amount of milk [ml]
                            {"value":200,
                            "unit":"ml"},      
                        "coffee":           # Amount of coffee [g]
                            {"value":100,
                            "unit":"g"}}   

        self.order = {"espresso":
                        {"ingredients":
                            {"water":50,
                             "coffee":18},
                        "cost":1.5},
                    "latte":
                        {"ingredients":
                            {"water":200,
                             "milk":150,
                             "coffee":24},
                        "cost":2.5},
                    "cappuccino":
                        {"ingredients":
                            {"water":250,
                             "milk":100,
                             "coffee":24},
                        "cost":3.0}
                    }
                            
        self.userActions = list(self.order.keys()) + ["report", "off"]

        # Amount of money introduced by the user [$]
        self.money = {"quarters":0,
                      "dimes":0,
                      "nickels":0,
                      "pennies":0}     

        # Amount of money earned by the machine [$]
        self.profit = 0


    def __call__(self, *args, **kwds):
        """ Wrapper for calling run function """

        self.run()


    def checkUserInput(self):
        """ Checks and ensure that the text introduced by the user matches with one of the user actions.\n
            It returns the user input """
        
        userInput = ""
        while userInput not in self.userActions: # Report and off options are hidden for users
            userInput = input(f"What would you like? {list(self.order.keys())}: ").lower()
            if userInput not in self.userActions:
                print("-- ERROR - INVALID INPUT --")

        return userInput
    

    def handleUserCoins(self):
        """ Stores the coins introduced by the user\n
            It receives the coffee type and calculates the change  """

        print("Please insert coins.")
        conversionToDollars = 0
        for coin, value in self.money.items():
            if coin == "quarters":
                conversionToDollars = 0.25
            elif coin == "dimes":
                conversionToDollars = 0.1
            elif coin == "nickles":
                conversionToDollars = 0.05
            elif coin == "pennies":
                conversionToDollars = 0.01

            self.money[coin] = int(input(f"How many {coin}?: "))*conversionToDollars

        return sum(self.money.values())
    

    def manageTransaction(self, coffeeType):
        """ Checks if the inserted money is enough to purchase the drink selected.\n
            If so, calculates the change and returns True.  """

        insertedMoney = self.handleUserCoins()

        if insertedMoney == self.order[coffeeType]["cost"]:
            print(f"Preparing {coffeeType}...")
            self.profit += self.order[coffeeType]["cost"]
            return True
        elif insertedMoney > self.order[coffeeType]["cost"]:
            print(f"Preparing {coffeeType}...")
            change = round(insertedMoney - self.order[coffeeType]["cost"],2)
            print(f"Here is ${change} in change.")
            self.profit += self.order[coffeeType]["cost"]
            return True
        else: 
            print("Sorry that's not enough money. Money refunded.")
            return False


    def manageUserInput(self, userInput):
        """ Manages the action introduced by the user """

        if userInput == "off":
            self.status = False
        elif userInput == "report":
            self.generateReport()
        elif userInput in list(self.order.keys()):
            self.prepareCofee(userInput)


    def checkResources(self,coffeeType):
        """ Checks if the available resources are enough to prepare the selected coffee.\n
            Returns True or False """
        
        for ingredient in self.order[coffeeType]["ingredients"]:
            if self.resources[ingredient]["value"] < self.order[coffeeType]["ingredients"][ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
                return False
            
        return True
    

    def prepareCofee(self,coffeeType):
        """Prepares the selected coffee.\n
        It first checks if there are sufficient ingredients.\n
        If so, it reduces the ingredient quantities and handles the payment process.
        """

        if self.checkResources(coffeeType):
            for ingredient in self.order[coffeeType]["ingredients"]:
                self.resources[ingredient]["value"] -= self.order[coffeeType]["ingredients"][ingredient]
            
            self.manageTransaction(coffeeType)


    def generateReport(self):
        """ Generates the report with the ingredients and the available money"""
        for ingredient, value in self.resources.items():
            print(f"{ingredient}: {value["value"]} {value["unit"]}")

        print(f"Money: ${self.profit}")


    def run(self):
        """ Main function. It calls the manager with the machine's logic """
        art.tprint("Coffee  Machine")
        while self.status == True:
            userInput = self.checkUserInput()
            self.manageUserInput(userInput)
            

def main():
    CoffeeMachine()()

if __name__ == "__main__":
    main()