def print_colored_text(text):
    reset = "\033[0m"
    green = "\033[32m"
    print(f"{green}{text}{reset}")

# 1
print_colored_text("task --> 1")
print("Programming" + "***" + "Essential" + "***" + "in" + "..." + "Python")

# 2
print_colored_text("task --> 2")
print("     *")
print("    * *")
print("   *   *")
print("  *     *")
print(" ***   ***")
print("   *   *")
print("   *   *")
print("   *****")

# 3
print_colored_text("task --> 3")
print("I'm student")

# 4
print_colored_text("task --> 4")
print("\"I'm\"\n\"\"learning\"\"\n\"\"\"Python\"\"\"")

# 5
print_colored_text("task --> 5")
print(0o500)

# 6
print_colored_text("task --> 6")
print(0x777)