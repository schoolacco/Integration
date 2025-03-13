class Addition:
    def add_numbers(a,b):
      try:
        return int(a) + int(b)
      except ValueError:
         return "One or more value(s) were not an integer"