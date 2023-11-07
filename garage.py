# Object Oriented Parking Garage Assignment

class Garage():

    def __init__(self, tickets, parkingSpaces):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = {}

    def takeTicket(self):
        if self.tickets > 0:
            self.tickets -= 1
            self.parkingSpaces -= 1
            ticket_number = input('enter a number to assign your ticket: ')
            self.currentTicket['ticket_number'] = ticket_number
            print('ticket taken.')
        else:
            print('sorry, the parking garage is full.')

    def payForParking(self, key, value):
        self.currentTicket[key] = value
        paid = int(input('enter an amount to pay: '))
        ticket_amount = int(self.currentTicket['ticket_number'])
        if paid >= ticket_amount:
            self.currentTicket['paid'] = True
            print('your ticket has been paid, please leave within 15 minutes')
        else:
            print(f'insufficient amount. Please pay a minimum of ${ticket_amount}')

    def leaveGarage(self):
        if self.currentTicket.get('paid'):
            self.tickets += 1
            self.parkingSpaces += 1
            print('thank you, have a nice day!')
        else:
            print('your ticket has not been paid.')
            print(self.currentTicket)
            pay_now = input('enter your ticket number: ')
            if pay_now == self.currentTicket['ticket_number']:
                ticket = input('please enter 25 to leave: ')
                if ticket == '25':
                    print('thank you, have a nice day!')
                    self.tickets += 1
                    self.parkingSpaces += 1
                else:
                    print('insufficient amount')
                    print(ticket)
                    self.tickets += 1
                    self.parkingSpaces += 1
            else:
                print('no such ticket')

def run():
    garage = Garage(2, 2) # amount of tickets available, amount of spaces available

    garage.takeTicket()

    while True:
        
        action = input('would you like to take another ticket, pay for your ticket, leave the garage, or quit? ')

        if action == 'quit':
            break
        elif action == 'take':
            garage.takeTicket()
        elif action == 'pay':
            garage.payForParking('ticket_number', 25)
        elif action == 'leave':
            garage.leaveGarage()
        else:
            print('invalid input. please enter take/pay/leave/quit.')

run()