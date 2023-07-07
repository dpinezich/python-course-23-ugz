from contacts import Address
#address = Address('55 Main St.', 'Concord', 'NH', '03301')
#print(address)

class Employee:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

    def __str__(self):
        return f"I am: {self.name} id: {self.id} from: {self.address}"


manager = Employee(1, 'Mary Poppins', 3000)
manager.address = Address(
    '121 Admin Rd',
    'Concord',
    'NH',
    '03301'
)

print(manager)