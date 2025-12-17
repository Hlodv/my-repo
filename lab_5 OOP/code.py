class MyName:
    """Опис класу / Документація"""
    total_names = 0 

    def __init__(self, name=None) -> None:
        # Перевірка на цифри та символи (Завдання 7)
        if name and not str(name).isalpha() and name != "Anonymous":
             raise ValueError("Ім'я може містити лише літери!")

        # Робимо ім'я з великої літери (Завдання 5)
        if name is not None:
            name = name.capitalize()

        # Якщо None — створюємо Anonymous (Завдання 1)
        self.name = name if name is not None else self.anonymous_user().name
        
        MyName.total_names += 1 
        self.my_id = self.total_names

    @property
    def whoami(self) -> str: 
        return f"My name is {self.name}"
    
    @property
    def my_email(self) -> str:
        return self.create_email()

    # Додано властивість full_name (Завдання 8)
    @property
    def full_name(self) -> str:
        return f"User #{self.my_id}: {self.name} ({self.my_email})"
    
    # Змінено: додано аргумент domain (Завдання 6)
    def create_email(self, domain="itcollege.lviv.ua") -> str:
        return f"{self.name.lower()}@{domain}"

    # Додано метод підрахунку літер (Завдання 3)
    def count_letters(self) -> int:
        return len(self.name)

    # Додано метод збереження у файл (Завдання 9)
    def save_to_file(self, filename="users.txt"):
        with open(filename, "a", encoding="utf-8") as f:
            f.write(self.full_name + "\n")

    @classmethod
    def anonymous_user(cls):
        return cls("Anonymous")
    
    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:
        return f"You say: {message}"

# --- Тіло програми ---

# Додано власне ім'я (Завдання 4)
names = ("Bohdan", "Marta", "Vitalik", None) 

all_names = {}
for name in names:
    try:
        all_names[name] = MyName(name)
    except ValueError as e:
        print(f"Помилка для {name}: {e}")

for name, me in all_names.items():
    print(f"Об'єкт: {me.full_name}")
    print(f"Кількість літер: {me.count_letters()}")
    # Зміна привітання (Завдання 2)
    print(me.say_hello("Привіт, світе!")) 
    me.save_to_file()

print(f"\nКількість імен у списку: {len(names)}")
print(f"Кількість створених об'єктів: {MyName.total_names}")