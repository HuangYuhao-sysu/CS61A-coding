

class Email:
    """Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.message = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name


class Mailman:
    """Each Mailman has an instance attribute clients, which
    is a dictionary that associates client names with
    client objects.
    """""
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the inbox of the client
        it is addressed to.
        """
        self.clients[email.recipient_name].receive(email)


    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds it
        to the clients instance attribute.
        """
        self.clients.update(client_name=client)

class Client:
    """Every Client has instance attributes name (which is
    used for addressing emails to the client), mailman
    (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received).
    """
    def __init__(self, mailman, name):
        self.inbox = []
        self.name = name
        self.mailman = mailman
        self.mailman.register_client(self, name)

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the
        given recipient client.
        """
        my_message = Email(msg, self.name, recipient_name)
        self.mailman.send(my_message)

    def receive(self, email):
        """Take an email and add it to the inbox of this
        client.
        """
        self.inbox.append(email)

class Pet(object):
    def __init__(self, name, owner):
        self.is_alive = True # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)


class Dog(Pet):
    def __init__(self, name, owner):
        Pet.__init__(self, name, owner)

    def talk(self):
        print(self.name + ' says woof!')


class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self, name, owner)
        self.lives = lives
        self.is_alive = True

    def talk(self):
        """A cat says meow! when asked to talk."""
        print(self.name + ' says mewo!')

    def lose_life(self):
        """A cat can only lose a life if they have at
        least one life. When lives reaches zero, 'is_alive'
        becomes False.
        """
        if self.lives >= 1:
            self.lives -= 1

        if self.lives == 0:
            self.is_alive = False

class NoisyCat(Cat): # Fill me in!
    """A Cat that repeats things twice."""

    def talk(self):
        """Repeat What a Cat says twice"""
        for _ in range(2):
            Cat.talk(self)

class A:
    def f(self):
        return 2
    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x - 1)

class B(A):
    def f(self):
        return 4

class Yolo:

    def __init__(self, x):
        self.motto = x

    def g(self, y):
        return self.motto+y
