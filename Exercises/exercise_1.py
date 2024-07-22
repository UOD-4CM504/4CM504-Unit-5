def calc_retail_price(wholesale, markup):
  return wholesale * (1 + markup/100)

def main():
  wholesale = input("Please enter a wholesale cost:\n")
  markup = input("Please enter a markup percentage:\n")
  retail = calc_retail_price(float(wholesale), float(markup))
  print(f"The retail price is £{retail:.2f}.")

# This is needed for the tests. This is the now the first bit of code Python will run.
# Please ask if you are curious, but it is enough to understand that this calls the main() function and runs whatever code you have in there.
if __name__ == "__main__":
  main() # calls the main function
