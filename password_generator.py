import random
import string

def generate_password(length, include_uppercase, include_lowercase, include_digits, include_symbols):
  """Generates a secure password based on user-specified criteria.

  Args:
      length (int): Desired length of the password.
      include_uppercase (bool): Whether to include uppercase letters.
      include_lowercase (bool): Whether to include lowercase letters.
      include_digits (bool): Whether to include digits.
      include_symbols (bool): Whether to include symbols.

  Returns:
      str: The generated password.
  """

  all_chars = ""
  if include_uppercase:
    all_chars += string.ascii_uppercase
  if include_lowercase:
    all_chars += string.ascii_lowercase
  if include_digits:
    all_chars += string.digits
  if include_symbols:
    all_chars += string.punctuation

  if not all_chars:
    raise ValueError("Please select at least one character type.")

  # Shuffle the characters to prevent predictable patterns
  random.shuffle(list(all_chars))
  password = ''.join(random.choices(all_chars, k=length))
  return password

def main():
  """Prompts the user for desired password length and character types, and generates a password."""

  while True:
    try:
      length = int(input("Enter desired password length (minimum 8 characters): "))
      if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

      include_uppercase = input("Include uppercase letters (y/n)? ").lower() == 'y'
      include_lowercase = input("Include lowercase letters (y/n)? ").lower() == 'y'
      include_digits = input("Include digits (y/n)? ").lower() == 'y'
      include_symbols = input("Include symbols (y/n)? ").lower() == 'y'

      password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_symbols)
      print(f"Your secure password is: {password}")
      break
    except ValueError as e:
      print(f"Error: {e}")

if __name__ == "__main__":
  main()
