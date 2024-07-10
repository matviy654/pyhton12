#task1
# def main():
#     try:
#         name = input("Введіть ваше ім'я: ")
#         age = int(input("Введіть ваш вік: "))
        
#         if age < 0 or age > 130:
#             raise ValueError("Некоректний вік. Введіть вік у діапазоні від 0 до 130.")
        
#         print(f"Привіт, {name}! Твій вік — {age}.")
#     except ValueError as e:
#         print(f"Помилка: {e}")

# if __name__ == "__main__":
#     main()
#task2
# def format_greeting(name, age):
#     if age < 0 or age > 130:
#         raise ValueError("Некоректний вік. Введіть вік у діапазоні від 0 до 130.")
#     return f"Привіт, {name}! Твій вік — {age}."

# def main():
#     try:
#         name = input("Введіть ваше ім'я: ")
#         age = int(input("Введіть ваш вік: "))
#         greeting = format_greeting(name, age)
#         print(greeting)
#     except ValueError as e:
#         print(f"Помилка: {e}")

# if __name__ == "__main__":
#     main()
# def format_greeting(name, age):
#     try:
#         if age < 0 or age > 130:
#             raise ValueError("Некоректний вік. Введіть вік у діапазоні від 0 до 130.")
#         return f"Привіт, {name}! Твій вік — {age}."
#     except ValueError as e:
#         return f"Помилка: {e}"

# def main():
#     name = input("Введіть ваше ім'я: ")
#     try:
#         age = int(input("Введіть ваш вік: "))
#     except ValueError:
#         print("Помилка: Вік повинен бути числом.")
#         return
#     greeting = format_greeting(name, age)
#     print(greeting)

# if __name__ == "__main__":
#     main()

#task3
# def get_positive_numbers():
#     numbers = []
#     while True:
#         try:
#             user_input = input("Введіть додатне число (або 'stop' для завершення): ")
#             if user_input.lower() == 'stop':
#                 break
#             number = float(user_input)
#             if number <= 0:
#                 raise ValueError("Число повинно бути більше нуля.")
#             numbers.append(number)
#         except ValueError as e:
#             print(f"Помилка: {e}")
#     return numbers

# def analyze_numbers(numbers):
#     try:
#         for num in numbers:
#             if num <= 0:
#                 raise ValueError("Виявлено від'ємне значення.")
#         total_sum = sum(numbers)
#         return total_sum
#     except ValueError as e:
#         print(f"Помилка: {e}")
#         return None

# def main():
#     numbers = get_positive_numbers()
#     result = analyze_numbers(numbers)
#     if result is not None:
#         print(f"Сума всіх чисел: {result}")

# if __name__ == "__main__":
#     main()

#task4
# def calculate_sum(numbers):
#     for num in numbers:
#         if num <= 0:
#             raise ValueError("Виявлено від'ємне значення.")
#     return sum(numbers)

# def main():
#     numbers = []
#     while True:
#         try:
#             user_input = input("Введіть додатне число (або 'stop' для завершення): ")
#             if user_input.lower() == 'stop':
#                 break
#             number = float(user_input)
#             if number <= 0:
#                 raise ValueError("Число повинно бути більше нуля.")
#             numbers.append(number)
#         except ValueError as e:
#             print(f"Помилка: {e}")

#     try:
#         total_sum = calculate_sum(numbers)
#         print(f"Сума всіх чисел: {total_sum}")
#     except ValueError as e:
#         print(f"Помилка: {e}")

# if __name__ == "__main__":
#     main()
# def calculate_sum(numbers):
#     try:
#         for num in numbers:
#             if num <= 0:
#                 raise ValueError("Виявлено від'ємне значення.")
#         return sum(numbers)
#     except ValueError as e:
#         return f"Помилка: {e}"

# def main():
#     numbers = []
#     while True:
#         try:
#             user_input = input("Введіть додатне число (або 'stop' для завершення): ")
#             if user_input.lower() == 'stop':
#                 break
#             number = float(user_input)
#             if number <= 0:
#                 raise ValueError("Число повинно бути більше нуля.")
#             numbers.append(number)
#         except ValueError as e:
#             print(f"Помилка: {e}")

#     total_sum = calculate_sum(numbers)
#     if isinstance(total_sum, str):
#         print(total_sum)
#     else:
#         print(f"Сума всіх чисел: {total_sum}")

# if __name__ == "__main__":
#     main()
