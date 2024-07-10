def check_password_strength(password):
     #check if minimum length is 8
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."
    
    # Character type checks
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
   # Print result based on evaluation
    if has_upper and has_lower and has_digit and has_special:
        return "Strong Password: Meet all requirements"
    elif has_upper and has_lower and has_digit:
        return "Moderate Password: Lacks Special Characters "
    else:
        return "Weak Password: Does not meet complexity requirements."


password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"Password Strength: {strength}")
